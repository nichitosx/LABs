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