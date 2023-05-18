from classes.pet_pydoc import Pet

class Dog(Pet):
    """A simple class for representing a dog"""

    def __init__(self, name, age, breed):
        """Initialize name and age variables"""
        super().__init__(name, age)
        self.breed = breed


    def placeDoginCarrier(self):
        """Represents placing the dog in a car carrier"""
        print(self.name + " is in the car carrier!")

    def takeToVet(self):
        """REpresents the act of taking the dog to the vet"""
        self.placeDoginCarrier()
        self.__visitVet()

    def __visitVet(self):
        """Represents the act of taking the dog to the vet"""
        print(self.name + " is on their way to the vet!")