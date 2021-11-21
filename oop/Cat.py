class Cat:
    __catclass = None
    __lifespan = None

    def __init__(self,  catclass=None, lifespan=None):
        if catclass and lifespan is None:
            self.__catclass = "American Bobtail"
            self.__lifespan = "13-15 years"

        else:
            self.__catclass = catclass
            self.__lifespan = lifespan

    def get_catclass(self):
        return self.__catclass

    def set_catclass(self, catclass):
        self.__catclass = catclass

    def get_lifespan(self):
        return self.__lifespan

    def set_lifespan(self, lifespan):
        self.__lifespan = lifespan

    def displays(self):
        displays = ("Breed:%s \nLifespan:%s " %
                    (self.__catclass, self.__lifespan))
        return displays


cat = Cat("Burmese", "16 -18 years")

print(cat.displays())


print()


cat.set_catclass("German Rex")
print(cat.get_catclass())

cat.set_lifespan("9 -14 years")
print(cat.get_lifespan())
