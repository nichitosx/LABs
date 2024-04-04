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