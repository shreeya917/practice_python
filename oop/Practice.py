
class Car:
    __speed = None

    def __init__(self, speed=None):
        if speed is None:
            self.__speed = 20
        else:
            self.__speed = speed

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def accelerate(self):
        self.__speed = self.__speed + 10

    def brake(self):
        self.__speed = 0


car1 = Car()
print(car1.get_speed())
car1.accelerate()
print(car1.get_speed())
car1.brake()
print(car1.get_speed())

car1.set_speed(100)
print(car1.get_speed())
