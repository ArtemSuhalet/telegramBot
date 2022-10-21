from telebot.types import Message
from config_data.config import emoji
from loader import bot


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.reply_to(message, f"_Привет_, {message.from_user.full_name}! {emoji['start']}\n"
                          f" Я - бот по поиску отелей\n"
                          f" Для получения информации о командах выберите /help в меню", parse_mode='Markdown')


