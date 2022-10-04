from telebot.types import Message
from database import data
from loader import bot


@bot.message_handler(commands=['history'])
def bot_history(message: Message):
    data_history.show_history(message)