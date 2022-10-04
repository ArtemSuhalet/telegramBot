from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config, host, user, password, db_name
from peewee import *
import pymysql


storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)

my_db = MySQLDatabase(
    database=db_name,
    user=user,
    password=password,
    host=host,
    port=3306
)