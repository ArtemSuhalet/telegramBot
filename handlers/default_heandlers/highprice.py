from telebot.types import Message

from loader import bot

@bot.message_handler(commands=['highprice'])
def bot_highprice(message: Message):
    msg = bot.bot.send_message(message.from_user.id, 'Введите город, где будет проводиться поиск.')
    bot.register_next_step_handler(msg, data.find_location)#функция по поиску отеля пока не создана