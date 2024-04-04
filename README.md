# Тема 4. Функции и модули
Отчет по Теме #4 выполнил:
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
Дайте подробный комментарий для кода, написанного ниже.
Комментарий нужен для каждой строчки кода, нужно описать что она
делает. Не забудьте, что функции комментируются по-особенному.

Исходный код:
```python
from datetime import datetime
from math import sqrt

def main(**kwargs):
 for key in kwargs.items():
 	result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
 	print(result)
if __name__ == '__main__':
 start_time = datetime.now()
 main(
 	one=[10, 3],
 	two=[5, 4],
 	three=[15, 13],
 	four=[93, 53],
 	five=[133, 15]
 )
 time_costs = datetime.now() - start_time
 print(f"Время выполнения программы - {time_costs}")
```
Закоменченный код
```python
from datetime import datetime# Импорт модуля datetime из стандартной библиотеки для работы с датой и временем
from math import sqrt# Импорт функции sqrt из модуля math для вычисления квадратного корня

def main(**kwargs):# Определение функции main с произвольным количеством именованных аргументов (**kwargs)
    for key in kwargs.items():    # Итерация по парам ключ-значение в словаре kwargs
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)    # Расчет значения переменной result по формуле гипотенузы прямоугольного треугольника
        print(result)    # Вывод значения переменной result
if __name__ == '__main__':# Проверка, является ли данный файл главным исполняемым файлом
    start_time = datetime.now()    # Получение текущего времени
    main(    # Вызов функции main с передачей аргументов
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )
    time_costs = datetime.now() - start_time    # Вычисление временных затрат на выполнение программы
    print(f"Время выполнения программы - {time_costs}")  # Вывод временных затрат на выполнение программы
```
### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

Было выполненно комментирование каждой строки.

## Самостоятельная работа №2
Напишите программу, которая будет заменять игральную кость с 6
гранями. Если значение равно 5 или 6, то в консоль выводится «Вы
победили», если значения 3 или 4, то вы рекурсивно должны вызвать
эту же функцию, если значение 1 или 2, то в консоль выводится «Вы
проиграли». При этом каждый вызов функции необходимо выводить в
консоль значение “кубика”. Для выполнения задания необходимо
Михаил А. Панов
использовать стандартную библиотеку random. Программу нужно
написать, используя одну функцию и “точку входа” 

```python
import random

def roll_dice():
    dice_value = random.randint(1, 6)
    print("Выпало значение кубика:", dice_value)
    if dice_value >= 5:
        print("Вы победили!")
    elif dice_value >= 3:
        roll_dice()
    else:
        print("Вы проиграли!")
if __name__ == "__main__":
    roll_dice()
```
### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

Программа использует одну функцию для броска игрального кубика и анализа результатов. Рекурсивный вызов функции обрабатывает случай, когда выпадают значения от 3 до 4. Для генерации случайных чисел используется библиотека random.

## Самостоятельная работа №3
Напишите программу, которая будет выводить текущее время, с
точностью до секунд на протяжении 5 секунд. Программу нужно
написать с использованием цикла. Подсказка: необходимо
использовать модуль datetime и time, а также вам необходимо как-то
“усыплять” программу на 1 секунду.

```python
num = int(input("Введите число от 0 до 10: "))
if 0 <= num <= 10:
    if num <= 3:
        print("Полученное число находится в диапазоне от 0 до 3 включительно")
    elif num <= 6:
        print("Полученное число находится в диапазоне от 3 до 6")
    else:
        print("Полученное число находится в диапазоне от 6 до 10 включительно")
else:
    print("Введите число от 0 до 10 повторно")
```
### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

Этот код использует модули datetime и time. Он запускает цикл, который повторяется 5 раз, и на каждой итерации выводит текущее время с помощью datetime.datetime.now(). Затем программа ожидает 1 секунду перед следующей итерацией с помощью time.sleep(1).

## Самостоятельная работа №4
Напишите программу на Python, которая
принимает предложение (на английском) в качестве входных данных
от пользователя. Выполните следующие операции и отобразите
результаты:
• Выведите длину предложения.
• Переведите предложение в нижний регистр.
• Подсчитайте количество гласных (a, e, i, o, u) в предложении.
• Замените все слова "ugly" на "beauty".
• Проверьте, начинается ли предложение с "The" и заканчивается
ли на "end".
Проверьте работу программы минимум на 3 предложениях, чтобы
охватить проверку всех поставленных условий.

```python
def process_sentence(sentence):
    print("Длина предложения:", len(sentence))

    lowercase_sentence = sentence.lower()
    print("Предложение в нижнем регистре:", lowercase_sentence)

    vowels = 'aeiou'
    vowel_count = sum(1 for char in lowercase_sentence if char in vowels)
    print("Количество гласных:", vowel_count)

    replaced_sentence = lowercase_sentence.replace("ugly", "beauty")
    print("Предложение с заменой:", replaced_sentence)

    starts_with_the = lowercase_sentence.startswith("the")
    ends_with_end = lowercase_sentence.endswith("end.")
    print("Начинается с 'The':", starts_with_the)
    print("Заканчивается на 'end':", ends_with_end)


sentences = input("Введите предложение: ").split(',')

for sentence in sentences:
    print("Исходное предложение:", sentence)
    process_sentence(sentence)
```
### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

Программа использует методы строк для определения длины предложения, преобразования его в нижний регистр, подсчета количества гласных, замены определенных слов и проверки начала и конца предложения. Она также использует условные операторы для проверки различных условий в предложениях.

## Самостоятельная работа №5
Составьте программу, результатом которой будет данный вывод в консоль:

hello world

hello

hello world

hello

hello world

hello

hello world

hello

hello world

hello

hello world

hello

Программу нужно составить из данных фрагментов кода:

memory = ' world'

if values not in string:

while ' world' not in string:

string = string + ' world'

if counter in values:

counter = 10

string = 'hello'

string = memory

string = 'world'

counter = 0

if counter > 7:

print(string + memory)

print(string)

while counter !=10:

values = [0, 2, 4, 6, 8, 10]

memory = string

if counter < 10:

counter += 1

print(memory)

memory = string

Строки кода можно использовать только один раз. Необязательно использовать все строки кода.

```python
string = 'hello'
memory = ' world'
counter = 0

while counter != 6:
    print(string + memory)
    print(string)
    counter += 1
```
### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

. В каждой итерации цикла программа выводит комбинацию string и memory, а затем только string. Переменная counter используется для отслеживания количества итераций цикла и остановки выполнения после 6 итераций.
