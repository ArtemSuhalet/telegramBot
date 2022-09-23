import requests
import json
from typing import Tuple, Dict
from telebot.types import Message
from loader import bot

@bot.message_handler(commands=['lowprice'])
def bot_lowprice(message: Message):
    bot.reply_to(message.from_user.id, 'Введите город, где будет проводится поиск.')

