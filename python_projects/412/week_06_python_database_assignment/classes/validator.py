#IT 412 - Eric Lovell - Validation class for Week 6-7 Python Database Assignment

class Validator():
    """Class that validates input information"""

    def __init__(self):
        """Constructor for the validation class"""


    def validate_description(self, passed_description):
        """Method for validating user input for the make of a vehicle
        Arguments:
            passed_make {String Value} -- String value containing vehicle make information *Letters Only*
        Returns:
            True -- if validation passes | False -- if validation fails"""
        
        passed_description = passed_description.strip()
        has_bad_chars = False

        if passed_description:
            for char in passed_description:
                if char == "'" or char == '"':
                    has_bad_chars = True
                    break
            
            if has_bad_chars:
                return False
            else:
                return True
        else:
            return False
            
    
    def validate_make(self, passed_make):
        """Method for validating user input for the make of a vehicle
        Arguments:
            passed_make {String Value} -- String value containing vehicle make information *Letters Only*
        Returns:
            True -- if validation passes | False -- if validation fails"""
        
        passed_make = passed_make.strip()

        if passed_make:
            if passed_make.isalpha():
                return True
            
            else:
                return False
        
        else:
            return False

    
    def validate_model(self, passed_model):
        """Method for validating user input for the make of a vehicle
        Arguments:
            passed_model {String Value} -- String value containing vehicle model information *Letters, Numbers, some SpChar*
        Returns:
            True -- if validation passes | False -- if validation fails"""
        
        bad_characters = ['!', '"', '@', '#', '$', '%', '^', '*', '(', ')',
                          '=', '+', ',', '<', '>', '/', '?', ';', ':', '[',
                          ']', '{', '}', '~', '|', '.']
        
        passed_model = passed_model.strip()
        contains_bad_characters = False
        
        if passed_model:
            for char in passed_model:
                if char in bad_characters:
                    contains_bad_characters = True
                    break

            if contains_bad_characters:
                return False
            else:
                return True
                
        else:
            return False


    def validate_name(self, passed_name):
        """Method for validating user input for the name of the person that sold the vehicle
        Arguments:
            passed_name {String Value} -- String value containing name of person who sold the vehicle *Letters and Numbers Only*
        Returns:
            True -- if validation passes | False -- if validation fails"""
        
        characters_ok = [' ', ',', '.', '\'', '-', 'a', 'b', 'c', 'd', 'e', 'f',
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


    def validate_price(self, passed_price):
        """Method for validating user input for the make of a vehicle
        Arguments:
            passed_price {String Value} -- String value containing vehicle price information *Floats Only*
        Returns:
            True -- if validation passes | False -- if validation fails"""
        
        passed_price = passed_price.strip()

        if passed_price:
            try:
                int(passed_price)
                return False
            except:
                pass

            try:
                float(passed_price)
                return True
            except:
                return False
        

    def validate_vin(self, passed_vin):
        """Method for validating user input for the make of a vehicle
        Arguments:
            passed_vin {String Value} -- String value containing vehicle vin information *Letters and Numbers Only*
        Returns:
            True -- if validation passes | False -- if validation fails"""
        
        passed_vin = passed_vin.strip()

        if passed_vin:
            if passed_vin.isalnum():
                return True
            
            else:
                return False
        
        else:
            return False

    
