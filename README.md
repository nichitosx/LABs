# Тема 11. Итераторы и генераторы
Отчет по Теме #11 выполнил: 
- Толмачев Никита Романович
- ИНО ЗБ ПОАС-22-2

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + |


Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1

Вас никак не могут оставить числа Фибоначчи, очень уж они вас заинтересовали. Изучив новые возможности Python вы решили реализовать программу, которая считает числа Фибоначчи при помощи итераторов. Расчет начинается с чисел 1 и 1. Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов. Для реализации этой функции потребуется обратиться к инструкции yield (Она не сохраняет в оперативной памяти огромную последовательность, а дает возможность “доставать” промежуточные результаты по одному).

Результатом решения задачи будет листинг кода и вывод в консоль с числом Фибоначчи от 200.

```python
def fib():
    fib1, fib2 = 1, 1
    yield fib1
    yield fib2
    count = 2
    while count < 200:
        fib1, fib2 = fib2, fib1 + fib2
        count += 1
        yield fib2

fibonacci_generator = fib()

while True:
    current_fib = next(fibonacci_generator)
    if current_fib >= 200:
        print(current_fib, end=' ')
        break

for _ in range(19):
    current_fib = next(fibonacci_generator)
    print(current_fib, end=' ')
```

### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

Этот код создает генератор для последовательности чисел Фибоначчи и использует его для вывода 20 чисел, начиная с числа, которое больше или равно 200.

## Самостоятельная работа №2

К коду предыдущей задачи добавьте запоминание каждого числа Фибоначчи в файл “fib.txt”, при этом каждое число должно находиться на отдельной строчке. Результатом выполнения задачи будет листинг кода и скриншот получившегося файла

```python
def fib():
    fib1, fib2 = 1, 1
    yield fib1
    yield fib2
    count = 2
    while True:
        fib1, fib2 = fib2, fib1 + fib2
        count += 1
        yield fib2

fibonacci_generator = fib()

while True:
    current_fib = next(fibonacci_generator)
    if current_fib >= 200:
        print(current_fib, end=' ')
        break

with open("fib.txt", "w") as file:
    file.write(str(current_fib) + "\n")

for _ in range(19):
    current_fib = next(fibonacci_generator)
    print(current_fib, end=' ')
    with open("fib.txt", "a") as file:
        file.write(str(current_fib) + "\n")
```
### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

Этот код создает генератор для последовательности чисел Фибоначчи и записывает каждое число в файл "fib.txt" на отдельной строке. Затем он выводит 20 чисел, начиная с числа, которое больше или равно 200, и записывает их в этот файл.
