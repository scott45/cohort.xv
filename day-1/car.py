__author__ = 'Scott Businge'


class Car(object):
    # Car class that instantiates various vehicle types

    # Attributes:
    # type: The type of vehicle as a string
    # model: The model of the car as a string
    # name: String representing the name of the car

    def __init__(self, name="General", model="GM", type="saloon"):
        self.type = type
        self.model = model
        self.name = name
        self.speed = 0

    @property
    def num_of_doors(self):
        if self.name == "Porshe" or self.name == "Koenigsegg":
            return 2
        return 4

    @property
    def num_of_wheels(self):
        if self.type != "trailer":
            return 4
        return 8

    def is_saloon(self):
        if self.type == "saloon":
            return True
        return False

    def drive(self, i):
        if (self.name == "Mercedes" or self.type == "saloon") and i == 3:
            self.speed = 1000
        elif (self.type == "trailer" or self.type == "trailer") and i == 7:
            self.speed = 77
        else:
            self.speed = 72  # Just making sure we change the speed as long as the car is being driven
        return self
