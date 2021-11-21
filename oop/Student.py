# class Student:

#     def __init__(self, id, name, roll, grade, address):
#         self.id = id
#         self.name = name
#         self.roll = roll
#         self.grade = grade
#         self.address = address

#     def display(self):
#         displays = ("ID:%d \nName:%s \nRoll no:%d \nGrade:%s \nAddress:%s" %
#                     (self.id, self.name, self.roll, self.grade, self.address))
#         return displays


# std = Student(1011, "Abhisek", 401, "10", "Maitidevi")
# print(std.display())

class Student:
    __id = None
    __name = None
    __roll = None
    __grade = None
    __address = None
    

    def __init__(self, id=None, name=None,roll= None,grade = None, address=None):
        if id and name and  roll and grade and address  is None:
            self.__id = 20
            self.__name = "hari"
            self.__roll = "25"
            self.__grade = "6"
            self.__address = "lazimpat"
            
        else:
            self.__id = id
            self.__name = name
            self.__roll = roll
            self.__grade = grade
            self.__address = address
            

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
    def get_roll(self):
        return self.__roll

    def set_roll(self, roll):
        self.__roll = roll

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def display(self):
        displays = ("ID:%d \nName:%s \nRoll no:%d \nGrade:%s \nAddress:%s" %
                    (self.__id, self.__name, self.__roll, self.__grade, self.__address))
        return displays
    

std = Student(1011, "Abhisek", 401, "10", "Maitidevi")
print(std.display())

print()
std.set_id(100)
print(std.get_id())

std.set_name("Akshara")
print(std.get_name())

std.set_roll("40")
print(std.get_roll())

std.set_grade("1")
print(std.get_grade())

std.set_address("Samakhushi")
print(std.get_address())

