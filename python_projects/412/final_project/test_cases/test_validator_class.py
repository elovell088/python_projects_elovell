#IT 412 - Eric Lovell - Test Cases for validator class - Week 6-7 Python Database Assignment

import unittest
from classes.validator import Validator

class TestEventClass(unittest.TestCase):
    """Test the event class"""

    def setUp(self):
        """Create an instance of the event class for testing all class functions"""

        self.test_validation = Validator()


    #--SUCCESSFUL TESTS--#
    def test_city_validator_success(self):
        """Test collecting a valid company name from the user. These options should be successful"""

        valid_cities_to_test = ["'Michigan'", ' New York', 'New Hampshire ', ' New Mexico ', "mi'", "'Michigan"]

        for city in valid_cities_to_test:
            self.assertTrue(self.test_validation.validateCity(city))


    def test_company_validator_success(self):
        """Test collecting a valid company name from the user. These options should be successful"""

        valid_names_to_test = ["It has a hemi", ' 4 doors', 'Kid vommited in back seat :( ', ' Broken Windshield! ', 'oil life at 80%', '  4 x 4 bed  ']

        for company in valid_names_to_test:
            self.assertTrue(self.test_validation.validateCompanyName(company))

    
    def test_email_validator_success(self):
        """Test collecting a valid email address from the user. These options should be successful"""

        valid_emails_to_test = ['eric_lovell0000@gmail.com', ' 12345@toaster.com', ' 67890@outlook.com', ' petz@walsh.com ', 'HIad102938@ccc.net']

        for email in valid_emails_to_test:
            self.assertTrue(self.test_validation.validateEmail(email))


    def test_name_validator_success(self):
        """Test collecting a valid name from the user. These options should be successful"""

        valid_names_to_test = ['Sarah Jones', ' sarah jones', 'SARAH JONES ', ' Josh ray-tims ',
                               'pete carter jr.', '  pete carter SR.', 'Rachel Jo-Ha, John Jo-Ha Jr.',
                               "Robert simoten's", " Eric's Automobiles", "San Peses' LLC", "cars inc.",
                               'abcde', 'fhijk', 'lmnop', 'qrstuv', 'wxyz']

        for name in valid_names_to_test:
            self.assertTrue(self.test_validation.validateName(name))


    def test_phone_validator_success(self):
        """Test collecting a valid phone number from the user. These options should be successful"""

        valid_phones_to_test = ["'412-987-1029'", ' 480-6200', '909-0876 ', ' 18-000-0987 ', '586-098-65453']

        for phone in valid_phones_to_test:
            self.assertTrue(self.test_validation.validatePhoneNumber(phone))

    
    def test_street_validator_success(self):
        """Test collecting a valid street address from the user. These options should be successful"""

        valid_streets_to_test = ['123 Tone street', ' 900 Brunswick apt# 5', ' 45000 apleton-square rd ', '1400 twelve & mack ', ' 400 West (apt#6) ']

        for street in valid_streets_to_test:
            self.assertTrue(self.test_validation.validateStreetAddress(street))
    

    def test_zip_validator_success(self):
        """Test collecting a valid zip code from the user. These options should be successful"""

        valid_zips_to_test = ["'4123'", ' 48062', '9090 ', ' 18028 ', "1111", "'98766", "6543"]

        for zip in valid_zips_to_test:
            self.assertTrue(self.test_validation.validateZip(zip))


    
            

    
    #--FAILED TEST--#
    def test_city_validator_failure(self):
        """Test collecting an invalid city name from the user. These options should be fail"""

        invalid_cities_to_test = ['', ' ', ' 123', '9!@# ', ' 7846*&^ ', '!!', '*&^%', '3.999999', '00()', '\\']

        for city in invalid_cities_to_test:
            self.assertFalse(self.test_validation.validateCity(city))


    def test_company_validator_failure(self):
        """Test collecting a valid company name from the user. These options should fail"""

        invalid_names_to_test = ["It's got a hemi", ' "4x4" Bed ', "Previous owner's kid threw up in it", " Broken tail light's! ", 'Nickname is "Old Bessy" ']

        for company in invalid_names_to_test:
            self.assertFalse(self.test_validation.validateCompanyName(company))


    def test_email_validator_failure(self):
        """Test collecting an invalid email address from the user. These options should fail"""

        invalid_emails_to_test = ['', ' ', ' !@#', 'elo$%^@&*.com ', ' ()<>@gmail.com', ' abc][}{ ', '*&^%', '3:00', 'tol@;.com', '\\']

        for email in invalid_emails_to_test:
            self.assertFalse(self.test_validation.validateEmail(email))


    def test_name_validator_failure(self):
        """Test collecting a valid name from the user. These options should fail"""

        invalid_names_to_test = ['', ' ', '123', ' 456', ' 789 ', '0!', 'WER*&^', '_)(^', 'Eric <>Lovell', 'Eric $%&', 'dr. #!@']

        for name in invalid_names_to_test:
            self.assertFalse(self.test_validation.validate_name(name))


    def test_phone_validator_failure(self):
        """Test collecting a invalid phone number from the user. These options should fail"""

        invalid_phones_to_test = ['', ' ', '123-123-!@#$', ' %^&-*(0-7654', ' ")}{-876-<>?; ', ' PHONE NUMBER ', ' abc-efg-hijk ', '+<>', '?[]', '"{456-098-7263}']

        for phone in invalid_phones_to_test:
            self.assertFalse(self.test_validation.validatePhoneNumber(phone))


    def test_street_validator_failure(self):
        """Test collecting a invalid street address from the user. These options should fail"""

        invalid_streets_to_test = ['', ' ', '123!', ' 900 Bar @ apt# 5', ' "456" $% ', '^twenny st ', ' &*_= ', '+<>', '?[]', '"{456 fairway}']

        for street in invalid_streets_to_test:
            self.assertFalse(self.test_validation.validateStreetAddress(street))

    
    def test_zip_validator_failure(self):
        """Test collecting an invalid zip code from the user. These options should be fail"""

        invalid_zips_to_test = ['', ' ', ' 123', '9!@# ', ' 7846*&^ ', '22', '333', '1', '*&^%', '5.6729999', '00()', '\\']

        for zip in invalid_zips_to_test:
            self.assertFalse(self.test_validation.validateZip(zip))

    