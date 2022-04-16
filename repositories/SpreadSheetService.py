import gspread, os
from oauth2client.service_account import ServiceAccountCredentials

class SpreadSheetService:

    #TODO 全部まとめて持てば良い
    client = {
        "type": "service_account",
        "project_id": os.environ.get('PROJECT_ID', ''),
        "private_key_id": os.environ.get('PRIVATE_KEY_ID', ''),
        "private_key": os.environ.get('PRIVATE_KEY', ''),
        "client_email": os.environ.get('CLIENT_EMAIL', ''),
        "client_id": os.environ.get('CLIENT_ID', ''),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.environ.get('CLIENT_X509_CERT_URL', '')
    }
    client["private_key"] = client["private_key"].replace("\\n", "\n")
    # ローカル用の処理を整備する（いまはcredsを切り変える）
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(client, scope)
    # credentials = ServiceAccountCredentials.from_json_keyfile_name('../client_secret.json', scope)
    gs = gspread.authorize(credentials)
    sheets = gs.open("kot_reminder_bot")


    def get_all(self):
        return SpreadSheetService.sheets.sheet1.get()


    def find(self, str):
        return SpreadSheetService.sheets.sheet1.find(str)


    def get_cell(self, row, col):
        return SpreadSheetService.sheets.sheet1.cell(row, col)


    def update_cell(self, row, col, val):
        SpreadSheetService.sheets.sheet1.update_cell(row, col, val)


    def append_row(self, value):
        SpreadSheetService.sheets.sheet1.append_row(value)


    def reset_stamping_count(self):
        """打刻回数をリセットする
        """
        length = len(self.get_all())
        SpreadSheetService.sheets.sheet1.update(f"H2:H{length}", [[0]]*(length - 1))


    def get_ek_from_user_id(self, user_id: str):
        cell = self.find(user_id)
        return self.get_cell(cell.row, cell.col + 4).value
