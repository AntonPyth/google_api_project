from googleapiclient import discovery
from google.oauth2.service_account import Credentials

CREDENTIALS_FILE = 'kochuev-project-fcaad29fd3ab.json'

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]


def auth():
    credentials = Credentials.from_service_account_file(
        filename=CREDENTIALS_FILE, scopes=SCOPES)
    service = discovery.build('sheets', 'v4', credentials=credentials)
    return service, credentials


def create_spreadsheet(service):
    spreadsheet_body = {
        'properties': {
            'title': 'Бюджет путешествий',
            'locale': 'ru_RU'},
        'sheets': [{
            'properties': {
                'sheetType': 'GRID',
                'sheetId': 0,
                'title': 'Отпуск 2077',
                'gridProperties': {
                    'rowCount': 100,
                    'columnCount': 100
                }
            }
        }]
    }

    request = service.spreadsheets().create(body=spreadsheet_body)
    response = request.execute()
    spreadsheet_id = response['spreadsheetId']

    print('https://docs.google.com/spreadsheets/d/' + spreadsheet_id)
    return spreadsheet_id

service, credentials = auth()
spreadsheetId = create_spreadsheet(service)
