class Bird:
    __birdclass = None
    __lifespan = None

    def __init__(self,  birdclass=None, lifespan=None):
        if birdclass and lifespan is None:
            self.__birdclass = "Mallard"
            self.__lifespan = "27 years"

        else:
            self.__birdclass = birdclass
            self.__lifespan = lifespan

    def get_birdclass(self):
        return self.__birdclass

    def set_birdclass(self, birdclass):
        self.__birdclass = birdclass

    def get_lifespan(self):
        return self.__lifespan

    def set_lifespan(self, lifespan):
        self.__lifespan = lifespan

    def displays(self):
        displays = ("Species:%s \nLifespan:%s " %
                    (self.__birdclass, self.__lifespan))
        return displays


bird = Bird("Elf Owl", " 5 years")

print(bird.displays())


print()


bird.set_birdclass("American Flamingo")
print(bird.get_birdclass())

bird.set_lifespan("49 years")
print(bird.get_lifespan())
