#TEST CODE

#IT 410 - Eric Lovell - While Loops Assignment#


#Create list to hold dictionaries of employee information
employee_information = []

#Create lists for bad characters unique to name, email, and address. Separate universal list created for characters that apply to all lists. 
name_bad_characters = ['@', '#', '(', ')', '_', ',', '/', '\\' ]

email_bad_characters = ['#', '(', ')', ',', '/', '\\', '\'' ]

address_bad_characters = ['@', '_', '\'' ]

universal_bad_characters = ['!', '"', '$', '%', '^', '&', '*', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}']

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
        
        if not id_validated:
            employee_id = input("Sorry, you entered an invalid ID Number. Please try again: ")

    #--END ID validation process--#

    #--START Name validation process--#
    
    first_name_validated = False
    last_name_validated = False

    while not name_validated:
        first_name = input("Please enter your first name: ")
        while not first_name_validated:
            #Value entered check
            if first_name and not first_name.isspace():
                #Two for loops to check if user input contains bad characters from two of the related lists. 
                for character in name_bad_characters:
                    if character in first_name:
                        contains_bad_characters = True
                for character in universal_bad_characters:
                    if character in first_name:
                        contains_bad_characters = True
                for character in number_characters:
                    if character in first_name:
                        contains_bad_characters = True
                #If statement to check for bad characters, if not, additional checks will continue
                if contains_bad_characters == True:
                    first_name_validated = False
                #Check make sure it is only upper/lower letters, no digits, no space. Break statements to terminate program if bad characters are entered.
                else:
                    first_name_validated = True
                    print("First name validated")
            else:
                first_name_validated = False

        #Catch all for invalid entry - Allows the user to re-enter the value correcly
            if not first_name_validated:
                contains_bad_characters = False
                first_name = input("Sorry, you entered an invalid first name. Please try again: ")

            first_name_validated = True

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
                #If statement to check for bad characters, if not, additional checks will continue
                if contains_bad_characters == True:
                    last_name_validated = False
                #Check make sure it is only upper/lower letters, no digits, no space. Break statements to terminate program if bad characters are entered.
                else:
                    last_name_validated = True
                    print("Last name validated")
            else:
                last_name_validated = False
        #Catch all for invalid entry - Allows the user to re-enter the value correcly
            if not last_name_validated:
                contains_bad_characters = False
                last_name = input("Sorry, you entered an invalid last name. Please try again: ")
            
            last_name_validated = True

        employee_name = first_name.strip().title() + " " + last_name.strip().title()
        print(employee_name)
        name_validated = True


    #--END name validation process--#
    
    #--START Email validation process--#
    first_part_validated = False
    second_part_validated = False
    last_part_validated = False

    while not email_validated:
        first_part_email = input("Please enter first part of your email: ")
        while not first_part_validated:
            if first_part_email and not first_part_email.isspace():
                for character in email_bad_characters:
                    if character in first_part_email:
                        contains_bad_characters = True
                for character in universal_bad_characters:
                    if character in first_part_email:
                        contains_bad_characters = True
                
                if contains_bad_characters == True:
                    first_part_validated = False
            #Check to validate if only whitespace was entered
                else:
                    first_part_validated = True
                    print("First part email validated")
            else:
                first_part_validated = False

            if not first_part_validated:
                contains_bad_characters = False
                first_part_email = input("You entered an invalid email. Please try again: ")
        
        second_part_email = input("Please enter the second part of your email: ")
        while not second_part_validated:
            if second_part_email.isalnum():
                second_part_validated = True
            else:
                second_part_validated = False
            
            if not second_part_validated:
                second_part_email = input("You entered invalid characters. Please try again: ")

        last_part_email = input("Please enter the last part of your email: ")
        while not last_part_validated:
            if last_part_email.isalpha():
                last_part_validated = True
                print("last part email validated")
            #Check to validate if only whitespace was entered
            else:
                last_part_validated = False
        

            if not last_part_validated:
                last_part_email = input("You entered an invalid character. Please only use letters and try again: ")

        employee_email = first_part_email.strip() + "@" + second_part_email + "." + last_part_email
        print(employee_email)

        email_validated = True
        #Catch all for invalid entry - Allows the user to re-enter the value correcly    
        

    #--END Email validation process--#

    #--START Address validation if provided--#

    #Ask user if they would like to enter their address. 
    enter_address_result = input("Would you like to provide your current address? (Y/N): ")
    enter_address_result = enter_address_result.lower()

    if enter_address_result != 'n':
        
        street_number_validated = False
        street_name_validated = False
        city_name_validated = False
        state_abbr_validated = False
        zip_code_validated = False

        #--START process to validate address entry
        while not address_validated:
            street_number = input("Please enter your street number: ")
            while not street_number_validated:
                #Check to make sure value was entered
                if street_number:
                    if street_number.isdigit() and not street_number.isspace():
                        street_number_validated = True
                        print("Street Number Validated")
                    else:
                        street_number_validated = False
                else: 
                    street_number_validated = False

                if not street_number_validated:
                    street_number = input("Sorry, you entered an invalid street number. Please try again: ")
            
            street_name = input("Please enter your street name: ")
            while not street_name_validated:
                if street_name:
                    if not street_name.isspace() and not street_name.isdigit():
                        
                        for character in address_bad_characters:
                            if character in street_name:
                                contains_bad_characters = True
                        for character in universal_bad_characters:
                            if character in street_name:
                                contains_bad_characters = True
                    #Throw error if bad characters are found
                        if contains_bad_characters == True:
                            street_name_validated = False
                    #Throw error if only white space is found
                        else:
                            street_name_validated = True
                            print("street name validated")
                    
                    else: street_name_validated = False
                #Throw error is no value was provided
                else:
                    address_validated = False
                   
                if not street_name_validated:
                    contains_bad_characters = False
                    street_name = input("Sorry, you entered an invalid street name. Please try again: ")
            
            city_name = input("Please enter your city: ")
            while not city_name_validated:
                if city_name:
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
                            print("City Name validated")
                    else:
                        city_name_validated = False
                #Throw error is no value was provided
                else:
                    city_name_validated = False

                if not city_name_validated:
                    contains_bad_characters = False
                    city_name = input("Sorry, you entered an invalid city. Please try again: ")

            state_abbr = input("Please enter your state abbreviation: ")
            while not state_abbr_validated:
                if state_abbr and not state_abbr.isspace():
                    if state_abbr.isalpha() and len(state_abbr) == 2:
                        state_abbr_validated = True
                        print("State validated")
                    else:
                        state_abbr_validated = False
                else:
                    state_abbr_validated = False

                if not state_abbr_validated:
                    state_abbr = input("Sorry, you entered an invalid state. Please try again: ")

            zip_code = input("Please enter your 5 digit zip code: ")
            while not zip_code_validated:
                if zip_code and not zip_code.isspace():
                    if zip_code.isdigit() and len(zip_code) == 5: 
                        zip_code_validated = True
                        print("Zip code validated")               
                    else:
                        zip_code_validated = False
                else:
                    zip_code_validated = False
                
                if not zip_code_validated:
                    zip_code = input("Sorry you input and invalid zip code. Please try again: ")

            employee_address = str(street_number).strip() + " " + street_name.strip().title() + ", " + city_name.strip().title() + ", " + state_abbr.upper() + " " + str(zip_code)

            address_validated = True
            #--END name validation process--#
            print(employee_address)

    
    else:
        #Process to compose message to user if they did not provide address 
        employee_address = "--Address not provided--"

    employee_information.append({'employee_id' : employee_id,
                                 'employee_name' : employee_name,
                                 'employee_email' : employee_email,
                                 'employee_address': employee_address})

    
    if program_index < 4:
        enter_more_info = input("Would you like to enter more employee information? (Y/N): ")
        enter_more_info = enter_more_info.lower()

        if enter_more_info != 'n':
            id_validated = False
            name_validated = False
            email_validated = False
            address_validated = False
        else:
            #Implement for loop for clean output if user decides they don't want to add any more employees
            count_index = 0
            output_string = ""

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
    else:
        #Implement for loop for clean output
        count_index = 0
        output_string = ""

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
