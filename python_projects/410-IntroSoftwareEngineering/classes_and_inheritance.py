#IT 410 - Eric Lovell - Classes and Inheritance lecture assignment#

#Class example with pet as the super and classes Dog and Cat inheriting from it
class Pet():
    """A simple class for representing a pet"""

    def __init__(self, name, age):
        """Initialize name and age variables"""
        self.name = name
        self.age = age

    def clean(self):
        """Represents act of cleaning the pet"""
        print(self.name + " is clean!")

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

class Cat(Pet):
    """A simple class that represents a cat"""
    def __init__(self, name, age):
        """Initialize variables for cat"""
        super().__init__(name, age)


#Instatiate instance of class example
my_dog = Dog("Jimmy", 3, "Golden Retriever")
my_cat = Cat("Benny", 5)
print("My dog's name is: " + my_dog.name)
print("My cat's name is: " + my_cat.name)

my_dog.takeToVet()
my_dog.clean()
print("My dog's breed is: " + my_dog.breed)