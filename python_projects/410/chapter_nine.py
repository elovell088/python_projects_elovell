#IT 410 - Eric Lovell - Chapter 9 Problems#

#Problem 9-1
class Shirt:
    """Class that represents a shirt"""
    def __init__(self, size, color):
        """Initialize class variables"""
        self.size = size
        self.color = color

    #Create method that prints the two attributes when called. 
    def shirt_details(self):
        """Prints out size and color of the shirt"""
        print("Shirt Details - Size: " + self.size + " | Color: " + self.color)

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



#Problem 9-2
class ShirtInventory:
    """Modified shirt class that represents a shirt along with the quantity"""
    def __init__(self, size, color):
        """Initialize class variables"""
        self.size = size
        self.color = color
        self.quantity = 1
    
    #Create method to decrease the quantity value
    def decrease_quantity(self, passed_number):
        """Decreases the quantity value for shirts"""
        self.quantity = self.quantity - passed_number

    #Create method to increase the quantity value
    def increase_quantity(self, passed_number):
        """Increases the quantity value for shirts"""
        self.quantity += passed_number
    
    #Create method that prints the two attributes when called. 
    def shirt_details(self):
        """Prints out size and color of the shirt"""
        print("Shirt Details - Size: " + self.size + " | Color: " + self.color)


#Create an instance of the new class
new_shirts = ShirtInventory("small", "blue")
#Call the increase method 3 times and print after calling the method
new_shirts.increase_quantity(1)
print("New shirt inventory: " + str(new_shirts.quantity))
new_shirts.increase_quantity(5)
print("New shirt inventory: " + str(new_shirts.quantity))
new_shirts.increase_quantity(10)
print("New shirt inventory: " + str(new_shirts.quantity))

#Call the decrease method 2 times and print after calling the method.
new_shirts.decrease_quantity(3)
print("New shirt inventory: " + str(new_shirts.quantity))
new_shirts.decrease_quantity(4)
print("New shirt inventory: " + str(new_shirts.quantity))



#Problem 9-3

#Rewrite shit class to be named clothing
class Clothing:
    """Modified shirt class that represents a shirt along with the quantity"""
    def __init__(self, size, color):
        """Initialize class variables"""
        self.size = size
        self.color = color
        self.quantity = 1
    
    #Create method to decrease the quantity value
    def decrease_quantity(self, passed_number):
        """Decreases the quantity value for shirts"""
        self.quantity = self.quantity - passed_number
    #Create method to increase the quantity value
    def increase_quantity(self, passed_number):
        """Increases the quantity value for shirts"""
        self.quantity += passed_number

    #Create method that prints the two attributes when called. 
    def shirt_details(self):
        """Prints out size and color of the shirt"""
        print("Clothing Details - Size: " + self.size + " | Color: " + self.color)
 
#Create new class, add type and message information
class ShirtInherit(Clothing):
    """Inherits clothing class and adds type information"""
    def __init__(self, size, color, type, message):
        """Initialize class variables"""
        super().__init__(size, color)
        self.type = type
        self.message = message
    #Method for message on shirt
    def print_message(self):
        """Prints our current message on the shirt"""
        print("Current message on the shirt: " + self.message)

#Create an instance and call the increase method
my_new_shirts = ShirtInherit("small", "light blue", "short sleeve", "this shirt rules.")
my_new_shirts.increase_quantity(100)
print("New shirt inventory: " + str(my_new_shirts.quantity))
#Call method print message on shirt
print("Shirt Message: " + my_new_shirts.message.title())



#Problem 9-4

#Using Java terminology, create a pants class that inherits from clothing class. Add fabric type and style attributes
class Pants(Clothing):
    """Representation of Pants, inherits from clothing class"""
    def __init__(self, size, color, fabric, style):
        super().__init__(size, color)
        self.fabric = fabric
        self.stlye = style
    



