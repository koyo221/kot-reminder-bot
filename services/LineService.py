import os

from linebot import LineBotApi, WebhookHandler


class LineService:
    line_bot_api = LineBotApi(os.environ.get('LINE_BOT_CHANNEL_ACCESS_TOKEN', ''))
    handler = WebhookHandler(os.environ.get('LINE_BOT_CHANNEL_SECRET', ''))

    def get_display_name(self, user_id):
        profile = LineService.line_bot_api.get_profile(user_id)
        return profile.display_name
