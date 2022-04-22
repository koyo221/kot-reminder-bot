import re
from typing import Literal, Union
from .UtilityService import UtilityService


class MatcherService:
    """文字列のマッチ処理を扱う
    """


    def __init__(self, message: str):
        self.message = message
        self.util_service = UtilityService()


    def is_valid_worktime(self) -> Union[list[str], Literal['invalid', False]]:
        """入力が妥当な時刻表記であれば、始業時間と就業時間のリストを返す

        Returns:
            Union[list[str], bool]: 妥当な場合、リスト そうでなければFalse
        """
        if re.fullmatch(r'\d\d/\d\d', self.message):
            start = self.message[:2]
            end = self.message[3:]
            if start >= end:
                return 'invalid'
            if not (self.util_service.is_valid_time(start) and self.util_service.is_valid_time(end)):
                return 'invalid'
            return [start, end]
        return False


    def is_debugging(self) -> bool:
        """入力が日付のデバッグ文か

        Returns:
            bool: デバッグ文である
        """
        return True if (re.fullmatch(r'\D\D/\D\D', self.message)) else False


    #TODO keyofみたいな型宣言があればしたほうがよい
    def match(self, dict: dict) -> str:
        """入力が辞書とマッチするか

        Args:
            dict (dict): 反応する文字列の辞書

        Returns:
            Union[str, bool]: 一致すれば辞書のキー しなければFalse
        """
        for key, list in dict.items():
            if self.message in list:
                return key
        return 'no_match'


    def is_employee_code(self):
        if not re.fullmatch(r'従業員番号\d+', self.message):
            return False
        return self.message[5:]
