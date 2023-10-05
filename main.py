# Импорт библиотек

# Импорт файлов
from Classes.Classes import *

if __name__ == '__main__':
    # Инициализация класса для опроса бота
    x = first_class()
    thread1 = threading.Thread(target=x.startprocessing)
    thread1.start()

    # Инициализация класса для постинга комиксов в канал
    y = second_class()
    thread2 = threading.Thread(target=y.startprocessing)
    thread2.start()

