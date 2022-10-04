import sqlite3
from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config
from peewee import *



storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)

my_db = sqlite3.connect('bot.db')