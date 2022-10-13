from telebot.types import Message
from database import data
from loader import bot
from datetime import datetime
from database.user_data import User
from config_data.config import emoji

@bot.message_handler(commands=['bestdeal'])
def bot_bestdeal(message: Message):
    User.request_time, User.command = datetime.now().strftime("%d.%m.%Y %H:%M:%S"), message.text
    msg = bot.send_message(message.from_user.id, '_Введите город, где будет проводиться поиск._ {}'.format(emoji['choose_city']), parse_mode='Markdown')
    bot.register_next_step_handler(msg, data.find_location)