#IT 412 - Eric Lovell - Test Pizza Class Example

import unittest
from classes.pizza import Pizza

class TestPizzaClass(unittest.TestCase):
    """Test the pizza class"""

    def setUp(self):
        """Create an instance of the pizza class for testing all class functions"""

        self.my_pizza = Pizza("Eric's Pizza")

    
    def test_add_topping_success(self):
        """Test adding a valid topping to the pizza"""

        self.my_pizza.addTopping("mushrooms")
        self.assertIn("mushrooms", self.my_pizza.toppings)


    def test_add_topping_failure(self):
        """Test adding a topping that is invalid to the Pizza"""

        self.my_pizza.addTopping("steak")
        self.assertNotIn("steak", self.my_pizza.toppings)

    
    def test_remove_topping_success(self):
        """Test adding a valid topping to the pizza and removing it to ensure it is removed properly"""

        self.my_pizza.addTopping("mushrooms")
        self.assertIn("mushrooms", self.my_pizza.toppings)
        self.my_pizza.removeTopping("mushrooms")
        self.assertNotIn("mushrooms", self.my_pizza.toppings)
    
