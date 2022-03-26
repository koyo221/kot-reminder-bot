import os
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
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
    message_service = MessageService('記事')
    return message_service.reply()


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_service = MessageService(event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message_service.reply())
    )


if __name__ == "__main__":
    app.run()
