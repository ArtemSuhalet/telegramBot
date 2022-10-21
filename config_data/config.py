import os
from dotenv import load_dotenv, find_dotenv
import sqlite3
from loguru import logger
from peewee import *

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

RAPID_API_KEY = os.getenv('RAPID_API_KEY')
DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
    ('lowprice', 'Вывод самых дешёвых отелей в городе'),
    ('highprice', 'Вывод самых дорогих отелей в городе'),
    ('bestdeal', 'Вывод отелей, наиболее подходящих по цене и расположению от центра'),
    ('history', 'Вывод истории поиска отелей')
)

headers = {
        'X-RapidAPI-Key': 'e315c3fde3mshabab10a3881c217p1ae69ejsn04fc52c9199b',
        'X-RapidAPI-Host': 'hotels4.p.rapidapi.com'
    }


my_db = SqliteDatabase('bot.db')

emoji = {'start': '\U0001F603',
         'choose_city': '\U0001f30d',
         'history': '\U0001F4DD',
         'echo': '\U0001F926',
         'Да': '\U00002714',
         'Нет': '\U0000274C'
         }

logger.add('debug.log', format="{time} {level} {message}", level='DEBUG', rotation='500 KB', compression='zip', serialize=True)