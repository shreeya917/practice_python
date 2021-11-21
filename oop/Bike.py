class Bike:
    __speed = None

    def __init__(self, speed=None):
        if speed is None:
            self.__speed = 30
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


bike1 = Bike()
print(bike1.get_speed())
bike1.accelerate()
print(bike1.get_speed())
bike1.brake()
print(bike1.get_speed())

bike1.set_speed(100)
print(bike1.get_speed())
