# Тема 4. Базовые коллекции: множества, списки
Отчет по Теме #5 выполнил:
- Толмачев Никита Романович
- ИНО ЗБ ПОАС-22-2

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
Ресторан на предприятии ведет учет посещений за неделю при помощи
кода работника. У них есть список со всеми посещениями за неделю.
Ваша задача почитать:
• Сколько было выдано чеков
• Сколько разных людей посетило ресторан
• Какой работник посетил ресторан больше всех раз
Список выданных чеков за неделю:
[8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365,
 1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666,
 5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928,
 5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987,
 3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]
Результатом выполнения задачи будет: листинг кода, и вывод в
консоль, в котором будет указана вся необходимая информация

```python
check_list = [
    8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321,
    3365, 1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444,
    5556, 6666, 5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365,
    7502, 3016, 4928, 5837, 8201, 2643, 5017, 9682, 8530, 3250,
    7193, 9051, 4506, 1987, 3365, 5410, 7168, 7777, 9865, 5678,
    8201, 4445, 3016, 4506, 4506
]


num_of_checks = len(check_list)
unique_visitors = len(set(check_list))
most_frequent_visitor = max(set(check_list), key=check_list.count)

# Вывод результатов
print("Сколько было выдано чеков:", num_of_checks)
print("Сколько разных людей посетило ресторан:", unique_visitors)
print("Какой работник посетил ресторан больше всех раз:", most_frequent_visitor)
```

### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

Программа использует список для хранения чеков за неделю, функцию len() для подсчета количества чеков и уникальных посетителей, множество set() для определения уникальных посетителей и функцию max() для определения наиболее часто встречающегося посетителя.

## Самостоятельная работа №2
На физкультуре студенты сдавали бег, у преподавателя физкультуры
есть список всех результатов, ему нужно узнать
• Три лучшие результата
• Три худшие результата
• Все результаты начиная с 10
Ваша задача помочь ему в этом.
Список результатов бега:
[10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9,
27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
Результатом выполнения задачи будет: листинг кода, и вывод в
консоль, в котором будет указана вся необходимая информация

```python
    results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

best_results = sorted(results)[:3]

worst_results = sorted(results)[-3:]

results_from_10 = [result for result in results if result >= 10]

print("Три лучших результатов:", best_results)
print("Три худших результатов:", worst_results)
print("Все результаты начиная с 10:", results_from_10)
```
### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

Программа выводит три лучших и три худших результатов бега студентов, а также всех студентов, чьи результаты были 10 или выше.

## Самостоятельная работа №3
Напишите программу, которая будет выводить текущее время, с
точностью до секунд на протяжении 5 секунд. Программу нужно
написать с использованием цикла. Подсказка: необходимо
использовать модуль datetime и time, а также вам необходимо как-то
“усыплять” программу на 1 секунду.

```python

```
### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

Этот код использует модули datetime и time. Он запускает цикл, который повторяется 5 раз, и на каждой итерации выводит текущее время с помощью datetime.datetime.now(). Затем программа ожидает 1 секунду перед следующей итерацией с помощью time.sleep(1).

## Самостоятельная работа №4
Напишите программу, которая считает среднее арифметическое от
аргументов вызываемое функции, с условием того, что изначальное
количество этих аргументов неизвестно. Программу необходимо
реализовать используя одну функцию и “точку входа".

```python

```
### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

Функция average принимает переменное число аргументов args, считает их сумму с помощью sum(args) и делит её на количество переданных аргументов len(args). Если ни одного аргумента не было передано, функция возвращает 0.

## Самостоятельная работа №5
Создайте два Python файла, в одном будет выполняться вычисление
площади треугольника при помощи формулы Герона (необходимо
реализовать через функцию), а во втором будет происходить
взаимодействие с пользователем (получение всей необходимой
информации и вывод результатов). Напишите эту программу и
выведите в консоль полученную площадь

Первый файл
```python

```

Второй файл
```python

```

### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

При выполнении файла Lab4_5_2.py пользователь будет приглашен ввести длины сторон треугольника, а программа вычислит этого треугольника через функцию calculate_triangle_area и выведет площадь.