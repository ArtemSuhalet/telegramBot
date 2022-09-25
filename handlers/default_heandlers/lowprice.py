from telebot.types import Message

from loader import bot

@bot.message_handler(commands=['lowprice'])
def bot_lowprice(message: Message):
    msg = bot.reply_to(message.from_user.id, 'Введите город, где будет проводиться поиск.')
    bot.register_next_step_handler(msg, data.find_location)#функция по поиску отеля пока не создана


