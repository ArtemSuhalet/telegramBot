from telebot import types
import requests
import re
import json
from datetime import datetime
import telebot
from user_data import *


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
            return response.text
    except requests.exceptions.Timeout:
        return None


def find_location(message):
    """
    Функция для определения локации поиска.
    :param message:
    :return:
    """
