class Pet():
    """A simple class for representing a pet"""

    def __init__(self, name, age):
        """Initialize name and age variables"""
        self.name = name
        self.age = age

    def clean(self):
        """Represents act of cleaning the pet"""
        print(self.name + " is clean!")