#IT 412 - Eric Lovell - Functions Assignment#
from functions.employee_input_functions import *

#Create list to add employee dictionary too
employee_information = []
#Create flag to terminate program when necessary
program_running = True

while program_running:
    #Gather and validate employee id with custom function
    employee_id = gather_input('id')
    #Gather and validate employee name with custom function
    employee_name = gather_input('name')
    #Gather and validate employee email with custom function
    employee_email = gather_input('email')
    #Ask user if they would like to enter their address
    user_continue = input("Would you like to enter your address? (Y/N): ")
    user_continue = user_continue.lower()

    if user_continue != 'n':
        #If user selects yes, gather and validate employee address information
        employee_address = gather_input('address')
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

