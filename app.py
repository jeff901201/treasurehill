# ====== 載入LineBot所需要的套件 ======
# ====== 這裡是呼叫的py功能 ======
import os

from flask import Flask, abort, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from datetime import datetime

# ====== 這裡是呼叫的檔案內容 =====
# from Message_test1 import *
# from Message_test2 import *
# from Message_test3 import *
import basic_fun

from version.version import version

# ======== ChatBot開始 ==========
app = Flask(__name__)

# Channel Access Token(TOKEN)
line_bot_api = LineBotApi(
    ""
)
# Channel Secret
handler = WebhookHandler("")
# Your user ID
# line_bot_api.push_message('U550173d8899009fad32fa4dc184a2ada', TextSendMessage(text='恭喜成功第一步了！'))


# ======== 監聽所有來自 /callback 的 Post Request ==========
@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


# 訊息傳遞區塊
# ======== 基本上程式編輯都在這個function ========
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text

    basic_fun_paramater = basic_fun.create_point_and_keyword(message)
    if len(basic_fun_paramater) > 0:
        match basic_fun_paramater[-1]:
            case "Image_Messge":
                ReplyMessage = basic_fun.create_image_message(basic_fun_paramater[0], basic_fun_paramater[1])

            case "Image_Carousel_Template":
                image_carousel_template_message = basic_fun.create_image_carousel_template(
                    basic_fun_paramater[0], basic_fun_paramater[1]
                )
                if len(basic_fun_paramater) == 4:
                    confirm_template_message = basic_fun.create_confirm_template_message(
                        basic_fun_paramater[0], basic_fun_paramater[2]
                    )
                    ReplyMessage = [image_carousel_template_message, confirm_template_message]
                else:
                    ReplyMessage = image_carousel_template_message

            case "Text_Message":
                ReplyMessage = basic_fun.create_text_message(basic_fun_paramater[0], basic_fun_paramater[1])

            case "ImageMap_Message":
                ReplyMessage = basic_fun.create_imagemap_message(basic_fun_paramater[0], basic_fun_paramater[1])

            case _:
                ReplyMessage = TextSendMessage(text="功能未完成")

        line_bot_api.reply_message(event.reply_token, ReplyMessage)

    else:
        match message:
            # =========================================================================
            # others
            case "版本":
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=str(version())))

            case _:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))


# ======== 主程式 ==========
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
