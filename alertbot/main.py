"""
Provide implementation of `alertbot` Telegram bot.
"""
import logging
import os

import telebot
from flask import Flask

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


if __name__ == '__main__':

    if os.environ.get('ENVIRONMENT') == 'production':
        server.run(host='192.168.0.1', port=int(os.environ.get('PORT', 8080)))

    if os.environ.get('ENVIRONMENT') == 'development':
        bot.poll()
