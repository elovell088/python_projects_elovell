#IT 414 - Eric Lovell - Test Validation Functions
import unittest
from functions.regex_assignment_functions import *

class TestFunctions(unittest.TestCase):
    """Tests for Validation functions in the regex_assignment_functions.py file"""

    ##--THESE TESTS SHOULD BE SUCCESSFUL--##
    def test_valid_cc(self):
        """Test for credit card numbers that should work"""
        valid_cc_to_test = ['4556799984114', '4929910992136630', '4485 417 07 4720', '453227 7709913001', '453 94514 76219 446', '4539 5821 3821 9893', '491697 216737 6396']

        for cc in valid_cc_to_test:
            self.assertTrue(validateCC(cc))

    
    def test_valid_coord(self):
        """Test for coordinate that should work"""
        valid_coord_to_test = ['72.42695, 164.36224', '-71.07059, 115.22109', '-82.14971, -176.53737', '13.439, 152.72812', '-81.41307, -27.6716']

        for coord in valid_coord_to_test:
            self.assertTrue(validateCoord(coord))


    def test_valid_dollar(self):
        """Test for dollar that should work"""
        valid_dollar_to_test = ['$1,000', '$2,345', '$1', '$12,345', '$678,910', '$999,999']

        for dollar in valid_dollar_to_test:
            self.assertTrue(validateDollar(dollar))


    ##--THESE TESTS SHOULD FAIL--##
    def test_invalid_cc(self):
        """Test for credit card number values that should fail"""
        invalid_cc_to_test = ['', ' ', '123456789101112131415']

        for cc in invalid_cc_to_test:
            self.assertFalse(validateCC(cc))


    def test_invalid_coord(self):
        """Test for coordinate values that should fail"""
        invalid_coord_to_test = ['', ' ', '1000', '2012', '$9,123', '1239877482', '2342342.1', '1.1', ')(*&%$^*)', 'coordinate']

        for coord in invalid_coord_to_test:
            self.assertFalse(validateCoord(coord))


    def test_invalid_dollar(self):
        """Test for dollar values that should fail"""
        invalid_dollar_to_test = ['', ' ', '1,000', '13231232133', '-123.09877', '$xx.xx', '$$10.99', '%(*&)', '2012']

        for dollar in invalid_dollar_to_test:
            self.assertFalse(validateDollar(dollar))
    
