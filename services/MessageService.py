import re, random
from typing import Union
from .UtilityService import UtilityService
from constants import *

class MessageService:

    def __init__(self, message: str):
        self.utilityService = UtilityService()
        self.message = message
        self.start_time: str
        self.end_time: str


    def reply(self) -> str:
        """"返信の文章を返す

        Returns:
            str: 返信文
        """
        reply = self.time_matcher()
        if (reply is None):
            reply = self.msg_matcher()
        return reply


    def time_matcher(self) -> Union[str, None]:
        """時刻設定を行う

        Returns:
            Union[str, None]: 時刻設定完了メッセージ、None
        """
        if (self.message_includes_worktime()):
            if (self.is_valid_worktime()):
                return f"{WorkTimeResponses['WORK_TIME_VALID1']}{self.start_time}:00\n{WorkTimeResponses['WORK_TIME_VALID2']}{self.end_time}:00\n{WorkTimeResponses['WORK_TIME_VALID3']}"
            return WorkTimeResponses['WORK_TIME_INVALID']

        elif (self.somehow_debugging()):
            return WorkTimeResponses['DEBUGGING']
        return


    def message_includes_worktime(self):
        return (re.fullmatch(r'\d\d/\d\d', self.message))


    def is_valid_worktime(self) -> bool:
        """設定可能な時刻であるかどうか判定する

        Note: self.start_time, self.end_timeを他のメソッドで再代入しない

        Returns:
            bool: 設定可能である
        """
        self.start_time = self.message[:2]
        self.end_time = self.message[3:]
        return self.start_time in TimeConst["START_TIME"] and self.end_time in TimeConst["END_TIME"]


    def somehow_debugging(self):
        return (re.fullmatch(r'\D\D/\D\D', self.message))


    # TODO: constantsの持ち方を変えてループで処理できるように修正する
    def msg_matcher(self)-> str:
        """RequestConstに沿ってメッセージを解釈する

        Returns:
            str: 返信
        """

        if (self.message_includes_words_from_list(RequestConst["REQUEST_ARTICLES"])):
            return random.choice(ResponseConst["RESPONSE_ARTICLES"])

        if (self.message_includes_words_from_list(RequestConst["REQUEST_ATTENDANCE"])):
            if (self.utilityService.slot_true_chance(0.9)):
                return f"{ResponseConst['RESPONSE_ATTENDANCE']}{ResponseConst['KOT_URL']}"
            return f"{random.choice(ResponseConst['RESPONSE_ATTENDANCE_SPECIAL'])}{ResponseConst['KOT_URL']}"

        if (self.message_includes_words_from_list(RequestConst["REQUEST_LEAVE"])):
            if (self.utilityService.slot_true_chance(0.9)):
                return f"{ResponseConst['RESPONSE_LEAVE']}{ResponseConst['KOT_URL']}"
            return f"{random.choice(ResponseConst['RESPONSE_LEAVE_SPECIAL'])}{ResponseConst['KOT_URL']}"

        if (self.message_includes_words_from_list(RequestConst["REQUEST_OVERWORK"])):
            return random.choice(ResponseConst["RESPONSE_OVERWORK"])

        return random.choice(ResponseConst["RESPONSE_NO_MATCH"])


    def message_includes_words_from_list(self, list: list[str]) -> bool:
        for str in list:
            if (str in self.message):
                return True
        return False
