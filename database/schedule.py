from datetime import timedelta, date
from database import data



def set_arrival_date(message):
    bot.send_message(message.from_user.id, "Введите дату заезда")
    pass


