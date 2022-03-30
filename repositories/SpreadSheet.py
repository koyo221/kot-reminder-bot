import gspread, os
from oauth2client.service_account import ServiceAccountCredentials

class SpreadSheet:

    client = {
        "type": "service_account",
        "project_id": os.environ.get("project_id", ''),
        "private_key_id": os.environ.get("private_key_id", ''),
        "private_key": os.environ.get("private_key", ''),
        "client_email": os.environ.get("client_email", ''),
        "client_id": os.environ.get("client_id", ''),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.environ.get("client_x509_cert_url", '')
    }

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(client, scope)
    # credentials = ServiceAccountCredentials.from_json_keyfile_name('./client_secret.json', scope)
    gs = gspread.authorize(credentials)
    sheets = gs.open("kot_reminder_bot")

# list_of_hashes = sheet.get("A1")
# print(list_of_hashes)
# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# credentials = ServiceAccountCredentials.from_json_keyfile_name('../client_secret.json', scope)
# gs = gspread.authorize(credentials)

# sheet = gs.open("kot_reminder_bot").sheet1
# list_of_hashes = sheet.get("A1")
# print(list_of_hashes)
