'''первоначальный бот
    вообще попробуем что из этого выйдет


'''

import telebot
from utils.bot_utils import get_token

TOKEN_DIR='gitignore_data\\token'


this_bot=telebot.TeleBot(get_token('gitignore_data\\token'))