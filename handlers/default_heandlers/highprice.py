from telebot.types import Message
from database import data
from loader import bot
from datetime import datetime



@bot.message_handler(commands=['highprice'])
def bot_highprice(message: Message):
    user.request_time, user.command = datetime.now().strftime("%d.%m.%Y %H:%M:%S"), message.text
    msg = bot.send_message(message.from_user.id, 'Введите город, где будет проводиться поиск.')
    bot.register_next_step_handler(msg, data.find_location)