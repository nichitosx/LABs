from datetime import datetime  # Импорт модуля datetime из стандартной библиотеки для работы с датой и временем
from math import sqrt  # Импорт функции sqrt из модуля math для вычисления квадратного корня
def main(**kwargs):  # Определение функции main с произвольным количеством именованных аргументов (**kwargs)
    for key in kwargs.items():  # Итерация по парам ключ-значение в словаре kwargs
        result = sqrt(key[1][0] ** 2 + key[1][
            1] ** 2)  # Расчет значения переменной result по формуле гипотенузы прямоугольного треугольника
        print(result)  # Вывод значения переменной result


if __name__ == '__main__':  # Проверка, является ли данный файл главным исполняемым файлом
    start_time = datetime.now()  # Получение текущего времени
    main(  # Вызов функции main с передачей аргументов
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )
    time_costs = datetime.now() - start_time  # Вычисление временных затрат на выполнение программы
    print(f"Время выполнения программы - {time_costs}")  # Вывод временных затрат на выполнение программы