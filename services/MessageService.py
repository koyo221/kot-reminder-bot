import random
from typing import Literal, Union

from constants import *

from .MatcherService import MatcherService
from .UtilityService import UtilityService


class MessageService:


    def __init__(self, message: str):
        self.message = message
        self.utility_service = UtilityService()
        self.matcher_service = MatcherService(self.message)


    def reply(self) -> str:
        """messageの内容に応じて返答する

        Returns:
            str: レスポンスメッセージ
        """
        #NOTE こんな型ってあっていいの？そもそもの設計がだめかもね
        result: Union[str, list[str], bool]

        result = self.matcher_service.is_employee_code()
        if result:
            return self.handle_employee_code(result)

        result = self.matcher_service.is_valid_worktime()
        if (result):
            return self.handle_worktime(result)

        result = self.matcher_service.is_debugging()
        if (result):
            return self.handle_debugging()

        result = self.matcher_service.match(RequestConst)
        if (result):
            return self.handle_match(result)

        return ErrorConst['GENERAL_ERROR']


    def handle_worktime(self, result: Union[Literal['invalid'], list[str]])->str:
        """勤務時間を受け取った時、対応するメッセージを返す

        Args:
            result (Union[Literal['invalid'], list[str]]): is_valid_worktime()の返り値

        Returns:
            str: レスポンスメッセージ
        """
        if result == 'invalid':
            return WorkTimeResponses['WORK_TIME_INVALID']

        return f"{WorkTimeResponses['WORK_TIME_VALID1']}\
            {result[0]}:00\n{WorkTimeResponses['WORK_TIME_VALID2']}\
            {result[1]}:00\n{WorkTimeResponses['WORK_TIME_VALID3']}"


    def is_valid_worktime(self, list: list[str])->bool:
        """妥当な勤務時間か

        Args:
            list (list[str]): 始業/終業

        Returns:
            bool: 妥当である
        """
        return int(list[0]) >= int(list[1])


    def handle_debugging(self)->str:
        """デバッグメッセージを受け取ったとき、対応するメッセージを返す

        Returns:
            str: レスポンスメッセージ
        """
        return WorkTimeResponses['DEBUGGING']


    def handle_match(self, key: str)->str:
        """keyを受け取ったとき、対応するメッセージを返す

        Args:
            key (str): RequestConstのキー

        Returns:
            str: レスポンスメッセージ
        """
        if key == 'REQUEST_ARTICLES':
            return random.choice(ResponseConst['RESPONSE_ARTICLES'])

        if key == 'REQUEST_ATTENDANCE':
            return self.is_special(
                ResponseConst['RESPONSE_ATTENDANCE'],
                ResponseConst['RESPONSE_ATTENDANCE_SPECIAL'])

        if key == 'REQUEST_LEAVE':
            return self.is_special(
                ResponseConst['RESPONSE_LEAVE'],
                ResponseConst['RESPONSE_LEAVE_SPECIAL'])

        if key == 'REQUEST_OVERWORK':
            return random.choice(ResponseConst['RESPONSE_OVERWORK'])

        if key == 'REQUEST_STAMPING':
            return self.is_special(
                ResponseConst['RESPONSE_STAMPING'],
                ResponseConst['RESPONSE_STAMPING_SPECIAL'])

        return random.choice(ResponseConst['RESPONSE_NO_MATCH'])


    def is_special(self, normal: str, special: list[str])->str:
        """10%の確率で特別なメッセージを返す

        Args:
            normal (str): 通常時のメッセージ
            special (list[str]): 特別なメッセージのリスト

        Returns:
            str: レスポンスメッセージ
        """
        if self.utility_service.slot_true_chance(0.1):
            return f"{random.choice(special)}{ResponseConst['KOT_URL']}"
        return f"{normal}{ResponseConst['KOT_URL']}"

    def handle_employee_code(self, employee_code):
        return f"{EmployeeCodeResponses['EMPLOYEE_CODE']}{employee_code}{EmployeeCodeResponses['REGISTERED']}"
