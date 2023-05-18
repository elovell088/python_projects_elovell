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