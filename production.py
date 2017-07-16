#!/usr/bin/env python
import telegram
from flask import Flask, request
from telegram.ext import Updater
import os
# from app import app
from dotenv import load_dotenv
import os
from os.path import join, dirname

# app = Flask(__name__)

# global bot
# bot = None

# @app.route('/' + os.getenv('TOKEN', ''), methods=['GET', 'POST'])
# def webhook_handler():
#     if request.method == "POST":
#         update = telegram.Update.de_json(request.get_json(force=True))
#         chat_id = update.message.chat.id
#         text = update.message.text.encode('utf-8')
#         bot.sendMessage(chat_id=chat_id, text=text)
#     return 'ok!'

# # def set_webhook(token, port, appname):
# #     updater = Updater(token)
# #     updater.bot.set_webhook("https://{}.herokuapp.com/".format(appname) + token)
# #     updater.idle()

# def main(data_dict):
#     token = data_dict['token']
#     appname = data_dict['appname']
#     port = data_dict['port']
#     debug = data_dict['debug']
#     bot = telegram.Bot(token=token)
#     app.run(host='0.0.0.0', port=int(port), debug=debug)
    


# if __name__ == '__main__':
#     # Prepare data
#     dotenv_path = join(dirname(__file__), '.env.bleat')
#     load_dotenv(dotenv_path)

#     data = {
#         'token': os.getenv('TOKEN'),
#         'appname': os.getenv('APPNAME'),
#         'port': os.getenv('PORT'),
#         'debug': os.getenv('DEBUG')
#     }
#     main(data)


app = Flask(__name__)

@app.route("/landing", methods=['GET', 'POST'])
def landing():
    return 'ok'


if __name__ == '__main__':
    # Prepare data
    dotenv_path = join(dirname(__file__), '.env.bleat')
    load_dotenv(dotenv_path)

    port = int(os.getenv('PORT'))
    debug = os.getenv('DEBUG')

    app.run(host='0.0.0.0', port=port, debug=debug)
