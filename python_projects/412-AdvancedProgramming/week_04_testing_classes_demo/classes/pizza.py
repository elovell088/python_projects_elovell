#IT 412 - Eric Lovell - Pizza Class Testing Environment

class Pizza():
    """A virtual representation of a pizza"""

    def __init__(self, whofor):
        """Constructor for pizza class"""

        self.whofor = whofor
        self.toppings = []
        self.valid_toppings = ['pepperoni', 'mushrooms', 'green peppers', 'sausage', 'ham', 'bacon']

    
    def addTopping(self, topping):
        """Adds a topping to the pizza"""

        if self.toppingOK(topping):
            self.toppings.append(topping)
        else:
            print("You have asked to add an invalid topping. Please try again: ")
    

    def removeTopping(self, topping):
        """Removes a topping from the pizza"""

        if self.toppingOK(topping):
            self.toppings.remove(topping)
        else:
            print("You have asked to remove an invalid topping. Please try again: ")

    def toppingOK(self, topping):
        """Ensures that a given topping is one of the allowed toppings"""

        if topping in self.valid_toppings:
            return True
        
        else:
            return False