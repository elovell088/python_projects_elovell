from classes.pet import Pet

class Cat(Pet):
    """A simple class that represents a cat"""
    def __init__(self, name, age):
        """Initialize variables for cat"""
        super().__init__(name, age)