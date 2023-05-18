#IT 412 - Eric Lovell - Week 1 - Problem 3

from classes.shirt import Shirt


#Create an instance of shirt class
my_shirt = Shirt("small", "red")
#Print each attribute of the class out individually
print("My shirt size is: " + my_shirt.size)
print("My shirt color is: " + my_shirt.color)
#Call method on the class that prints out the two attributes
my_shirt.shirt_details()
#Create a new instance of the shirt class
my_dads_shirt = Shirt("large", "grey")
#Print each attribute out individually
print("My Dad's shirt size is: " + my_dads_shirt.size)
print("My Dad's shirt color is: " + my_dads_shirt.color)
#Call method on the class that prints out attributes 
my_dads_shirt.shirt_details()