from telebot.types import Message
from config_data.config import emoji
from loader import bot


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@bot.message_handler(state=None)
def bot_echo(message: Message):
    bot.reply_to(message, f"Не совсем вас понял. {emoji['echo']} Воспользуйтесь командой - Help.\nСообщение:"
                          f"{message.text}")
