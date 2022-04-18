import requests
from .UtilityService import UtilityService
from repositories.SpreadSheetService import SpreadSheetService

class KingOfTimeService:
    proxies = ''
    access_token = ''
    headers = {
        'Authorization': f"Bearer {access_token}",
        'content-type': "application/json",
    }


    def __init__(self) -> None:
        self.us = UtilityService()
        self.ss = SpreadSheetService()


    def stamp(self, user_id):
        """LINEユーザーIDから打刻を行う

        https://developer.kingtime.jp/#%E5%8B%A4%E6%80%A0-%E6%97%A5%E5%88%A5%E6%89%93%E5%88%BB%E3%83%87%E3%83%BC%E3%82%BF-post

        Args:
            ec (str): 従業員コード

        Returns:
            requests.Response: レスポンス
        """
        employee_key = self.ss.get_ek_from_user_id(user_id)

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


    def get_employee_code(self):
        pass
