#Create new class, add type and message information

from classes.clothing import Clothing

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