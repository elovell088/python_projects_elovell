#IT 410 - Eric Lovell - Functions Assignment#

def bad_character_check(passed_string, passed_type):
    """Checks if string has bad characters
    Arguments:
        passed_string {String value} -- String value to check bad characters against
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


def validate_input(passed_input_type):
    """Validate input based on id, name, email, and address
    Arguments:
        passed_input_type {string value} -- Enter input type to validate  'id' 'name' 'email' or 'address'
    Returns:
        temp_variable {string value} -- return string variable only when entered correctly"""

    if passed_input_type == 'id':
        temp_variable = input("Please enter your employee ID: ")
        validated = False
        while not validated:
            if temp_variable.isdigit() and len(temp_variable) <= 7:
                validated = True
            else:
                temp_variable = input("Sorry, you entered an invalid character. Please try again..")

        return temp_variable

    else:
        temp_variable = input("Please enter your " + passed_input_type + ": ")
        validated = False
        while not validated:
            if bad_character_check(temp_variable, passed_input_type) == True or temp_variable.isdigit():
                temp_variable = input("Sorry, you entered an invalid character. Please try again: ")
            else:
                validated = True
        
        return temp_variable


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


#Start Main Program

#Create list to add employee dictionary too
employee_information = []
#Create flag to terminate program when necessary
program_running = True

while program_running:
    #Gather and validate employee id with custom function
    employee_id = validate_input('id')
    #Gather and validate employee name with custom function
    employee_name = validate_input('name')
    #Gather and validate employee email with custom function
    employee_email = validate_input('email')
    #Ask user if they would like to enter their address
    user_continue = input("Would you like to enter your address? (Y/N): ")
    user_continue = user_continue.lower()

    if user_continue != 'n':
        #If user selects yes, gather and validate employee address information
        employee_address = validate_input('address')
    else: 
        #If they select no, no address provided will be input as the address value
        employee_address = "- NO ADDRESS PROVIDED -"
    #Append validated employee information to list
    employee_information.append({'employee_id' : employee_id,
                                 'employee_name' : employee_name,
                                 'employee_email' : employee_email,
                                 'employee_address': employee_address})
    #Limit employee entries to 5 total 
    if len(employee_information) <= 4:
        add_another = input("Would you like to add another employee? (Y/N): ")
        add_another = add_another.lower()
        if add_another != 'n':
            program_running = True
        else:
            #Once 5 employees have entered, clean output provided by custom function
            print_output(employee_information)
            program_running = False
    else:
        #If does not want to add any more employees, clean output provided by custom function
        print_output(employee_information)
        program_running = False

