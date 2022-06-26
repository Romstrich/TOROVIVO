'''первоначальный бот
    вообще попробуем что из этого выйдет


'''

import telebot
from utils.bot_utils import get_token

TOKEN_DIR='gitignore_data\\token'


this_bot=telebot.TeleBot(get_token('gitignore_data\\token'))

# Функция, обрабатывающая команду /start
@this_bot.message_handler(commands=["start"])
def start(m, res=False):
    this_bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
# Получение сообщений от юзера
@this_bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text=='time':
        this_bot.send_message(message.chat.id, 'Сейчас покажу время')
    else:
        print(message)
        this_bot.send_message(message.chat.id, 'Вы написали: ' + message.text)

@this_bot.message_handler(content_types=['photo'])
def handle_photo(message):
    print('Пришла фотка')
    print(f'вот такой месадж:\t----------->{message}')
    this_bot.send_message(message.chat.id,'Классная фотка!!!\tКинь ещё!')
# Запускаем бота
this_bot.polling(none_stop=True, interval=0)