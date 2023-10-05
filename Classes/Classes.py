# Импорт библиотек
import time
import telebot
import threading
import logging

# Импорт файлов
from Classes.Dates import *

# Первый класс, отвечает за вечный опрос бота
class first_class:
    def __init__(self):
        # Токен для связи с ботом
        self.bot = telebot.TeleBot(botkey)
        # Логгирование в файл
        logging.basicConfig(level=logging.DEBUG, filename="loggerfirstclass.log", filemode="w",  format="%(asctime)s\t\t%(levelname)s\t%(filename)s\t%(message)s")

    def startprocessing(self):
        logging.debug("Инициализация класса для опроса бота прошла успешно")
        self.bot.polling(none_stop=True, interval=0)

# Второй класс, отвечает за генерацию и постинг комиксов в канал
class second_class:
    # Токен для связи с ботом
    bot = telebot.TeleBot(botkey)

    def __init__(self):
        # Логгирование в файл
        logging.basicConfig(level=logging.DEBUG, filename="loggersecondclass.log", filemode="w")

    def startprocessing(self):
        logging.debug("Инициализация класса для постинга комиксов прошла успешно")