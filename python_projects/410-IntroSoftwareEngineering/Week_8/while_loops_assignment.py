#IT 410 - Eric Lovell - While Loops Assignment#


#Create list to hold dictionaries of employee information
employee_information = []

#Create lists for bad characters unique to name, email, and address. Separate universal list created for characters that apply to all lists. 
name_bad_characters = ['@', '#', '(', ')', '_', ',', '/', '\\' ]

email_bad_characters = ['#', '(', ')', ',', '/', '\\', '\'' ]

address_bad_characters = ['@', '_', '\'' ]

universal_bad_characters = ['!', '"', '$', '%', '^', '&', '*', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}']
#List of numbers to validate input that can't be alphanumeric but must be alpha
number_characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#Crate flag variable to terminate program if bad characters are entered
program_running = True
#Validation flags to check if a piece of information has been entered correctly
id_validated = False
name_validated = False
email_validated = False
address_validated = False

#Count index to control number of employee information that can be entered into list
program_index = 0

#Start program
while program_running:
    #Flag variable to determine if bad characters are found
    contains_bad_characters = False

    #--START ID validation process--#
    employee_id = input("Please enter your Employee ID: ")

    while not id_validated:
    #Value entered check and check to make sure it is only digits 7 or less. Break statements to terminate program if bad characters are entered.
        if employee_id.isdigit() and len(employee_id) <= 7:
            print("ID validated")
            id_validated = True
        else:
             id_validated = False
        #Allow user to reenter values
        if not id_validated:
            employee_id = input("Sorry, you entered an invalid ID Number. Please try again: ")

    #--END ID validation process--#

    #--START Name validation process--#
    #Flags to chedck for invalid input for firstand last names
    first_name_validated = False
    last_name_validated = False

    while not name_validated:
        first_name = input("Please enter your first name: ")
        #Nested while loop to allow user to reenter first name 
        while not first_name_validated:
            #Value entered check
            if first_name and not first_name.isspace():
                #Three for loops to check if user input contains bad characters. Number Checks for alphanumeric string. Must be alpha
                for character in name_bad_characters:
                    if character in first_name:
                        contains_bad_characters = True
                for character in universal_bad_characters:
                    if character in first_name:
                        contains_bad_characters = True
                for character in number_characters:
                    if character in first_name:
                        contains_bad_characters = True
                #If statement to check if bad characters were found
                if contains_bad_characters == True:
                    first_name_validated = False
                else:
                    first_name_validated = True
                    print("First name validated")
            else:
                first_name_validated = False

        #Catch all for invalid entry - Allows the user to re-enter the value correcly
            if not first_name_validated:
                #Bring variables back to false state
                contains_bad_characters = False
                first_name = input("Sorry, you entered an invalid first name. Please try again: ")

            first_name_validated = True
        #Begin last name check
        last_name = input("Please enter your last name: ")
        while not last_name_validated:
            if last_name and not last_name.isspace():
                #Three for loops to check if user input contains bad characters or alpha numeric values
                for character in name_bad_characters:
                    if character in last_name:
                        contains_bad_characters = True
                for character in universal_bad_characters:
                    if character in last_name:
                        contains_bad_characters = True
                for character in number_characters:
                    if character in last_name:
                        contains_bad_characters = True
                #If statement to check if bad characters were found
                if contains_bad_characters == True:
                    last_name_validated = False
                else:
                    last_name_validated = True
            else:
                last_name_validated = False
        #Catch all for invalid entry - Allows the user to re-enter the value correcly
            if not last_name_validated:
                contains_bad_characters = False
                last_name = input("Sorry, you entered an invalid last name. Please try again: ")
            
            last_name_validated = True
        #Put name values into single variable. Title case, strip white space
        employee_name = first_name.strip().title() + " " + last_name.strip().title()
        print("Full name validated")
        name_validated = True

    #--END name validation process--#
    
    #--START Email validation process--#
    #Flags to chedk for first, second and last part of email <first_part>@<second_part.<third_part>
    first_part_validated = False
    second_part_validated = False
    last_part_validated = False

    while not email_validated:
        first_part_email = input("Please enter first part of your email: ")
        #Nested while loop to validate first part of email 
        while not first_part_validated:
            #IF statement to check if value was entered or whitespace
            if first_part_email and not first_part_email.isspace():
                #For loops to check for bad characters
                for character in email_bad_characters:
                    if character in first_part_email:
                        contains_bad_characters = True
                for character in universal_bad_characters:
                    if character in first_part_email:
                        contains_bad_characters = True
                #IF to determine if bad characters were found
                if contains_bad_characters == True:
                    first_part_validated = False
                else:
                    first_part_validated = True
                    print("First part email validated")
            else:
                first_part_validated = False
            #If first part fails, this if statement allows user to retry
            if not first_part_validated:
                contains_bad_characters = False
                first_part_email = input("You entered an invalid email. Please try again: ")
        
        #Begin checks for second part of email address
        second_part_email = input("Please enter the second part of your email: ")
        while not second_part_validated:
            #Checks if second part is alphanumerical
            if second_part_email.isalnum():
                second_part_validated = True
            else:
                second_part_validated = False
            #Allow user to reenter values if validation fails
            if not second_part_validated:
                second_part_email = input("You entered invalid characters. Please try again: ")
        #Begin checks for last part of email
        last_part_email = input("Please enter the last part of your email: ")
        while not last_part_validated:
            #Check to make sure it is alpah only and 3 or less characters long
            if last_part_email.isalpha() and len(last_part_email) <= 3:
                last_part_validated = True
                print("Email address validated")
            #Check to validate if only whitespace was entered
            else:
                last_part_validated = False
            #Allow user to reenter values
            if not last_part_validated:
                last_part_email = input("You entered an invalid character. Please only use 1-3 letters and try again: ")

        #Combine all email values into one variable. Strip whitespace
        employee_email = first_part_email.strip() + "@" + second_part_email + "." + last_part_email

        email_validated = True
        #Catch all for invalid entry - Allows the user to re-enter the value correcly    
        
        #--END Email validation process--#

    
    #--START Address validation if provided--#
    #Ask user if they would like to enter their address. 
    enter_address_result = input("Would you like to provide your current address? (Y/N): ")
    enter_address_result = enter_address_result.lower()

    if enter_address_result != 'n':
        #create flags for each section of address entries
        street_number_validated = False
        street_name_validated = False
        city_name_validated = False
        state_abbr_validated = False
        zip_code_validated = False

        #--START process to validate address entry
        while not address_validated:
            #Begin Checks for street number. Make sure it is digits
            street_number = input("Please enter your street number: ")
            while not street_number_validated:
                #Check to make sure value was entered
                if street_number.isdigit():
                    street_number_validated = True
                    print("Street Number Validated")
                else:
                        street_number_validated = False
                #Allow user to reenter values
                if not street_number_validated:
                    street_number = input("Sorry, you entered an invalid street number. Please try again: ")
            
            #Begin checks for street name
            street_name = input("Please enter your street name: ")
            while not street_name_validated:
                if street_name:
                    #No whitespace and no digit checks
                    if not street_name.isspace() and not street_name.isdigit(): 
                        #For loops to check for bad characters                  
                        for character in address_bad_characters:
                            if character in street_name:
                                contains_bad_characters = True
                        for character in universal_bad_characters:
                            if character in street_name:
                                contains_bad_characters = True
                        #Throw error if bad characters are found
                        if contains_bad_characters == True:
                            street_name_validated = False
                        else:
                            street_name_validated = True
                            print("Street name validated")               
                    else: street_name_validated = False
                #Throw error is no value was provided
                else:
                    address_validated = False
                #Allow user to reenter values
                if not street_name_validated:
                    contains_bad_characters = False
                    street_name = input("Sorry, you entered an invalid street name. Please try again: ")
            
            #Begin checks for city name
            city_name = input("Please enter your city: ")
            while not city_name_validated:
                if city_name:
                    #No white space and no digit checks
                    if not city_name.isspace() and not city_name.isdigit():
                        #Two for loops to check if user input contains bad characters from two of the related lists. 
                        for character in address_bad_characters:
                            if character in city_name:
                                contains_bad_characters = True
                        for character in universal_bad_characters:
                            if character in city_name:
                                contains_bad_characters = True
                        #Throw error if bad characters are found
                        if contains_bad_characters == True:
                            city_name_validated = False
                        #Throw error if only white space is found
                        else:
                            city_name_validated = True
                            print("City name validated")
                    else:
                        city_name_validated = False
                #Throw error is no value was provided
                else:
                    city_name_validated = False
                #Allow user to reenter values
                if not city_name_validated:
                    contains_bad_characters = False
                    city_name = input("Sorry, you entered an invalid city. Please try again: ")
            #Begin State abbreviation check
            state_abbr = input("Please enter your state abbreviation: ")
            while not state_abbr_validated:
                #Make sure only alpha characters are inputted
                if state_abbr.isalpha() and len(state_abbr) == 2:
                    state_abbr_validated = True
                    print("State validated")
                else:
                    state_abbr_validated = False
                #Allow user to reenter values
                if not state_abbr_validated:
                    state_abbr = input("Sorry, you entered an invalid state. Please try again: ")

            #Begin zip code validation check
            zip_code = input("Please enter your 5 digit zip code: ")
            while not zip_code_validated:
                #Only digits can be entered with length of 5 characters
                if zip_code.isdigit() and len(zip_code) == 5: 
                    zip_code_validated = True
                    print("Zip code validated")               
                else:
                    zip_code_validated = False
                #Allow user to reenter values
                if not zip_code_validated:
                    zip_code = input("Sorry you input and invalid zip code. Please try again: ")
            
            #Combine employee address values into one variable. Title ane strip whitespace
            employee_address = str(street_number).strip() + " " + street_name.strip().title() + " " + city_name.strip().title() + " " + state_abbr.upper() + " " + str(zip_code)

            address_validated = True
            #--END name validation process--#


    
    else:
        #Process to compose message to user if they did not provide address 
        employee_address = "--Address not provided--"

    employee_information.append({'employee_id' : employee_id,
                                 'employee_name' : employee_name,
                                 'employee_email' : employee_email,
                                 'employee_address': employee_address})

    #If statement for program index that will only allow up to 5 employees to be entered into system
    if program_index < 4:
        enter_more_info = input("Would you like to enter more employee information? (Y/N): ")
        #Lower case the inputted value
        enter_more_info = enter_more_info.lower()

        #Reset values to false so program can start over
        if enter_more_info != 'n':
            id_validated = False
            name_validated = False
            email_validated = False
            address_validated = False
        else:
            #Implement for loop for clean output if user decides they don't want to add any more employees
            count_index = 0
            output_string = ""
            #Clean print of all employee information
            print("Employee Information:")
            for employee in employee_information:
                output_string = output_string + "Employee Index: " + str(count_index)
                output_string = output_string + " |  ID Number: " + employee['employee_id']
                output_string = output_string + " |  Name: " + employee['employee_name'].title()
                output_string = output_string + " |  Email: " + employee['employee_email']
                output_string = output_string + " |  Address: " + employee['employee_address'] + "\n"
                
                count_index = count_index + 1

            print(output_string)

            #Terminate program
            program_running = False
    #If 5 employees have been entered. Program automatically comes here
    else:
        #Implement for loop for clean output
        count_index = 0
        output_string = ""
        #Print Clean output of all employee information
        print("Employee Information:")
        for employee in employee_information:
            output_string = output_string + "Employee Index: " + str(count_index)
            output_string = output_string + " |  ID Number: " + employee['employee_id']
            output_string = output_string + " |  Name: " + employee['employee_name'].title()
            output_string = output_string + " |  Email: " + employee['employee_email']
            output_string = output_string + " |  Address: " + employee['employee_address'] + "\n"
            
            count_index = count_index + 1

        print(output_string)
        #Terminate Program
        program_running = False



    program_index = program_index + 1

    