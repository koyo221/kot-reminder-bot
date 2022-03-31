import gspread, os
from oauth2client.service_account import ServiceAccountCredentials

class SpreadSheet:

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
