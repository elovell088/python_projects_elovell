#IT 412 - Eric Lovell - Testing functions

import unittest
from functions.function_library import *

class DateTestCase(unittest.TestCase):
    """Tests for functions in the function_library.py file"""

    def test_valid_clean_output(self):
        """Here is a test that I think should work for the cleanOutput() function"""
        self.assertEqual(cleanOutput('6 ', ' 15', ' 2023 '), '6/15/2023')

    
    def test_valid_day(self):
        """Here is a test that I think should work for getDay() function"""
        valid_days_to_test = ['1', '04', ' 31', '29 ', ' 15', '0015 ']

        for day in valid_days_to_test:
            self.assertTrue(validate_day(day))


    def test_valid_month(self):
        """Here is a test that I think should work for getMonth() function"""
        valid_months_to_test = ['1', '01', ' 3', '12 ', '  11', '0011']

        for month in valid_months_to_test:
            self.assertTrue(validate_month(month))


    def test_valid_year(self):
        """Here is a test that I think should work for getYear() function"""
        valid_years_to_test = ['1991', ' 2000', '2030 ', ' 1723 ', '1111', '1010 ']

        for year in valid_years_to_test:
            self.assertTrue(validate_year(year))
    

    def test_invalid_day(self):
        """Here is a test that has a bunch of values that should NOT work for getDay() function"""
        invalid_days_to_test = ['Monday', '32', 'Day 02', '#15', ' ', '9 \'', '4.55']

        for day in invalid_days_to_test:
            self.assertFalse(validate_day(day))


    def test_invalid_month(self):
        """Here is a test that has a bunch of values that should NOT work for getMonth() function"""
        invalid_months_to_test = ['September', '46', '13', '%12', '##', ' ', 'month04', '10.5']

        for month in invalid_months_to_test:
            self.assertFalse(validate_month(month))
    
    
    def test_invalid_year(self):
        """Here is a test that has a bunch of values that should NOT work for getYear() function"""
        invalid_years_to_test = ['two thousand', '12345o', ' Eric 9090', 'Eric# ', '   ', '^', 'Eric', '2023.9']

        for year in invalid_years_to_test:
            self.assertFalse(validate_year(year))

