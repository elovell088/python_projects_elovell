import re

class Event():
    """Virtual representation for an event"""

    def __init__(self, name='', date='', time='', type=''):
        """Constructor for the Event Class"""

        self.name = name
        self.date = date
        self.time = time
        self.type = type


    def date_validator(self, passed_date):
        """Method that validates date attribute is number and '-' only
        Arguments:
            passed_date {String Value} -- String value that contains date information
        Return:
            True -- if date is in correct format | False -- if date is incorrect format"""

        passed_date = passed_date.strip()

        if passed_date:
            if re.match('(\d\d-\d\d-\d\d\d\d)', passed_date):
                return True
            
            else:
                return False

        else:
            False


    def get_date(self, passed_date):
        """Method that gathers and validates the event date
        Arguments:
            passed_date {String Value} -- String value consisting of date information
        Return:
            ret_date {String Value} -- String value that has been validated to be in correct format"""

        ret_date = passed_date.strip()
        date_validated = False

        while not date_validated:
            date_validated = self.date_validator(ret_date)

            if not date_validated:
                ret_date = input("Sorry, you entered an invalid character or format. Please try again: ")
                date_validated = self.date_validator(ret_date)
        
        return ret_date

    
    def get_name(self, passed_name):
        """Method that gathers and validates name information
        Arguments:
            passed_name {String Value} -- String value containing event name information
        Return:
            ret_name {String Value} -- String value that has been validated to be in proper format"""

        ret_name = passed_name.strip()
        name_validated = False

        while not name_validated:
            name_validated = self.name_validator(ret_name)

            if not name_validated:
                ret_name = input("Sorry, you entered an invalid character. Please try again: ")
                name_validated = self.name_validator(ret_name)
        
        return ret_name

    
    def get_time(self, passed_time):
        """Method that gathers and validates the event time
        Arguments:
            passed_time {String Value} -- String value containing event time information
        Return:
            ret_time {String Value} -- String value that has been validated to be in proper format"""

        ret_time = passed_time.strip()
        
        time_validated = False

        while not time_validated:
            time_validated = self.time_validator(ret_time)

            if not time_validated:
                ret_time = input("Sorry, you entered an invalid character or format. Please try again: ")
                time_validated = self.time_validator(ret_time)
                
        
        return ret_time

    
    def get_type(self, passed_type):
        """Method that gathers and validates the event type
        Arguments:
            passed_type {String Value} -- String value containing event type information
        Return:
            ret_type {String Value} -- String value that contains validated event type"""

        
        ret_type = passed_type.strip()
        ret_type = ret_type.lower()

        type_validated = False
        while not type_validated:
            type_validated = self.type_validator(ret_type)

            if not type_validated:
                ret_type = input("Sorry, you entered an invalid character. Please try again: ")
                type_validated = self.type_validator(ret_type)
        
        if ret_type == 's':
            ret_type = 'single occurrence'
        
        elif ret_type == 'r':
            ret_type = 'recurring'

        elif ret_type == 'f':
            ret_type = 'fixed number of meetings'
        
        return ret_type


    def name_validator(self, passed_name):
        """Method that validates event name value is letters only
        Arguments:
            passed_name {String Value} -- String value that contains event name information
        Return:
            True -- if name is in correct format | False -- if name is incorrect format"""

        passed_name = passed_name.strip()

        if passed_name:
            if passed_name.isalpha():
                return True
            
            else: 
                return False
        
        else:
            return False
    
    
    def time_validator(self, passed_time):
        """Method that validates time attribute is number and ':' only
        Arguments:
            passed_time {String Value} -- String value that contains time information
        Return:
            True -- if time is in correct format | False -- if time is incorrect format"""

        passed_time = passed_time.strip()

        if passed_time:
            if re.match('\d\d:\d\d', passed_time):
                return True
            
            else:
                return False


    def type_validator(self, passed_type):
        """Method that validates type attribute is s, r, or f.
        Arguments:
            passed_type {String Value} -- String value that contains type information
        Return:
            True -- if type is in correct character | False -- if type is incorrect character"""

        passed_type = passed_type.strip()
        passed_type = passed_type.lower()
        
        if passed_type:
            if passed_type == 'r':
                return True
            
            elif passed_type == 's':
                return True

            elif passed_type == 'f':
                return True

            else:
                return False


    

