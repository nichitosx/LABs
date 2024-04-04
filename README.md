# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил: 
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

Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```python
def count_words(file_name):
    try:
        word_count = {}
        max_count_word = ""
        max_count = 0

        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.strip(",.!?")
                    if word:
                        word_count[word] = word_count.get(word, 0) + 1
                        if word_count[word] > max_count:
                            max_count = word_count[word]
                            max_count_word = word

        total_words = sum(word_count.values())
        unique_words = len(word_count)

        return total_words, unique_words, max_count_word, max_count
    except FileNotFoundError:
        print("Файл не найден.")
        return None
    except Exception as e:
        print("Произошла ошибка:", e)
        return None

file_name = "Статья.txt"

try:
    result = count_words(file_name)
    if result is not None:
        total_words, unique_words, most_common_word, max_count = result
        print("Самое часто встречающееся слово:", most_common_word)
        print("Количество его вхождений:", max_count)
except Exception as e:
    print("Произошла ошибка:", e)
```

### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

Программа подсчитывает количество слов в текстовом файле и выводит информацию о самом часто встречающемся слове и количестве его вхождений. Если файл не найден или происходит ошибка, программа выводит соответствующее сообщение.

## Самостоятельная работа №2

У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.


```python
def save_expenses(expenses, filename):
    with open(filename, 'w') as file:
        for category, amount in expenses.items():
            file.write(f"{category}: {amount}\n")

def load_expenses(filename):
    expenses = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                category, amount = line.strip().split(': ')
                expenses[category] = float(amount)
    except FileNotFoundError:
        print("Файл с данными не найден. Создан новый файл.")
    return expenses

def print_expenses(expenses):
    if not expenses:
        print("Нет информации о расходах.")
    else:
        print("Расходы:")
        for category, amount in expenses.items():
            print(f"{category}: {amount}")


def main():
    expenses_file = "rashod.txt"
    expenses = load_expenses(expenses_file)

    while True:
        print("\nМеню:")
        print("1. Ввести новый расход")
        print("2. Показать текущие расходы")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            category = input("Введите категорию расхода: ")
            amount = float(input("Введите сумму расхода: "))
            expenses[category] = amount
            save_expenses(expenses, expenses_file)
            print("Расход успешно добавлен.")
        elif choice == '2':
            print_expenses(expenses)
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие снова.")
if __name__ == "__main__":
    main()
```
### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

Функция save_expenses сохраняет расходы в файл. Она принимает словарь расходов и имя файла и записывает каждую категорию расходов и сумму в файл.

Функция load_expenses загружает расходы из файла. Она считывает категории и суммы расходов из файла и возвращает словарь.

Функция print_expenses выводит расходы на экран. Если расходы отсутствуют, она выводит сообщение об этом, иначе выводит каждую категорию и сумму расходов.

Функция main является основной частью программы. Она загружает расходы из файла, а затем предоставляет пользователю меню для ввода новых расходов, просмотра текущих расходов или выхода из программы.

## Самостоятельная работа №3

Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

• Текст в файле:

Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

• Ожидаемый результат:

Input file contains:

108 letters

20 words

4 lines

```python
with open('input.txt', 'r') as file:
    content = file.read()

num_letters = sum(1 for char in content if char.isalpha())
num_words = len(content.split())
num_lines = content.count('\n') + 1

print("Input file contains:")
print(num_letters, "letters")
print(num_words, "words")
print(num_lines, "lines")
```
### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

Этот код открывает файл 'input.txt' для чтения и считывает его содержимое. Затем он подсчитывает количество букв, слов и строк в файле. Результаты подсчета выводятся на экран.

## Самостоятельная работа №4

Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.

• Запрещенные слова:

hello email python the exam wor is

• Предложение для проверки:

Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!

• Ожидаемый результат:

*****, ***ld! ****** ** *** programming language of *** future. My ***** **.... ****** ** awesome!!!!

```python
def censor_sentence(sentence, forbidden_words):
    censored_sentence = sentence.lower()
    for word in forbidden_words:
        censored_sentence = censored_sentence.replace(word, '*' * len(word))
    return censored_sentence

def load_forbidden_words(file_name):
    try:
        with open(file_name, 'r') as file:
            forbidden_words = file.read().split()
            return forbidden_words
    except FileNotFoundError:
        print("Файл с запрещенными словами не найден.")
        return []

def main():
    forbidden_words_file = "input.txt"
    sentence = input("Введите предложение для проверки: ")

    forbidden_words = load_forbidden_words(forbidden_words_file)

    censored_sentence = censor_sentence(sentence, forbidden_words)
    print("Предложение с замененными запрещенными словами:")
    print(censored_sentence)

if __name__ == "__main__":
    main()
```
### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

Программа цензурирует предложение, заменяя запрещенные слова на звездочки. Для этого она использует функции censor_sentence, load_forbidden_words и main. Функция censor_sentence преобразует предложение в нижний регистр и заменяет запрещенные слова на звездочки. Функция load_forbidden_words загружает запрещенные слова из файла. Функция main является точкой входа в программу, она запрашивает предложение у пользователя, загружает запрещенные слова из файла и выводит цензурированное предложение.

## Самостоятельная работа №5

Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

Есть текстовый файл, содержащий данные о продажах товаров в магазине за определенный период времени. Каждая строка файла представляет собой запись о продаже одного товара и содержит информацию о его названии, цене и количестве проданных единиц
Нужно написать программу, которая считывает данные из этого файла и выполняет следующие действия:

Рассчитывает общую сумму продаж за весь период. 

Определяет товар с наибольшей и наименьшей выручкой.

Выводит список всех товаров, отсортированных по алфавиту.

```python
with open('Zadanie5.txt', 'r') as file:
    lines = file.readlines()

total_sales = 0
products = []

for line in lines:
    parts = line.split()
    product, price, quantity = parts[0], int(parts[1]), int(parts[2])
    total_sales += price * quantity
    products.append((product, price * quantity))

max_sales_product = max(products, key=lambda x: x[1])[0]
min_sales_product = min(products, key=lambda x: x[1])[0]

sorted_products = sorted(products, key=lambda x: x[0])

print("Общая сумма продаж:", total_sales)
print("Товар с наибольшей выручкой:", max_sales_product)
print("Товар с наименьшей выручкой:", min_sales_product)
print("Список всех товаров:")
for product, sales in sorted_products:
    print(product, "-", sales)
```

### Результат.
![Меню](https://github.com/vnika2003/Software_Engineering/blob/Тема_2/pic/Lab2_1.png)

## Выводы

Этот код сначала открывает файл 'input.txt' для чтения, затем читает его содержимое в переменную content. Затем мы подсчитываем количество букв, используя генератор списка, проверяя каждый символ на то, является ли он буквой латинского алфавита. Количество слов мы получаем, разделив содержимое файла на отдельные слова с помощью метода split(). Количество строк мы определяем, подсчитывая количество символов новой строки \n и добавляя 1, так как последняя строка может не завершаться символом новой строки.