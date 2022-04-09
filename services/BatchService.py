from constants import *
from linebot.models import TextSendMessage
from repositories.SpreadSheetService import SpreadSheetService

from .LineService import LineService
from .MessageService import MessageService
from .UtilityService import UtilityService


class BatchService:


    def __init__(self) -> None:
        self.sheet_service = SpreadSheetService()
        self.util_service = UtilityService()
        #TODO インスタンス変数を必要としない処理がMessageServiceにあるのがそもそも良くない
        #　（ただMessageSendServiceみたいなものを作るのはやりすぎという気もする）　どこ？？
        self.message_service = MessageService('batch')


    #TODO リファクタリングの余地あり
    def exec_batch(self):
        if not self.util_service.is_weekday():
            return

        sheet = self.sheet_service.get_all()
        dt = self.util_service.get_date()

        for i, row in enumerate(sheet):
            if (i == 0):
                continue
            if self.util_service.is_ten_minutes_before(dt, row[1]):
                try:
                    push = self.message_service.is_special(
                        ResponseConst['RESPONSE_ATTENDANCE'],
                        ResponseConst['RESPONSE_ATTENDANCE_SPECIAL'])
                    #TODO この処理ってLineServiceの役割
                    LineService.line_bot_api.push_message(row[0], TextSendMessage(text=push))
                except:
                    print(f"batch failed for user {row[0]}")
            if self.util_service.is_ten_minutes_after(dt, row[2]):
                try:
                    push = self.message_service.is_special(
                        ResponseConst['RESPONSE_LEAVE'],
                        ResponseConst['RESPONSE_LEAVE_SPECIAL'])
                    LineService.line_bot_api.push_message(row[0], TextSendMessage(text=push))
                except:
                    print(f"batch failed for user {row[0]}")
