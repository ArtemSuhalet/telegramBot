from telebot.types import Message
from loader import bot
from database import data_history

@bot.message_handler(commands=['history'])
def bot_history(message: Message):
    data_history.show_history(message)