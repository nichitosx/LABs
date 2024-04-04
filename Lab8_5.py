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
