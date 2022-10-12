from telebot.types import Message
from database.user_data import User
from database import data
from loader import bot
from datetime import datetime
from config_data.config import emoji

@bot.message_handler(commands=['lowprice'])
def bot_lowprice(message: Message):
    User.request_time, User.command = datetime.now().strftime("%d.%m.%Y %H:%M:%S"), message.text
    msg = bot.send_message(message.from_user.id, 'Введите город, где будет проводиться поиск. {}'.format(emoji['low']))
    bot.register_next_step_handler(msg, data.find_location)


