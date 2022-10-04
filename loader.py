import pymysql
from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config
from peewee import *



storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)

my_db = pymysql.connect(database=db_name, user=user, password=password, host=host, port=3306)