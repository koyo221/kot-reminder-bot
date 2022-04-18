import requests
import os
from .UtilityService import UtilityService
from repositories.SpreadSheetService import SpreadSheetService
from repositories.StampingRepository import StampingRepository

class KingOfTimeService:
    fixie = os.environ.get('FIXIE_URL', '')
    access_token = os.environ.get('KOT_ACCESS_TOKEN', '')
    proxies = {
        "http": fixie,
        "https": fixie
    }
    headers = {
        'Authorization': f"Bearer {access_token}",
        'content-type': "application/json",
    }


    def __init__(self) -> None:
        self.us = UtilityService()
        self.sss = SpreadSheetService()


    def stamp(self, user_id):
        """LINEユーザーIDから打刻を行う

        https://developer.kingtime.jp/#%E5%8B%A4%E6%80%A0-%E6%97%A5%E5%88%A5%E6%89%93%E5%88%BB%E3%83%87%E3%83%BC%E3%82%BF-post

        Args:
            ec (str): 従業員コード

        Returns:
            requests.Response: レスポンス
        """

        count = self.add_stamping_count(user_id)
        if count == False:
            return 'ALREADY_STAMPED_ERROR'
        employee_key = self.sss.get_ek_from_user_id(user_id)

        if not employee_key:
            return 'NO_EMPLOYEE_KEY_ERROR'

        url = f"https://api.kingtime.jp/v1.0/daily-workings/timerecord/{employee_key}"
        dt = self.us.get_date()

        payload = {
            'time': self.us.get_kot_time(dt),
            'date': self.us.get_kot_date(dt)
        }

        try:
            response = requests.post(
                url=url,
                headers=KingOfTimeService.headers,
                data=payload,
                proxies=KingOfTimeService.proxies,
                timeout=10)
        except:
            return 'REQUEST_FAILED'

        return response

    def add_stamping_count(self, user_id):
        cell_id = self.sss.find(user_id)
        stamping_count = self.get_stamping_count(cell_id)
        if stamping_count >= 2:
            return False
        self.update_stamping_count(cell_id, stamping_count)


    def get_stamping_count(self, cell_id):
        return int(self.sss.get_cell(cell_id.row, cell_id.col + 7).value)


    def update_stamping_count(self, cell_id, stamping_count):
        self.sss.update_cell(cell_id.row, cell_id.col + 7, stamping_count + 1)
