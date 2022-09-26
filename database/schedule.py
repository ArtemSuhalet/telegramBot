from datetime import timedelta, date
import find_hotels



def set_arrival_date(message):
    bot.send_message(message.from_user.id, "Введите дату заезда")


