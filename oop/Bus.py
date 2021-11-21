class Bus:
    __speed = None

    def __init__(self, speed=None):
        if speed is None:
            self.__speed = 40
        else:
            self.__speed = speed

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def accelerate(self):
        self.__speed = self.__speed + 30

    def brake(self):
        self.__speed = 0


bus1 = Bus()
print(bus1.get_speed())
bus1.accelerate()
print(bus1.get_speed())
bus1.brake()
print(bus1.get_speed())

bus1.set_speed(100)
print(bus1.get_speed())
