import os

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

class LineService:
    line_bot_api = LineBotApi(os.environ.get('LINE_BOT_CHANNEL_ACCESS_TOKEN', ''))
    handler = WebhookHandler(os.environ.get('LINE_BOT_CHANNEL_SECRET', ''))
