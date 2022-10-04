from loader import bot
import handlers
from database import data_history
from utils.set_bot_commands import set_default_commands

if __name__ == '__main__':
    set_default_commands(bot)
    data_history.create_db()
    bot.infinity_polling()
