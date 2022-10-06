from loader import bot
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from datetime import timedelta, date
from database import data
from database import user_data



def set_arrival_date(message):
    bot.send_message(message.from_user.id, "Введите дату заезда")
    calendar, step = DetailedTelegramCalendar(calendar_id=1,
                                              current_date=date.today(),
                                              min_date=date.today(),
                                              max_date=date.today() + timedelta(days=365),
                                              locale="ru").build()
    bot.send_message(message.chat.id,
                     f"Select {LSTEP[step]}",
                     reply_markup=calendar)


