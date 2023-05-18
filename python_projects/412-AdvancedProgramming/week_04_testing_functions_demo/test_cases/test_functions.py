#IT 412 - Eric Lovell - Testing functions

import unittest
from functions.function_library import *

class NamePartTestCase(unittest.TestCase):
    """Tests for functions in the function_library.py file"""

    def test_valid_name_part(self):
        """Here is a test that I think should work"""
        valid_names_to_test = ['Eric', 'eric', ' Eric', 'Eric ', ' eric', 'eric ']

        for name in valid_names_to_test:
            self.assertTrue(validate_name_part(name))
    

    def test_invalid_name_part(self):
        """Here is a test that has a bunch of values that should not work"""
        invalid_names_to_test = ['Eric\'', '12345', ' Eric 9090', 'Eric# ', '   ', '^', '****'] 

        for name in invalid_names_to_test:
            self.assertFalse(validate_name_part(name))