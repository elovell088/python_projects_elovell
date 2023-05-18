def bad_character_check(passed_string, passed_type):
    """Checks if string has bad characters
    Arguments:
        passed_string {String value} -- String value to check bad characters against
        passed_type {String value} -- String value that signifies the type of characters to check for
    Returns:
        True - if bad characters are found in string | False - if no bad characters were found"""

    bad_characters = {'name' : ['@', '#', '(', ')', '_', ',', '/', '\\','!', '"', '$', '%', '^', '&', '*', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}' ],
                      'email' : ['#', '(', ')', ',', '/', '\\', '\'','!', '"', '$', '%', '^', '&', '*', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}' ],
                      'address' : ['@', '_', '\'','!', '"', '$', '%', '^', '&', '*', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}' ]}

    character_found = False
    for character in passed_string:
        if character in bad_characters[passed_type]:
            character_found = True
            break 
    if not passed_string or passed_string.isspace():
        character_found = True
    
    if character_found == True:
        return True
    else:
        return False


def validate_input(passed_string, passed_input_type):
    """Validate input based on id, name, email, and address
    Arguments:
        passed_string [String Value] -- Input from the user that is to be validated
        passed_input_type {string value} -- Enter input type to validate  'id' 'name' 'email' or 'address'
    Returns:
        True -- if the input is successfully validated | False -- if the input is invalid"""

    if passed_input_type == 'id':

        if passed_string.isdigit() and len(passed_string) <= 7:
            return True
        else:
            return False

    else:
        check_result = bad_character_check(passed_string, passed_input_type)
        if check_result == False and not passed_string.isdigit():
            return True
        else:
            return False
        

def gather_input(passed_input_type):
    """Gathers users input regarding their ID, Name, Email, and Address
    Arguments:
        passed_input_type [String Value] -- Enter input type to determine type of information to gather
    Returns:
        temp_variable [String Value] -- Returns validated string value based on ID, Name, Email, Address""" 

    if passed_input_type == 'id':
        temp_variable = input("Please enter your employee ID: ")
        validated = False
        while not validated:
            validation_result = validate_input(temp_variable, 'id')
            if validation_result == True:
                validated = True
                return temp_variable
            else:
                temp_variable = input("Sorry, you entered an invalid value. Please try again: ")
    
    else:
        temp_variable = input("Please enter your " + passed_input_type + ": ")
        validated = False
        while not validated:
            validation_result = validate_input(temp_variable, passed_input_type)
            if validation_result == True:
                validated = True
                return temp_variable
            else:
                temp_variable = input("Sorry, you entered an invalid value. Please try again: ")
            

def print_output(passed_list):
    """Prints clean output
    Arguments:
        passed_list {list} -- passes list for program to iterate through and displays values with cleaner output
    Returns:
        Nothing -- prints out list"""
    
    count_index = 0
    output_string = ""
        #Clean print of all employee information
    print("Employee Information:")
    for employee in passed_list:
        output_string = output_string + "Employee Index: " + str(count_index)
        output_string = output_string + " |  ID Number: " + employee['employee_id']
        output_string = output_string + " |  Name: " + employee['employee_name'].title()
        output_string = output_string + " |  Email: " + employee['employee_email']
        output_string = output_string + " |  Address: " + employee['employee_address'] + "\n"
                
        count_index = count_index + 1

    print(output_string)

