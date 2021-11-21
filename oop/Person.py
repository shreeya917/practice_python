# class Person:

#     def __init__(self,  name, address, phoneno, occupation):

#         self.name = name
#         self.address = address
#         self.phoneno = phoneno
#         self.occupation = occupation

#     def display(self):
#         displays = ("Name:%s \nAddress:%s \nPhone Number:%s \nOccupation:%s" %
#                     (self.name, self.address, self.phoneno, self.occupation))
#         return displays


# person = Person("Ashmita", "Baneshwore", "9801258744", "Dentist")
# print(person.display())

class Person:
    __name = None
    __address = None
    __phoneno = None
    __occupation = None

    def __init__(self, name=None, address=None, phoneno=None, occupation=None):
        if name and address and phoneno and occupation is None:
            self.__name = "Swati"
            self.__address = "Dhumbarai"
            self.__phoneno = "9808126451"
            self.__occupation = "student"
        else:
            self.__name = name
            self.__address = address
            self.__phoneno = phoneno
            self.__occupation = occupation

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_phoneno(self):
        return self.__phoneno

    def set_phoneno(self, phoneno):
        self.__phoneno = phoneno

    def get_occupation(self):
        return self.__occupation

    def set_occupation(self, occupation):
        self.__occupation = occupation

    def displays(self):
        displays = ("Name:%s \nAddress:%s \nPhone Number:%s \nOccupation:%s" %
                    (self.__name, self.__address, self.__phoneno, self.__occupation))
        return displays


person = Person("Ashmita", "Baneshwore", "9801258744", "Dentist")
print(person.displays())


print()

person.set_name("Ishita")
print(person.get_name())

person.set_address("Tangal")
print(person.get_address())

person.set_phoneno("9841468546")
print(person.get_phoneno())

person.set_occupation("Sales Manager")
print(person.get_occupation())
