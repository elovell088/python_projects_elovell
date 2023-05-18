#IT 410 - Eric Lovell - While Loops Assignment#


#Create list to hold dictionaries of employee information
employee_information = []

#Create lists for bad characters unique to name, email, and address. Separate universal list created for characters that apply to all lists. 
name_bad_characters = ['@', '#', '(', ')', '_', ',', '/', '\\' ]

email_bad_characters = ['#', '(', ')', ',', '/', '\\', '\'' ]

address_bad_characters = ['@', '_', '\'' ]

universal_bad_characters = ['!', '"', '$', '%', '^', '&', '*', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}']
#Number list for instances where string cannot be alphanumeric but must be alpha
number_characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#Crate flag variable to terminate program if bad characters are entered
program_running = True
#Validation flags to check if a piece of information has been entered correctly
id_validated = False
name_validated = False
email_validated = False
address_validated = False

#Start program
while program_running:
    #Flag variable to determine if bad characters are found
    contains_bad_characters = False

    #--START ID validation process--#
    employee_id = input("Please enter your Employee ID: ")

    #Value entered check and check to make sure it is only digits 7 or less. Break statements to terminate program if bad characters are entered.
    if employee_id.isdigit() and len(employee_id) <= 7:
        print("ID validated")
        id_validated = True
    else:
        print("Sorry, you entered an invalid ID.")
        break
        
    #--END ID validation process--#


    #--START Name validation process--#
    first_name = input("Please enter your first name: ")
        #Value entered check
    if first_name and not first_name.isspace():
        #Three for loops to check if user input contains bad characters or alphanumeric values. Must contain alpha characters
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
            print("Sorry, you entered an invalid character.")
            break

        else:
            print("First name validated")
    else:
        print("You did not enter a value.")
        break

    #Variable for last name check
    last_name = input("Please enter your last name: ")
    #If statement for validation checks   
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
            print("Sorry, you entered an invalid character.")
            break
        else:
             print("Full name validated") 

    else:
        print("You did not enter a value.")
        break

    #Put name variables into full name variable and remove white space. Add title case.       
    employee_name = first_name.strip().title() + " " + last_name.strip().title()

    #--END name validation process--#
    
    
    #--START Email validation process--#
    first_part_email = input("Please enter first part of your email: ")
    #If statement for validation checks
    if first_part_email and not first_part_email.isspace():
        #For loops to check for invalid special characters
        for character in email_bad_characters:
            if character in first_part_email:
                contains_bad_characters = True
        for character in universal_bad_characters:
            if character in first_part_email:
                contains_bad_characters = True
        #Terminate if bad values are found       
        if contains_bad_characters == True:
            print("Sorry, you entered an invalid character.")
            break
        else:
            print("First part of email validated")
    else:
        print("You did not enter a value.")
        break
    
    #Begin second part of email validation  
    second_part_email = input("Please enter the second part of your email: ")
    if second_part_email.isalnum():
        print("Second part of email validated")
    else:
        print("Sorry, you entered an invalid character.")
        break
    
    #Begin last part of email
    last_part_email = input("Please enter the last part of your email: ")
    if last_part_email.isalpha():
        print("last part email validated")
    #Check to validate if only whitespace was entered
    else:
        print("You entered an invalid character.")
        break

    employee_email = first_part_email.strip() + "@" + second_part_email + "." + last_part_email
   
    #--END Email validation process--#

    #--START Address validation if provided--#

    #Ask user if they would like to enter their address. 
    enter_address_result = input("Would you like to provide your current address? (Y/N): ")
    enter_address_result = enter_address_result.lower()
    #If statement if user decides to add address
    if enter_address_result != 'n':
        
        #--START process to validate address entry
        street_number = input("Please enter your street number: ")
        #Check to make sure value is digit 
        if street_number.isdigit():
                print("Street Number Validated")
        else:
            print("Sorry, you entered an invalid character.")
            break
        #Begin validation checks for street name.       
        street_name = input("Please enter your street name: ")
        if street_name:
            if not street_name.isspace() and not street_name.isdigit():
                #Two for loops to check for bad characters
                for character in address_bad_characters:
                    if character in street_name:
                        contains_bad_characters = True
                for character in universal_bad_characters:
                    if character in street_name:
                        contains_bad_characters = True
                #Terminate if bad characters found
                if contains_bad_characters == True:
                    print("Sorry, you entered an invalid character.")
                    break
                else:
                    print("Street name validated")
                    
            else:
                print("Sorry, you entered an invalid character.")
                break
        else:
            print("You did not enter a value.")
            break
                
        #Begin check for city name         
        city_name = input("Please enter your city: ")
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
                    print("Sorry, you entered an invalid character.")
                    break
                #Throw error if only white space is found
                else:
                    print("City name validated")
            else:
                print("Sorry, you entered an invalid value.")
                break
        #Throw error is no value was provided
        else:
            print("You did not enter a value.")
            break
        
        #Begin check for state abbreviation
        state_abbr = input("Please enter your state abbreviation: ")
        if state_abbr.isalpha() and len(state_abbr) == 2:
            print("State validated")            
        else:
            print("Sorry, you entered an invalid value.")
            break

        #Begin check for zip code
        zip_code = input("Please enter your 5 digit zip code: ")
        #Input must contain only digits and must be 5 characters in length
        if zip_code.isdigit() and len(zip_code) == 5: 
            zip_code_validated = True
            print("Zip code validated")               
        else:
            break
        
        #Combine all address values into one variable
        employee_address = str(street_number).strip() + " " + street_name.strip().title() + ", " + city_name.strip().title() + ", " + state_abbr.upper() + " " + str(zip_code)

        #--END address validation process--#
    
    else:
        #If user decides not to enter an address. This will default to users address
        employee_address = "--Address not provided--"

    #Process to compose message to user 
    message = ""
    message += "Hello, " + employee_name.title() + ". "
    message += "Your Employee ID is " + employee_id + ", "
    message += "and your email address is " + employee_email + ". " 
    message += "Your address is " + employee_address + "."
        
    #Print message to user 
    print(message)
    break
