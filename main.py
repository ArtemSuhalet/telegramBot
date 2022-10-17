import config_data.config
from loader import bot
from utils.set_bot_commands import set_default_commands
import handlers
from database import data_history

if __name__ == '__main__':
    set_default_commands(bot)
    data_history.create_db()
    bot.infinity_polling()
