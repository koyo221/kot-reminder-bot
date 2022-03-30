import os
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
from repositories.WorkTimeRepository import WorkTimeRepository
from services.MessageService import MessageService

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get('LINE_BOT_CHANNEL_ACCESS_TOKEN', 'test'))
handler = WebhookHandler(os.environ.get('LINE_BOT_CHANNEL_SECRET', 'test'))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@app.route("/hi")
def hello():
    # message_service = MessageService('記事')
    # work_time_repository = WorkTimeRepository("new yada", "08", "20")

    message_service = MessageService('10/20aa')
    result = True
    # if (message_service.start_time and message_service.end_time):
    if (message_service.message_includes_worktime() and message_service.is_valid_worktime()):

        work_time_repository = WorkTimeRepository(
            'user',
            message_service.start_time,
            message_service.end_time
            )

        result = work_time_repository.update_worktime()

    return message_service.reply(result)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_service = MessageService(event.message.text)
    result = True
    if (message_service.message_includes_worktime() and message_service.is_valid_worktime()):

        work_time_repository = WorkTimeRepository(
            event.source.userId,
            message_service.start_time,
            message_service.end_time
            )

        result = work_time_repository.update_worktime()

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message_service.reply(result))
    )


if __name__ == "__main__":
    app.run()
