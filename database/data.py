from telebot import types
import requests
import re
import json
from datetime import datetime
import telebot
from database import user_data
from loader import bot
import schedule


def delete_spans(data: str) -> str:
    """
    Функция, удаляющая спецсимволы HTML.
    :param data: строка, содержащая теги HTML
    :return: строка без HTML тегов
    """
    result = re.compile(r'<.*?>')
    return result.sub('', data)

def modify_number(number: str) -> int or float:
    """
    Функция принимает число с типом данных str и заменяет символ запятой на точку.
    :param number: целочисленное или вещественное число с запятой
    :return: целочисленное или вещественное число в соответствии с правилами  Python
    """
    pass

def is_number_float(line: str) -> bool:
    """
    Функция проверяет, является ли число float.
    :param line: строка
    :return: True or False
    """
    pass

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
        if result:
            caption_dict_with_destination_id = dict()
            for i_elem in result:
                if "<" in i_elem.get("caption"):#удаление htmlткгов и спанов типа 'caption': "Нью-Йорк, Нью-Йорк, США (<span class='highlighted'>New</span> <span class='highlighted'>York</span> City)",
                    cap = delete_spans(i_elem.get("caption"))
                    if (user.city.title() in cap) or (user.city.lower() in cap):
                        caption_dict_with_destination_id[cap] = i_elem.get("destinationId")

            for elem in caption_dict_with_destination_id:
                markup.add(types.InlineKeyboardButton(elem, callback_data=caption_dict_with_destination_id[elem]))

            bot.send_message(message.chat.id, "Выберите локацию", reply_markup=markup)
        else:
            return bot.send_message(message.chat.id, "По Вашему запросу ничего не найдено.\n"
                                                     "Пожалуйста, проверьте, правильно ли указан город.")

    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        user.destination_id = call.data
        msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    text="Введите кол-во отелей (максимум - 10):",
                                    reply_markup=None)

        bot.register_next_step_handler(msg, set_hotels_number)

def set_hotels_number(message: telebot.types.Message) -> telebot.types.Message or None:
    """
    Сеттер для кол-ва выводимых отелей.
    Проверяет, правильно ли пользователь ввел кол-во отелей для вывода.
    Значение выводимых отелей должно быть числом и не должно превышаь 10.
    :param message:
    :return:
    """
    user = User.get_user(message.from_user.id)

    if message.text.isdigit():
        if int(message.text) > 10:
            return bot.send_message(message.chat.id, "Вы ввели значение, превышающее 10.\nПопробуйте снова.")

        user.hotels_number_to_show = int(message.text)
        if user.command == "/lowprice" or user.command == "/highprice":
            return schedule.set_arrival_date(message)
        msg = bot.send_message(message.chat.id, "Введите диапазон цен (пример ввода: 1000-5000):")
        return bot.register_next_step_handler(msg, set_price_range)

    bot.send_message(message.chat.id, "Ошибка ввода. Необходимо ввести число от 1 до 25.")


def set_price_range(message: telebot.types.Message) -> None:
    """
    Сеттер для диапазона цен.
    Проверяет, правилньо ли пользователь ввел диапазон цен в соответствии с примером.
    :param message:
    :return:
    """
    user = User.get_user(message.from_user.id)
    price_range = message.text.split("-")
    if len(price_range) == 2:
        if price_range[0].isdigit() and price_range[1].isdigit():
            if int(price_range[0]) < int(price_range[1]):
                price_min, price_max = int(price_range[0]), int(price_range[1])
            else:
                price_min, price_max = int(price_range[1]), int(price_range[0])
            user.min_price, user.max_price = price_min, price_max#запись в user
            msg = bot.send_message(message.chat.id, "Введите удаленность от центра в км:")

            bot.register_next_step_handler(msg, set_distance_from_center)

    else:
        bot.send_message(message.chat.id, "Ошибка ввода. Попробуйте снова.")


def set_distance_from_center(message: types.Message):
    """
    Сеттер для расстояния от центра.
    Проверяет, правильно ли пользователь ввел данные.
    :param message:
    :return:
    """
    user = User.get_user(message.from_user.id)
    if message.text.isdigit() or is_number_float.(str(modify_number(message.text))):
        user.distance_from_center = message.text + " км"
        return calendars.set_arrival_date(message)

