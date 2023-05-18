#IT 412 - Eric Lovell - Testing methods within the task class for Lecture Problem 2

import unittest
from classes.task import Task

class TestTaskClass(unittest.TestCase):
    """Test the pizza class"""

    def setUp(self):
        """Create an instance of the pizza class for testing all class functions"""

        self.my_task = Task("Image PC", "Task that involves downloading a new OS onto a PC", 20)


    def test_decrease_by_default(self):
        """Test decreasing the time value by the default of 1"""

        self.my_task.decrease_time()
        self.assertEqual(self.my_task.default_time, 19)
    
    def test_decrease_by_other(self):
        """Test decreasing the time value by using a value different than the default"""

        self.my_task.decrease_time(4.5)
        self.assertEqual(self.my_task.default_time, 15.5)


    def test_increase_by_default(self):
        """Test increasing the time value by the default of 1"""

        self.my_task.increase_time()
        self.assertEqual(self.my_task.default_time, 21)

    
    def test_increase_by_other(self):
        """Test increasing the time value by using a value different than the default"""

        self.my_task.increase_time(10.5)
        self.assertEqual(self.my_task.default_time, 30.5)
    

    def test_reset_time(self):
        """Test reset time method. Time value should change to 0"""

        self.my_task.reset_time()
        self.assertEqual(self.my_task.default_time, 0)
    