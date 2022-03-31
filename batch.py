from repositories.WorkTimeRepository import WorkTimeRepository
import datetime, pytz, os
from linebot import LineBotApi
from linebot.models import TextSendMessage

line_bot_api = LineBotApi(os.environ.get('LINE_BOT_CHANNEL_ACCESS_TOKEN', 'test'))

# TODO None, None, Noneって最悪すぎる
work_time_repository = WorkTimeRepository(None, None, None)
sheet = work_time_repository.get_all()

now = str(datetime.datetime.now(pytz.timezone('Asia/Tokyo')).hour)
print(now)

# TODO 回しすぎ
for row in sheet:
    for cell in row:
        if (cell == now):
            # try:
                print(row[0])
                line_bot_api.push_message(row[0], TextSendMessage(text='これがpush通知です'))
            # except:
            #     print(failed)
            #     pass
