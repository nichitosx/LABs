# Тема 2. Базовые операции языка Python
Отчет по Теме #2 выполнил:
- Толмачев Никита Романович
- ИНО ЗБ ПОАС-22-2

| Задание    | Сам_раб |
|------------| ------ |
| Задание 1  | + |
| Задание 2  | + |
| Задание 3  | + |
| Задание 4  | + |
| Задание 5  | + |
| Задание 6  | + |
| Задание 7  | + |
| Задание 8  | + |
| Задание 9  | + |
| Задание 10 | + |

Работу проверили:
- к.э.н., доцент Панов М.А.
- 
### Задание №1
- Текст задания

Выведите в консоль булевую переменную False, не используя слово False в строке или 
изначально присвоенную булевую переменную. Программа должна занимать не более двух 
строк редактора кода.
- Оформленный код

```python
result = not True
print(result)
```

- Скрины консоли
  ![img_2_1.png](https://github.com/nichitosx/LABs/blob/Lab2/pic/Lab2_1.png)

- Развернутый вывод

Этот код создает переменную под названием result, которая получает значение, которое является обратным для истины. То есть, когда мы берем истину (True) и делаем ее обратной, получается ложь (False). Затем программа выводит это значение (ложь) в консоль. Таким образом, на экране будет напечатано False.

### Задание №2
- Текст задания

Присвоить значения трем переменным и вывести их в консоль, используя только две строки
редактора кода

- Оформленный код

```python
a, b, c = 1, 2, 3; print(a, b, c)
```

- Скрины консоли
  ![img_2_2.png](https://github.com/nichitosx/LABs/blob/Lab2/pic/Lab2_2.png)

- Развернутый вывод

Этот код присваивает значения 1, 2 и 3 переменным a, b и c соответственно, и затем выводит их на консоль, используя функцию print() в одной строке.

### Задание №3
- Текст задания

Реализуйте ввод данных в программу, через консоль, в виде только целых чисел (тип данных int). То есть при вводе буквенных символов в консоль, программа не должна работать. Программа должна занимать не более двух строк редактора кода

- Оформленный код

```python
a, b, c = map(int, input().split())
print(a, b, c)
```

- Скрины консоли
  ![img_2_3.png](https://github.com/nichitosx/LABs/blob/Lab2/pic/Lab2_3.png)

- Развернутый вывод

Этот код считывает строку ввода с консоли, разделяет её на отдельные значения с помощью метода split(), затем преобразует каждое значение в целое число с помощью функции map(int, ...). Если введены не целые числа, возникнет исключение ValueError.

### Задание №4
- Текст задания

Создайте только одну строковую переменную. Длина строки должна не превышать 5 символов. На выходе мы должны получить строку длиной не менее 16 символов. Программа должна занимать не более двух строк редактора кода
- Оформленный код

```python
s = "РАЗ ДВА"
print(s * 2)
```

- Скрины консоли
  ![img_2_4.png](https://github.com/nichitosx/LABs/blob/Lab2/pic/Lab2_4.png)

- Развернутый вывод

Программа создает строковую переменную s со значением "РАЗ ДВА" и затем выводит это значение умноженное на 2, таким образом, строка будет повторена дважды.

### Задание №5
- Текст задания

Создайте три переменные: день (тип данных - числовой), месяц (тип данных - строка), год (тип данных - числовой) и выведите в консоль текущую дату в формате: “Сегодня день месяц год. Всего хорошего!” используя F строку и оператор end внутри print(), в котором вы должны написать фразу “Всего хорошего!”. Программа должна занимать не более двух строк редактора кода.

Оформленный код

```python
day, month, year = 30, "март", 2024
print(f"Сегодня {day} {month} {year}. ", end='')
print("Всего хорошего!")
```

- Скрины консоли
  ![img_2_5.png](https://github.com/nichitosx/LABs/blob/Lab2/pic/Lab2_5.png)

- Развернутый вывод

Этот код создает три переменные day, month и year для представления дня, месяца и года соответственно. Затем он выводит текущую дату и завершает вывод фразой "Всего хорошего!" без перехода на новую строку.

### Задание №6
- Текст задания

В предложении ‘Hello World’ вставьте ‘my’ между двумя словами. Выведите полученное предложение в консоль в одну строку. Программа должна занимать не более двух строк редактора кода.
Оформленный код

```python
print('Hello World'.replace(' ', ' my '))
```

- Скрины консоли
  ![img_2_6.png](https://github.com/xsadsenpai/py_practice/blob/lab2/pic/img_2_6.png)

- Развернутый вывод

Этот код заменяет пробел между словами на строку ' my ' и выводит результат в консоль.

### Задание №7
- Текст задания

Узнайте длину предложения ‘Hello World’, результат выведите в консоль. Программа должна занимать не более двух строк редактора кода.

Оформленный код

```python
print(len('Hello World'))
```

- Скрины консоли
  ![img_2_7.png](https://github.com/nichitosx/LABs/blob/Lab2/pic/Lab2_7.png)

- Развернутый вывод

Этот код вычисляет длину строки 'Hello World' и выводит результат в консоль.

### Задание №8
- Текст задания

Преобразовать предложение 'HELLO WORLD' в нижний регистр и вывести результат.

Оформленный код

```python
print('HELLO WORLD'.lower())
```

- Скрины консоли
  ![img_2_8.png](https://github.com/nichitosx/LABs/blob/Lab2/pic/Lab2_8.png)

- Развернутый вывод

Этот код преобразует строку 'HELLO WORLD' в нижний регистр и выводит результат в консоль.

### Задание №9
- Текст задания

Самостоятельно придумайте задачу по проходимой теме и решите ее. Задача должна быть cвязанна со взаимодействием с числовыми значениями.
#### Задача: 
Поиск максимального числа в списке.


Оформленный код

```python
numbers_input = input("Введите несколько чисел, разделенных пробелом: ")
numbers = list(map(float, numbers_input.split()))
max_number = max(numbers)
print(f"Максимальное число в списке {numbers} равно {max_number}")
```

- Скрины консоли
  ![img_2_9.png](https://github.com/nichitosx/LABs/blob/Lab2/pic/Lab2_9.png)

- Развернутый вывод

Эта программа запрашивает у пользователя несколько чисел, разделенных пробелом. Затем она разбивает введенную строку на список чисел, находит максимальное число с помощью функции max(), и выводит результат на экран.

### Задание №10
- Текст задания

Самостоятельно придумайте задачу по проходимой теме и решите ее. Задача должна быть cвязанна со взаимодействием со строковыми значениями
#### Задача: 
Скрипт запрашивает у пользователя набор символом, после просит указать символы, которые нужно заменить и на что.

Оформленный код

```python
s, old_word, new_word = input("Введите строку: "), input("Введите символы, которые нужно заменить: "), input("Введите символы, на которые нужно заменить: ")
print(f"Строка после замены: {s.replace(old_word, new_word)}")
```

- Скрины консоли
  ![img_2_10.png](https://github.com/nichitosx/LABs/blob/Lab2/pic/Lab2_10.png)

- Развернутый вывод

Этот код просит пользователя ввести строку, символы для замены и символы, на которые нужно заменить. Затем он использует метод .replace() для замены символов в строке и выводит результат.