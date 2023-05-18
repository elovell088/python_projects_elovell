#IT 412 - Eric Lovell - Final Project Input Collection Class
from classes.validator import Validator

#Instance of Validator class
validate = Validator()

class Inputs():
    """Class that holds methods for collecting customer information"""

    def __init__(self):
        """Constructor for Inputs class"""
    
    def getCity(self):
        """Method that prompts the user for their City
        Arguments:
            None -- Input statements are within the method
        Returns:
            ret_city {String Value} -- String value containing validated city information"""
        
        ret_city = input("Please enter city: ")
        
        validate_city = False
        while not validate_city:
            validate_city = validate.validateCity(ret_city)

            if not validate_city:
                ret_city = input("Sorry, you entered an invalid character. Please try again: ")
                validate_city = validate.validateCity(ret_city)

        return ret_city


    def getCompanyName(self):
        """Method that prompts user for their first name
        Arguments: 
            None -- Input statements are within the method
        Returns:
            ret_companyname {String Value} -- String value containing validated name information"""
        
        user_decision = self.getOptionalQuestion("c")
        if user_decision:
            ret_companyname = input("Please enter company name: ")
            
            validate_companyname = False
            while not validate_companyname:
                validate_companyname = validate.validateCompanyName(ret_companyname)

                if not validate_companyname:
                    ret_companyname = input("Sorry, you entered an invalid character. Please try again: ")
                    validate_companyname = validate.validateCompanyName(ret_companyname)
        else:
            ret_companyname = None


        return ret_companyname
    

    def getEmail(self):
        """Method that prompts the user for their email address
        Arguments:
            None -- Input statements are within the method
        Returns:
            ret_email {String Value} -- String value containing validated email information"""

        user_decision = self.getOptionalQuestion("e")
        if user_decision:
            ret_email = input("Please enter email address: ")
            
            validate_email = False
            while not validate_email:
                validate_email = validate.validateEmail(ret_email)

                if not validate_email:
                    ret_email = input("Sorry, you entered an invalid character. Please try again: ")
                    validate_email = validate.validateEmail(ret_email)
        else:
            ret_email = None


        return ret_email


    def getFirstName(self):
        """Method that prompts user for their last name
        Arguments: 
            None -- Input statements are within the method
        Returns:
            ret_firstname {String Value} -- String value containing validated name information"""
        
        ret_firstname = input("Please enter first name: ")
        
        validate_firstname = False
        while not validate_firstname:
            validate_firstname = validate.validateName(ret_firstname)

            if not validate_firstname:
                ret_firstname = input("Sorry, you entered an invalid character. Please try again: ")
                validate_firstname = validate.validateName(ret_firstname)

        return ret_firstname
    

    def getLastName(self):
        """Method that prompts user for their full name
        Arguments: 
            None -- Input statements are within the method
        Returns:
            ret_lastname {String Value} -- String value containing validated name information"""
        
        ret_lastname = input("Please enter last name: ")
        
        validate_lastname = False
        while not validate_lastname:
            validate_lastname = validate.validateName(ret_lastname)

            if not validate_lastname:
                ret_lastname = input("Sorry, you entered an invalid character. Please try again: ")
                validate_lastname = validate.validateName(ret_lastname)

        return ret_lastname
    

    def getOptionalQuestion(self, passed_type):
        """Method that holds input statements for optional Customer class attributes
        Arguments:
            passed_type {String Value} -- String value holding questions for 'c' - company, 's' - secondary phone, 'e' - email address
        Reutns:
            None -- Asks the user a specified input statment based on passed_type"""
        
        if passed_type == "c":
            ask_user = input("(Optional) Would you like to add a company name? (Y/N): ")
            
        elif passed_type == "s":
            ask_user = input("(Optional) Would you like to add a second phone? (Y/N): ")
            
        elif passed_type == "e":
            ask_user = input("(Optional) Would you like to add an email? (Y/N): ")
        
            
        ask_user = ask_user.lower()
            
        if ask_user == 'y':
            return True
        elif ask_user == 'n':
            return False
        else:
            print("\nSorry, you entered an invalid character. Please try again..\n\n")


    def getPhoneNumber(self):
        """Method that prompts the user for their phone number
        Arguments:
            None -- Input statements are within the method
        Returns:
            ret_phone {String Value} -- String value containing validated phone information"""
        
        ret_phone = input("Please enter phone number: ")
        
        validate_phone = False
        while not validate_phone:
            validate_phone = validate.validatePhoneNumber(ret_phone)

            if not validate_phone:
                ret_phone = input("Sorry, you entered an invalid character. Please try again: ")
                validate_phone = validate.validatePhoneNumber(ret_phone)

        return ret_phone
    

    def getSecPhone(self):
        """Method that get the secondary pohone from the user if provided
        Arguments:
            None -- Asks user for information that method will work with
        Returns:
            ret_sec_phone {String Value} -- String value containint customers secondary phone number | None if nothing is provided"""
        
        user_decision = self.getOptionalQuestion("s")
        if user_decision:
            ret_sec_phone = self.getPhoneNumber()
        else:
            ret_sec_phone = None
        

        return ret_sec_phone


    def getState(self):
        """Method that prompts the user for their street address
        Arguments:
            None -- Input statements are within the method
        Returns:
            ret_state {String Value} -- String value containing validated state information"""
        
        ret_state = input("Please enter state: ")
        
        validate_state = False
        while not validate_state:
            validate_state = validate.validateState(ret_state)

            if not validate_state:
                ret_state = input("Sorry, you entered an invalid character or format. Please try again: ")
                validate_state = validate.validateState(ret_state)

        return ret_state


    def getStreetAddress(self):
        """Method that prompts the user for their street address
        Arguments:
            None -- Input statements are within the method
        Returns:
            ret_street_address {String Value} -- String value containing validated street address information"""
        
        ret_street_address = input("Please enter street address: ")
        
        validate_street = False
        while not validate_street:
            validate_street = validate.validateStreetAddress(ret_street_address)

            if not validate_street:
                ret_street_address = input("Sorry, you entered an invalid character. Please try again: ")
                validate_street = validate.validateStreetAddress(ret_street_address)

        return ret_street_address
    

    def getZip(self):
        """Method that prompts the user for their zip code
        Arguments:
            None -- Input statements are within the method
        Returns:
            ret_zip {String Value} -- String value containing validated zip information"""
        
        ret_zip = input("Please enter zip code: ")
        
        validate_zip = False
        while not validate_zip:
            validate_zip = validate.validateZip(ret_zip)

            if not validate_zip:
                ret_zip = input("Sorry, you entered an invalid character. Please try again: ")
                validate_zip = validate.validateZip(ret_zip)

        return ret_zip
    


    
