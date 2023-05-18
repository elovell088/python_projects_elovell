#IT 412 - Eric Lovell - Final Project Validator Class
import re

class Validator:
    """Class that holds methods to validate input"""

    def __init__(self):
        """Constructor for the Validator Class"""

    def validateCity(self, passed_city):
        """Method for validating user input for the city
        Arguments:
            passed_city {String Value} -- String value containing city portion of address information
        Returns:
                True -- if validation passes | False -- if validation fails"""
        
        characters_ok = [' ', "'", 'a', 'b', 'c', 'd', 'e', 'f',
                         'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
                         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        passed_city = passed_city.strip()
        passed_city = passed_city.lower()

        contains_bad_characters = False

        if passed_city:
            for char in passed_city:
                if char not in characters_ok:
                    contains_bad_characters = True
                    break    
        
            if contains_bad_characters:
                return False
            else:
                return True
        
        else:
            return False
    
        
        
    def validateCompanyName(self, passed_company):
        """Method for validating user input for the company name
        Arguments:
            passed_make {String Value} -- String value containing vehicle make information *Letters Only*
        Returns:
            True -- if validation passes | False -- if validation fails"""
            
        passed_company = passed_company.strip()
        has_bad_chars = False

        if passed_company:
            for char in passed_company:
                if char == "'" or char == '"':
                    has_bad_chars = True
                    break
                
            if has_bad_chars:
                return False
            else:
                return True
        else:
            return False
    
    
    def validateEmail(self, passed_email):
        """Method for validating user input for the email address
        Arguments:
            passed_email {String Value} -- String value containing email address information information
        Returns:
            True -- if validation passes | False -- if validation fails"""
        
        bad_characters = ['!', '"', "'", '#', '$', '%', '^', '&', '*', '(',
                          ')', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']',
                          '{', '}', '\\']
        
        passed_email = passed_email.strip()
        contains_bad_characters = False
        
        if passed_email:
            for char in passed_email:
                if char in bad_characters:
                    contains_bad_characters = True
                    break

            if contains_bad_characters:
                return False
            else:
                return True
                
        else:
            return False


    def validateName(self, passed_name):
        """Method for validating user input for the first and last name of the person that sold the vehicle
        Arguments:
            passed_name {String Value} -- String value containing name of person who sold the vehicle *Letters and Numbers Only*
        Returns:
            True -- if validation passes | False -- if validation fails"""
        
        characters_ok = [' ', "'", '-', 'a', 'b', 'c', 'd', 'e', 'f',
                         'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
                         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        passed_name = passed_name.strip()
        passed_name = passed_name.lower()

        contains_bad_characters = False

        if passed_name:
            for char in passed_name:
                if char not in characters_ok:
                    contains_bad_characters = True
                    break    
        
            if contains_bad_characters:
                return False
            else:
                return True
        
        else:
            return False
    
    
    def validatePhoneNumber(self, passed_phone):
        """Method for validating user input for the make of a vehicle
        Arguments:
            passed_model {String Value} -- String value containing street address information information
        Returns:
            True -- if validation passes | False -- if validation fails"""
        
        characters_ok = ['-', '1', '2', '3', '4', '5',
                         '6', '7', '8', '9', '0']
        
        passed_phone = passed_phone.strip()

        contains_bad_characters = False
        
        if passed_phone:
            for char in passed_phone:
                if char not in characters_ok:
                    contains_bad_characters = True
                    break    
        
            if contains_bad_characters:
                return False
            else:
                return True
        
        else:
            return False

    def validateState(self, passed_state):
        """Method for validating user input for the state
        Arguments:
            passed_state {String Value} -- String value containing state information information
        Returns:
            True -- if validation passes | False -- if validation fails"""
        
        passed_state = passed_state.strip()

        if passed_state:
            if passed_state.isalpha() and len(passed_state) == 2:
                return True
            else:
                return False
        else:
            return False


    def validateStreetAddress(self, passed_street):
        """Method for validating user input for the make of a vehicle
        Arguments:
            passed_model {String Value} -- String value containing street address information information
        Returns:
            True -- if validation passes | False -- if validation fails"""
        
        bad_characters = ['!', '"', "'", '@', '$', '%', '^', '&', '*',
                          '_', '=', '+', '<', '>', '?', ';', '[', ']',
                          '{', '}']
        
        passed_street = passed_street.strip()
        contains_bad_characters = False
        
        if passed_street:
            for char in passed_street:
                if char in bad_characters:
                    contains_bad_characters = True
                    break

            if contains_bad_characters:
                return False
            else:
                return True
                
        else:
            return False

    
    def validateZip(self, passed_zip):
            """Method for validating user input for the make of a vehicle
            Arguments:
                passed_make {String Value} -- String value containing vehicle make information *Letters Only*
            Returns:
                True -- if validation passes | False -- if validation fails"""
            
            passed_zip = passed_zip.strip()
            is_int = False

            if passed_zip:
                try:
                    int(passed_zip)
                    is_int = True
                except:
                    pass
                
                if is_int:
                    if len(passed_zip) == 4 or len(passed_zip) == 5:
                        return True
                    else:
                        return False
                else:
                    return False
            
            else:
                return False