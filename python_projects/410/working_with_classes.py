#IT 410 - Eric Lovell - Working with classes lecture assignment#

#Simple class example with public and private methods
class Dog():
    """A simple class for representing a dog"""

    def __init__(self, name, age):
        """Initialize name and age variables"""
        self.name = name
        self.age = age

    def clean(self):
        """Represents act of cleaning the dog"""
        print(self.name + " is clean!")

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


#Instatiate instance of class example
my_dog = Dog("Scout", 3)

print("My dog's name is: " + my_dog.name)

my_dog.takeToVet()