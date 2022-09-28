from telebot.types import Message

from loader import bot

@bot.message_handler(commands=['bestdeal'])
def bot_bestdeal(message: Message):
    msg = bot.send_message(message.from_user.id, 'Введите город, где будет проводиться поиск.')
    bot.register_next_step_handler(msg, data.find_location)#функция по поиску отеля пока не создана