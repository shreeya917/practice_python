# class Rectangle:

#     def __init__(self, length, height):
#         self.length = length
#         self.height = height

#     def area(self):
#         area = self.length * self.height
#         return area

#     def perimeter(self):
#         perimeter = 2 * (self.length + self.height)
#         return perimeter


# rectangle1 = Rectangle(4, 3)
# print(rectangle1.area())
# print(rectangle1.perimeter())
class Rectangle:
    __length = None
    __height = None

    def __init__(self, length= None, height=None):
        if length and height is None:
            self.__length = 2
            self.__height = 2
            
        else:
            self.__length = length
            self.__height = height
            
    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def area(self):
        area = (self.__length * self.__height)
        return area
    
        
    def perimeter(self):
        perimeter = ( 2 * (self.__length + self.__height))
        return perimeter
        

rectangle1 = Rectangle(length=3, height =4)
print(rectangle1.get_length())
print(rectangle1.get_height())
print()

print(rectangle1.area())
print(rectangle1.perimeter())


print()

rectangle1.set_length(8)
print(rectangle1.get_length())

rectangle1.set_height(6)
print(rectangle1.get_height())
