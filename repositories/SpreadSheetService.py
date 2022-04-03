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
    # credentials = ServiceAccountCredentials.from_json_keyfile_name('./client_secret.json', scope)
    gs = gspread.authorize(credentials)
    sheets = gs.open("kot_reminder_bot")

    def get_all(self):
        return SpreadSheetService.sheets.sheet1.get()

    def find(self, str):
        return SpreadSheetService.sheets.sheet1.find(str)
