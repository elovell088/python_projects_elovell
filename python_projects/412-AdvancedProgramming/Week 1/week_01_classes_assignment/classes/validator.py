class Validator:
    """Class for validating user input"""
    def __init__(self):
        """Initialize class"""

    def validate_email(self, passed_string):
        """Validates user input for their email
        Arguments:
            passed_string {String Value} -- String value for persons email that will be validated for bad characters
        Returns:
            True -- if string contains bad characters   |   False -- if string does not contain bad characters"""

        bad_characters = ['#', '(', ')', ',', '/', '\\', '\'','!', '"', '$', '%', '^', '&', '*', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}' ]

        character_found = False
        for character in passed_string:
            if character in bad_characters:
                character_found = True
                return True

            if not passed_string or passed_string.isspace():
                character_found = True
                return True
            
            if character_found == False:
                return False

    
    def validate_id(self, person_type, passed_string):
        """Validates user input for their ID
        Arguments:
            passed_string {String Value} -- String value for persons ID that will be validated for letters and length 
        Returns:
            True -- if string contains bad characters   |   False -- if string does not contain bad characters"""

        if person_type == 'student':
            if passed_string.isdigit() and len(passed_string) <= 7:
                return True
            else: 
                return False
        
        else:
            if passed_string.isdigit() and len(passed_string) <= 5:
                return True
            else:
                return False


    def validate_name(self, passed_string):
        """Validates user input for their name
        Arguments:
            passed_string {String Value} -- String value for persons name that will be validated for bad characters
        Returns:
            True -- if string contains bad characters   |   False -- if string does not contain bad characters"""

        bad_characters = ['@', '#', '(', ')', '_', ',', '/', '\\','!', '"', '$', '%', '^', '&', '*', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}' ]

        character_found = False

        for character in passed_string:
            if character in bad_characters:
                character_found = True
                return True

            if not passed_string or passed_string.isspace():
                character_found = True
                return True
            
            if character_found == False:
                return False


    def validate_string(self, passed_string):
        """Validates string input for bad characters
        Arguments:
            passed_string {String Value} -- String value that will be validated for bad characters
        Returns:
            True -- if string contains bad characters   |   False -- if string does not contain bad characters"""

        bad_characters = ['@', '#', '(', ')', '_', ',', '/', '\\','!', '"', '$', '%', '^', '&', '*', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}' ]

        character_found = False

        for character in passed_string:
            if character in bad_characters:
                character_found = True
                return True
            if not passed_string or passed_string.isspace():
                character_found = True
                return True
            
            if character_found == False:
                return False