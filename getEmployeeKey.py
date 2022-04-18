import os
import sys

import requests

from repositories.SpreadSheetService import SpreadSheetService

# 利用禁止時間帯
# 以下の時間帯（JST）はアクセストークン、打刻登録以外のAPIの利用ができません。
#
# 8:30～10:00
#
# 17:30～18:30

employee_code = sys.argv[1]
fixie = os.environ.get('FIXIE_URL', '')
access_token = os.environ.get('KOT_ACCESS_TOKEN', '')

os.environ['http_proxy'] = fixie
os.environ['https_proxy'] = fixie

url = f'https://api.kingtime.jp/v1.0/employees/{employee_code}'

proxies = {
    "http": fixie,
    "https": fixie
}
headers = {
    'Authorization': f"Bearer {access_token}",
    'content-type': "application/json",
}

response = requests.get(url, headers=headers, proxies=proxies).json()
key = response['key']
name = f"{response['first_name']}{response['last_name']}"

sss = SpreadSheetService()
cell = sss.find(employee_code)

# 従業員キーを更新
sss.update_cell(cell.row, cell.col + 1, key)

# 従業員名を更新
sss.update_cell(cell.row, cell.col + 3, name)

print('done!')
