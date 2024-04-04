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
