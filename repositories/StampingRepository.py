from SpreadSheetService import SpreadSheetService
import requests

class StampingRepository:

    def __init__(self, id) -> None:
        self.id = id
        self.sss = SpreadSheetService()


    def stamp(self):
        cell_id = self.sss.find(self.id)
        stamping_count = self.get_stamping_count(cell_id)
        if stamping_count >= 2:
            return
        employee_key = self.get_employee_key(cell_id)
        self.execute_kot_api(employee_key)
        self.add_stamping_count(cell_id, stamping_count)


    def add_stamping_count(self, cell_id, stamping_count):
        self.sss.update_cell(cell_id.row, cell_id.col + 7, stamping_count + 1)


    def get_employee_key(self, cell_id):
        return self.sss.get_cell(cell_id.row, cell_id.col + 4).value


    def get_stamping_count(self, cell_id):
        return int(self.sss.get_cell(cell_id.row, cell_id.col + 7).value)


    #TODO ここにあるべき処理ではないのかもしれない…………………………
    def execute_kot_api(self, ec):
        url = f"https://api.kingtime.jp/v1.0/daily-workings/timerecord/{ec}"
        proxies = ''
        access_token = ''
        headers = {
            'Authorization': f"Bearer {access_token}",
            'content-type': "application/json",
        }

        payload = {
            'date': '',
            'time': ''
        }

        response = requests.post(url, headers=headers, data=payload, proxies=proxies)
