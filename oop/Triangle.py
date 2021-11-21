# class Triangle:

#     def __init__(self, base, height, side):
#         self.base = base
#         self.height = height
#         self.side = side

#     def area(self):
#         area = self.base * self.height
#         return area

#     def perimeter(self):
#         perimeter = self.base + self.height + self.side
#         return perimeter

# triangle1 = Triangle(5 ,6,7)
# print(triangle1.area())
# print(triangle1.perimeter())

class Triangle:
    __base = None
    __height = None
    __side = None

    def __init__(self, base=None, height=None, side=None):
        if base and height and side is None:
            self.__base = 2
            self.__height = 3
            self.__side = 4

        else:
            self.__base = base
            self.__height = height
            self.__side = side

    def get_base(self):
        return self.__base

    def set_base(self, base):
        self.__base = base

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_side(self):
        return self.__side

    def set_side(self, side):
        self.__side = side

    def area(self):
        area = (self.__base * self.__height)
        return area

    def perimeter(self):
        perimeter = (self.__base + self.__height + self.__side)
        return perimeter


triangle1 = Triangle(base=3, height=4, side=5)
print(triangle1.get_base())
print(triangle1.get_height())
print(triangle1.get_side())
print()

print(triangle1.area())
print(triangle1.perimeter())


print()

triangle1.set_base(8)
print(triangle1.get_base())

triangle1.set_height(6)
print(triangle1.get_height())

triangle1.set_side(6)
print(triangle1.get_side())
