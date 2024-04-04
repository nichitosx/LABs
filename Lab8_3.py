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

my_electric_car = ElectricCar("Tesla", "Model S", 2020, "white", 75)

my_electric_car.accelerate(100)

my_electric_car.charge_battery(20)

print(f"Марка: {my_electric_car.brand}, Модель: {my_electric_car.model}, Год выпуска: {my_electric_car.year}, Цвет: {my_electric_car.color}")
print(f"Текущая скорость: {my_electric_car.speed} км/ч")
print(f"Уровень заряда батареи: {my_electric_car.battery_level}%")