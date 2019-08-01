#SDK software development kit
#web app
#架設伺服器 (寫網站) 通常用 flask django(通常用來做網頁)

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('bzusChGUsJ801lBM++2U66tmCtfmRmI4EziQ4Rw1ECOQ0dnMKxX1jHRbeTMQnYMG5asGKwZDr57sHhf4rquavGNykThzo3gBJHhc9pR8AWkHBbeWxRNaavdb0e1Ev2/gG5yvNksCqXsL+u5TAz7wBAdB04t89/1O/w1cDnyilFU=')
#access token : 存取 權杖
handler = WebhookHandler('af846d292fd7c81f58756b02fcc1a3ad')


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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()