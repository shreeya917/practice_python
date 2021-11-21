class Square:
    __length = None

    def __init__(self, length =None):
        if length is None:
            self.__length = 2
        else:
            self.__length = length

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def area(self):
        self.__length = self.__length * self.__length

    def perimeter(self):
        self.__length = 4 * self.__length

square1 = Square()
print(square1.get_length())
square1.area()
print(square1.get_length())
square1.perimeter()
print(square1.get_length())

square1.set_length(5)
print(square1.get_length())