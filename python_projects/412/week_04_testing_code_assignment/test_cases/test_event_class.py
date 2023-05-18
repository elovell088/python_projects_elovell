#IT 412 - Eric Lovell - Test the Event Class

import unittest
from classes.event import Event

class TestEventClass(unittest.TestCase):
    """Test the event class"""

    def setUp(self):
        """Create an instance of the event class for testing all class functions"""

        self.test_event = Event()


    #--SUCCESSFUL TESTS--#
    def test_get_name_validator_success(self):
        """Test collecting a valid name from the user. These options should be successful"""

        valid_names_to_test = ['Event', 'event', 'EVENT', ' EvEnt', 'eVENT  ', ' NewEvent ']

        for name in valid_names_to_test:
            self.assertTrue(self.test_event.name_validator(name))

    def test_get_date_validator_success(self):
        """Test collecting a valid date from the user. These options should be successful"""

        valid_dates_to_test = ['09-04-1991', ' 10-23-2012', '06-30-1000 ', ' 11-11-1111 ']

        for date in valid_dates_to_test:
            self.assertTrue(self.test_event.date_validator(date))
    

    def test_get_time_validator_success(self):
        """Test collecting a valid time from the user. These options should be successful"""

        valid_times_to_test = ['12:00', ' 04:30', '05:30 ', ' 10:45 ']

        for time in valid_times_to_test:
            self.assertTrue(self.test_event.time_validator(time))

    
    def test_get_type_validator_success(self):
        """Test collecting a valid date from the user. These options should be successful"""

        valid_types_to_test = ['s', 'S ', ' s', ' s ', 'r', ' r', 'R ', ' r ', 'f', ' F', 'f ', ' f ']

        for type in valid_types_to_test:
            self.assertTrue(self.test_event.type_validator(type))
    


    #--FAILED TESTS--#
    def test_get_name_validator_failure(self):
        """Test collecting a valid name from the user. These options should fail"""

        invalid_names_to_test = ['Event12', 'event$$', 'EV^&*', '', ' ', '123', ' @#$', '5', '@']

        for name in invalid_names_to_test:
            self.assertFalse(self.test_event.name_validator(name))

    def test_get_date_validator_failure(self):
        """Test collecting a valid date from the user. These options should be fail"""

        invalid_dates_to_test = ['09-04', ' 10/21/1991', '06-30-1xxx ', '', ' ', '$$', 'TEst', '01-%*-2000']

        for date in invalid_dates_to_test:
            self.assertFalse(self.test_event.date_validator(date))
    

    def test_get_time_validator_failure(self):
        """Test collecting a valid time from the user. These options should be fail"""

        invalid_times_to_test = ['12:xx', ' 04:$', 'hi ', ' 09::30 ', '', ' ', '1030', '11-15']

        for time in invalid_times_to_test:
            self.assertFalse(self.test_event.time_validator(time))

    
    def test_get_type_validator_failure(self):
        """Test collecting a invalid type from the user. These options should be fail"""

        invalid_types_to_test = ['$', '1 ', ' x', ' testing ' 'single', ' s:', ' ', ' \n ', 'a a', '']

        for type in invalid_types_to_test:
            self.assertFalse(self.test_event.type_validator(type))
