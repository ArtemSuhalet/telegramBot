from database import user_data
import telebot
from peewee import *


class BaseModel(Model):
    class Meta:
        database = my_db


class User_Data(BaseModel):
    user_telegram_id = IntegerField()
    user_command = CharField()
    user_time_request = CharField()
    user_hotels_list = CharField()


def create_db() -> None:
    """
    Функция создает базу данных, если она отсутствует.
    :return:
    """
    try:
        my_db.connect()
        User_Data.create_table()
    except InternalError as px:
        print(str(px))


def add_user_data(user_telegram_id, command, request_time, text_for_database) -> None:
    """
    Функция создает запись в базе данных.
    :param user_telegram_id:
    :param command:
    :param request_time:
    :param text_for_database:
    :return:
    """

    with my_db:
        User_Data.create(user_telegram_id=user_telegram_id,
                         user_command=command,
                         user_time_request=request_time,
                         user_hotels_list=text_for_database
                         )


