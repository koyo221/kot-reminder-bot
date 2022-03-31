from repositories.WorkTimeRepository import WorkTimeRepository
from services.MessageService import MessageService
import datetime, pytz, os
from linebot import LineBotApi
from linebot.models import TextSendMessage

# TODO linebotの接続をクラス化する
line_bot_api = LineBotApi(os.environ.get('LINE_BOT_CHANNEL_ACCESS_TOKEN', 'test'))

# TODO None, None, Noneも"msg"も最悪すぎる→値の運び方を改善する
work_time_repository = WorkTimeRepository(None, None, None)
message_service = MessageService("msg")

sheet = work_time_repository.get_all()

dt = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
hour = str(dt.hour)
weekday = dt.weekday()

if (weekday not in [5, 6]):
    # TODO 回しすぎ
    for row in sheet:
        # start_time
        if (row[1] == hour):
            try:
                print(row[0])
                line_bot_api.push_message(row[0], TextSendMessage(text=message_service.send_start()))
            except:
                print(f"batch failed for user {row[0]}")
        # end_time
        if (row[2] == hour):
            try:
                print(row[0])
                line_bot_api.push_message(row[0], TextSendMessage(text=message_service.send_end()))
            except:
                print(f"batch failed for user {row[0]}")
