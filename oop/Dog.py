class Dog:
    __dogclass = None
    __lifespan = None

    def __init__(self,  dogclass=None, lifespan=None):
        if dogclass and lifespan is None:
            self.__dogclass = "Labrador Retriever"
            self.__lifespan = " 11 years"

        else:
            self.__dogclass = dogclass
            self.__lifespan = lifespan

    def get_dogclass(self):
        return self.__dogclass

    def set_dogclass(self, dogclass):
        self.__dogclass = dogclass

    def get_lifespan(self):
        return self.__lifespan

    def set_lifespan(self, lifespan):
        self.__lifespan = lifespan

    def displays(self):
        displays = ("Breed:%s \nLifespan:%s " %
                    (self.__dogclass, self.__lifespan))
        return displays


dog = Dog("German Shepherd", " 11 years")

print(dog.displays())


print()


dog.set_dogclass("Golden Retriever")
print(dog.get_dogclass())

dog.set_lifespan("11 years")
print(dog.get_lifespan())
