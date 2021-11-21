class Animal:
    __name = None
    __animalclass = None
    __lifespan = None

    def __init__(self, name=None, animalclass=None, lifespan=None):
        if name and animalclass and lifespan is None:
            self.__name = "Cat"
            self.__animalclass = "mammal"
            self.__lifespan = "2-16 years"

        else:
            self.__name = name
            self.__animalclass = animalclass
            self.__lifespan = lifespan

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_animalclass(self):
        return self.__animalclass

    def set_animalclass(self, animalclass):
        self.__animalclass = animalclass

    def get_lifespan(self):
        return self.__lifespan

    def set_lifespan(self, lifespan):
        self.__lifespan = lifespan

    def displays(self):
        displays = ("Name:%s \nClass:%s \nLifespan:%s " %
                    (self.__name, self.__animalclass, self.__lifespan))
        return displays


animal = Animal("Snake", "Reptiles", "9 years")
print(animal.displays())


print()

animal.set_name("Dog")
print(animal.get_name())

animal.set_animalclass("Mammals")
print(animal.get_animalclass())

animal.set_lifespan("10 -13 years")
print(animal.get_lifespan())
