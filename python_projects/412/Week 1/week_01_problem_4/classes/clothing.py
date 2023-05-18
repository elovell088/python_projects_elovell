#Rewrite shirt class to be named clothing
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