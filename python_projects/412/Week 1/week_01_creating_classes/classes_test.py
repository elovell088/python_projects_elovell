
from classes.dog import Dog
from classes.cat import Cat

my_dog = Dog("Jimmy", 3, "Golden Retriever")
my_cat = Cat("Benny", 5)
print("My dog's name is: " + my_dog.name)
print("My cat's name is: " + my_cat.name)

my_dog.takeToVet()
my_dog.clean()
print("My dog's breed is: " + my_dog.breed)