import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('5647023944:AAFycsOng1PsagKmGHWB4cDzruIkIcfb0es')#5647023944:AAFycsOng1PsagKmGHWB4cDzruIkIcfb0es

RAPID_API_KEY = os.getenv('RAPID_API_KEY')#Artem_suhalet23
DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку")
)
