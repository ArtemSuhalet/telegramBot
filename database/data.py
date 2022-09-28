from telebot import types
import requests
import re
import json
from datetime import datetime
import telebot
#from user_data import *
from loader import bot

def calculate_price_for_night(date_1, date_2, price):
    """
    Функция считает стоимость проживания в отеле за ночь.
    :param date_1: дата заезда
    :param date_2: дата выезда
    :param price: стоимость проживания за весь период
    :return: стоимость проживания за ночь
    """

    d_1 = datetime.strptime(str(date_1), "%Y-%m-%d")
    d_2 = datetime.strptime(str(date_2), "%Y-%m-%d")
    date_delta = int((d_2 - d_1).days)
    return int(price) // date_delta

def request_to_api(url, headers, querystring):
    """
    Функция, производящая запрос к API.
    :param url: ссылка
    :param headers: headers
    :param querystring: parameters
    :return:
    """

    try:
        response = requests.request("GET", url,
                                    headers=headers,
                                    params=querystring,
                                    timeout=10)
        if response.status_code == requests.codes.ok:#проверка
            print(response.text)
            return response.text
    except requests.exceptions.Timeout:
        return None


def find_location(message):
    """
    Функция для определения локации поиска.
    :param message:
    :return:
    """
    user = User.get_user(message.from_user.id)# берем юзера из словаря
    user.city = message.text
    markup = types.InlineKeyboardMarkup()

    url_for_destination_id = "https://hotels4.p.rapidapi.com/locations/v2/search"

    querystring_for_destination_id = {"query": user.city,
                                      "locale": "ru_RU",
                                      "currency": "USD"
                                      }
    headers = {
        'X-RapidAPI-Key': 'e315c3fde3mshabab10a3881c217p1ae69ejsn04fc52c9199b',
        'X-RapidAPI-Host': 'hotels4.p.rapidapi.com'
    }

    response = request_to_api(url=url_for_destination_id,
                              headers=headers,
                              querystring=querystring_for_destination_id)

    if not response:
        bot.send_message(message.chat.id, "Произошла ошибка.\nПопробуйте снова.")
    else:

        result = json.loads(response)['suggestions'][0]['entities']


