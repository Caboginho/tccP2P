import gspread
from oauth2clientoauth2client.service_account import ServiceAccountCredentials

class GoogleSheets:
    def __init__(self, creds_file, sheet_name):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
        self.client = gspread.authorize(creds)
        self.sheet = self.client.open(sheet_name).sheet1

    def insert_row(self, row_data):
        self.sheet.append_row(row_data)

    # Adicionar outros métodos conforme necessário
