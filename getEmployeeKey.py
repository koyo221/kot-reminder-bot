import sys
import requests
from repositories.SpreadSheetService import SpreadSheetService

employee_code = sys.argv[1]

url = f'https://api.kingtime.jp/v1.0/employees/{employee_code}'
access_token = 'test'
proxies = 'p'
headers = {
    'Authorization': f"Bearer {access_token}",
    'content-type': "application/json",
}

response = requests.get(url, headers=headers, proxies=proxies).json()
key = response['key']
name = f"{response['first_name']}{response['last_name']}"

sss = SpreadSheetService()
cell = sss.find(employee_code)

sss.update_cell(cell.row, cell.col + 1, key)
sss.update_cell(cell.row, cell.col + 3, name)

print('done!')
