## Тема 8. Введение в ООП
Отчет по Теме #8 выполнил: 
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

Самостоятельно создайте класс и его объект. Они должны
отличаться, от тех, что указаны в теоретическом материале
(методичке) и лабораторных заданиях. Результатом выполнения
задания будет листинг кода и получившийся вывод консоли

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

my_car = Car("Toyota", "Camry")

my_car.accelerate(60)

print(f"Текущая скорость: {my_car.speed} км/ч")
```

### Результат.
![Меню](https://github.com/nichitosx/LABs/blob/Lab8/pic/Lab8_1.png)

## Выводы

Этот код представляет класс Car, который имеет атрибуты brand, model и speed. Конструктор __init__ инициализирует атрибуты brand и model значением, переданным при создании объекта, а атрибут speed устанавливается в 0 по умолчанию.

## Самостоятельная работа №2

Самостоятельно создайте атрибуты и методы для ранее созданного
класса. Они должны отличаться, от тех, что указаны в
теоретическом материале (методичке) и лабораторных заданиях.
Результатом выполнения задания будет листинг кода и
получившийся вывод консоли

```python
class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
    def accelerate(self, amount):
        self.speed += amount
    def change_color(self, new_color):
        self.color = new_color
    def get_age(self):
        current_year = 2024
        return current_year - self.year

my_car = Car("Toyota", "Camry", 2018, "black")

my_car.accelerate(60)

my_car.change_color("red")

age = my_car.get_age()

print(f"Марка: {my_car.brand}, Модель: {my_car.model}, Год выпуска: {my_car.year}, Цвет: {my_car.color}")
print(f"Текущая скорость: {my_car.speed} км/ч")
print(f"Возраст автомобиля: {age} года")
```

### Результат.
![Меню](https://github.com/nichitosx/LABs/blob/Lab8/pic/Lab8_2.png)

## Выводы

добавили атрибуты year и color для хранения года выпуска и цвета автомобиля. Также мы создали методы change_color, чтобы изменить цвет автомобиля, и get_age, чтобы получить его возраст.

## Самостоятельная работа №3

Самостоятельно реализуйте наследование, продолжая работать с
ранее созданным классом. Оно должно отличаться, от того, что
указано в теоретическом материале (методичке) и лабораторных
заданиях. Результатом выполнения задания будет листинг кода и
получившийся вывод консоли.

```python
from Lab8_2 import (Car)

class ElectricCar(Car):
    def __init__(self, brand, model, year, color, battery_capacity):
        super().__init__(brand, model, year, color)
        self.battery_capacity = battery_capacity
        self.battery_level = 100

    def charge_battery(self, amount):
        self.battery_level += amount
        if self.battery_level > 100:
            self.battery_level = 100

# Создаем объект класса ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 2020, "white", 75)

# Ускоряемся до 100 км/ч
my_electric_car.accelerate(100)

# Заряжаем батарею на 20%
my_electric_car.charge_battery(20)

# Выводим информацию о машине и уровне заряда батареи
print(f"Марка: {my_electric_car.brand}, Модель: {my_electric_car.model}, Год выпуска: {my_electric_car.year}, Цвет: {my_electric_car.color}")
print(f"Текущая скорость: {my_electric_car.speed} км/ч")
print(f"Уровень заряда батареи: {my_electric_car.battery_level}%")
```
### Результат.
![Меню](https://github.com/nichitosx/LABs/blob/Lab8/pic/Lab8_3.png)

## Выводы

Здесь ElectricCar является подклассом Car, и он добавляет новый атрибут battery_capacity и метод charge_battery, который позволяет заряжать батарею автомобиля.

## Самостоятельная работа №4

Самостоятельно реализуйте инкапсуляцию, продолжая работать с
ранее созданным классом. Она должна отличаться, от того, что
указана в теоретическом материале (методичке) и лабораторных
заданиях. Результатом выполнения задания будет листинг кода и
получившийся вывод консоли.

```python
class Car:
    def __init__(self, brand, model, year, color):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__color = color
        self.__speed = 0

    def accelerate(self, speed_delta):
        self.__speed += speed_delta

    def brake(self, speed_delta):
        self.__speed -= speed_delta
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):
        return self.__speed

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def get_brand(self):
        return self.__brand

my_car = Car("Toyota", "Corolla", 2015, "blue")

my_car.accelerate(50)

my_car.brake(20)

print("Текущая скорость:", my_car.get_speed())

print("Цвет машины:", my_car.get_color())

print("Марка машины:", my_car.get_brand())

```
### Результат.
![Меню](https://github.com/nichitosx/LABs/blob/Lab8/pic/Lab8_4.png)

## Выводы

Теперь атрибут __speed является приватным и не может быть изменен напрямую извне класса. Мы добавили методы get_speed и get_color для доступа к этим приватным атрибутам извне класса.

## Самостоятельная работа №5

Самостоятельно реализуйте полиморфизм. Он должен отличаться,
от того, что указан в теоретическом материале (методичке) и
лабораторных заданиях. Результатом выполнения задания будет
листинг кода и получившийся вывод консоли.

```python
class Car:
    def __init__(self, brand, model, year, color):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__color = color
        self.__speed = 0

    def accelerate(self, speed_delta):
        self.__speed += speed_delta

    def brake(self, speed_delta):
        self.__speed -= speed_delta
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):
        return self.__speed


class ElectricCar(Car):
    def accelerate(self, speed_delta):
        self._Car__speed += speed_delta * 2

    def brake(self, speed_delta):
        self._Car__speed -= speed_delta * 2
        if self._Car__speed < 0:
            self._Car__speed = 0


my_electric_car = ElectricCar("Tesla", "Model S", 2020, "white")

my_electric_car.accelerate(50)

my_electric_car.brake(20)

print("Текущая скорость электромобиля:", my_electric_car.get_speed())

```

### Результат.
![Меню](https://github.com/nichitosx/LABs/blob/Lab8/pic/Lab8_5.png)

## Выводы

В этом примере мы создали класс ElectricCar, который является подклассом класса Car. Мы переопределили методы accelerate и brake, чтобы они увеличивали и уменьшали скорость в два раза быстрее, чем у обычного автомобиля. Теперь мы можем создать объект этого класса и использовать его методы для управления скоростью электромобиля.