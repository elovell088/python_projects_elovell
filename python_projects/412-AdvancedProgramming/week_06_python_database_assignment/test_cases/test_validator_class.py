#IT 412 - Eric Lovell - Test Cases for validator class - Week 6-7 Python Database Assignment

import unittest
from classes.validator import Validator

class TestEventClass(unittest.TestCase):
    """Test the event class"""

    def setUp(self):
        """Create an instance of the event class for testing all class functions"""

        self.test_validation = Validator()


    #--SUCCESSFUL TESTS--#
    def test_desc_validator_success(self):
        """Test collecting a valid description from the user. These options should be successful"""

        valid_desc_to_test = ["It has a hemi", ' 4 doors', 'Kid vommited in back seat :( ', ' Broken Windshield! ', 'oil life at 80%', '  4 x 4 bed  ']

        for desc in valid_desc_to_test:
            self.assertTrue(self.test_validation.validate_description(desc))


    def test_make_validator_success(self):
        """Test collecting a valid make from the user. These options should be successful"""

        valid_makes_to_test = ['Ford', ' fOrd', 'foRD ', ' DODGE ', 'dodge', '  dOdGE  ']

        for make in valid_makes_to_test:
            self.assertTrue(self.test_validation.validate_make(make))


    def test_model_validator_success(self):
        """Test collecting a valid model from the user. These options should be successful"""

        valid_models_to_test = ['F150', 'CR-V45', ' 45RT & 6t ', ' S8 Hybrid', 'RS49 Recharge ', 'gt extended cab', '  45x  ', '1500', 'XRT']

        for model in valid_models_to_test:
            self.assertTrue(self.test_validation.validate_model(model))
    

    def test_name_validator_success(self):
        """Test collecting a valid name from the user. These options should be successful"""

        valid_names_to_test = ['Sarah Jones', ' sarah jones', 'SARAH JONES ', ' Josh ray-tims ',
                               'pete carter jr.', '  pete carter SR.', 'Rachel Jo-Ha, John Jo-Ha Jr.',
                               "Robert simoten's", " Eric's Automobiles", "San Peses' LLC", "cars inc.",
                               'abcde', 'fhijk', 'lmnop', 'qrstuv', 'wxyz']

        for name in valid_names_to_test:
            self.assertTrue(self.test_validation.validate_name(name))

    
    def test_price_validator_success(self):
        """Test collecting a valid price from the user. These options should be successful"""

        valid_prices_to_test = ['1.00', ' 2.33', '5.44 ', ' 4000.99 ', '0.99', ' .36', '1.1']

        for price in valid_prices_to_test:
            self.assertTrue(self.test_validation.validate_price(price))
    

    def test_vin_validator_success(self):
        """Test collecting a valid vin from the user. These options should be successful"""

        valid_vins_to_test = ['ABC123', 'abc123', ' X1Y2Z3 ', ' QUI76ASII', ' Y78uuii ', 'exUU8I90oolPoi ', ' c9o7p3e4y6']

        for vin in valid_vins_to_test:
            self.assertTrue(self.test_validation.validate_vin(vin))
    


    #--FAILED TESTS--#
    def test_desc_validator_failure(self):
        """Test collecting a valid description from the user. These options should be successful"""

        invalid_desc_to_test = ["It's got a hemi", ' "4x4" Bed ', "Previous owner's kid threw up in it", " Broken tail light's! ", 'Nickname is "Old Bessy" ']

        for desc in invalid_desc_to_test:
            self.assertFalse(self.test_validation.validate_description(desc))


    def test_make_validator_failure(self):
        """Test collecting a valid make from the user. These options should fail"""

        invalid_makes_to_test = ['', ' ', 'f0rd', ' 999', 'd!dge ', ' 123ABC ', '', '  dOdG3  ', '!@#', '$$car']

        for make in invalid_makes_to_test:
            self.assertFalse(self.test_validation.validate_make(make))

    def test_model_validator_failure(self):
        """Test collecting a valid model from the user. These options should fail"""

        invalid_models_to_test = ['', ' ', '!@#', ' $%^', '^&* .', ' SRx-~() ', ' $$__?', '[]{}', '|@', '/;:', '<>']

        for model in invalid_models_to_test:
            self.assertFalse(self.test_validation.validate_model(model))
    

    def test_name_validator_failure(self):
        """Test collecting a valid name from the user. These options should be fail"""

        invalid_names_to_test = ['', ' ', '123', ' 456', ' 789 ', '0!', 'WER*&^', '_)(^', 'Eric <>Lovell', 'Eric $%&', 'dr. #!@']

        for name in invalid_names_to_test:
            self.assertFalse(self.test_validation.validate_name(name))

    
    def test_price_validator_failure(self):
        """Test collecting a valid price from the user. These options should be fail"""

        invalid_prices_to_test = ['', ' ', ' 1', '2 ', ' 3 ', '!!', '*&^%', 'twenty dollars', '4 pesos', '$40,000.00']

        for price in invalid_prices_to_test:
            self.assertFalse(self.test_validation.validate_price(price))
    

    def test_vin_validator_failure(self):
        """Test collecting a valid vin from the user. These options should fail"""

        invalid_vins_to_test = ['', ' ', ' !!!EEEE66', '** ', 'VIN number', ' 5000.00 ', 'xxx-001-ax4ds-0009', '11000 XXXX00']

        for vin in invalid_vins_to_test:
            self.assertFalse(self.test_validation.validate_vin(vin))