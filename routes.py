from flask import abort, request
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from app import app
from constants import *
from repositories.EmployeeCodeRepository import EmployeeCodeRepository
from repositories.WorkTimeRepository import WorkTimeRepository
from services.KingOfTimeService import KingOfTimeService
from services.LineService import LineService
from services.MatcherService import MatcherService
from services.MessageService import MessageService

#NOTE 処理をここにそのまま書くのってかなり変だけど、@handler.add周辺の処理が謎だしルートも実質1つなので一旦このままにする(Controllerクラスを作成するほどでもない)

line_bot_api = LineService.line_bot_api
handler = LineService.handler

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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input_text = event.message.text
    message_service = MessageService(input_text)
    matcher_service = MatcherService(input_text)

    reply = message_service.reply()

    #TODO かなりいまいちな処理, どうするのが適切かは謎
    # どこかでリプライの種類を保持するようにすればいいのかも

    # 労働時間登録
    work_time = matcher_service.is_valid_worktime()
    if type(work_time) is list:
        work_time_repo = WorkTimeRepository(event.source.user_id, work_time)

        try:
            work_time_repo.update_worktime()
        except:
            reply = ErrorConst['GENERAL_ERROR']

    # 従業員コード登録
    employee_code = matcher_service.is_employee_code()
    if employee_code:
        ec_service = EmployeeCodeRepository(event.source.user_id, employee_code)
        try:
            ec_service.register_ec()
        except:
            reply = ErrorConst['GENERAL_ERROR']

    # 打刻
    stamping = matcher_service.match(RequestConst)
    if stamping == 'REQUEST_STAMPING':
        try:
            kot_service = KingOfTimeService()
            response = kot_service.stamp(event.source.user_id)
            if response == 'NO_EMPLOYEE_KEY_ERROR':
                reply = ErrorConst['NO_EMPLOYEE_KEY_ERROR']
            if response == 'REQUEST_FAILED':
                reply = ErrorConst['STAMPING_ERROR']
            if response == 'ALREADY_STAMPED_ERROR':
                reply = ErrorConst['ALREADY_STAMPED_ERROR']
        except:
            reply = ErrorConst['STAMPING_ERROR']


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply)
    )


# for testing
@app.route("/hi")
def hello():
    return 'hi'
