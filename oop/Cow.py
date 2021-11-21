class Cow:
    __cowclass = None
    __example = None

    def __init__(self,  cowclass=None, example=None):
        if cowclass and example is None:
            self.__cowclass = "Draught Breeds"
            self.__example = "Amritmahal, Siri"

        else:
            self.__cowclass = cowclass
            self.__example = example

    def get_cowclass(self):
        return self.__cowclass

    def set_cowclass(self, cowclass):
        self.__cowclass = cowclass

    def get_example(self):
        return self.__example

    def set_example(self, example):
        self.__example = example

    def displays(self):
        displays = ("Breed:%s \nLifespan:%s " %
                    (self.__cowclass, self.__example))
        return displays


cow = Cow("Dairy ", "Sahiwal, Red Sindhi, Holstein Friesian")

print(cow.displays())


print()


cow.set_cowclass("Dual purpose breeds")
print(cow.get_cowclass())

cow.set_example(" Haryana, Ongole, Kankrej")
print(cow.get_example())
