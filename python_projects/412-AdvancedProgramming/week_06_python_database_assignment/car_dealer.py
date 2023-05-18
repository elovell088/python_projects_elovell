#IT 412 - Eric Lovell - Week 6-7 Python Database Assignment

from classes.database_access import DB_Connect
from classes.modify_database import *

vehicle_database = DB_Connect('root', '', 'python_projects')
#my_db = DB_Connect('root', '', 'python_projects')
modify = ModifyDatabase()

#Start Program
program_running = True
while program_running:
    modify.programPrompts()
    user_selection = input("\nSelect from the prompts above - Please enter the number: ")
    
    #Option 1.) Calls showVehicle() Method
    if user_selection == '1':
        modify.showVehicles()
    
    #Option 2.) Calls addVehicle() Method
    elif user_selection == '2':
        modify.addVehicle()
    
    #Option 3.) Calls editVehicle() Method
    elif user_selection == '3':
        modify.editVehicle()
    
    #Option 4.) Calls removeVehicle() Method
    elif user_selection == '4':
        modify.removeVehicle()
    
    #Option 5.) Terminate program
    elif user_selection == '5':
        program_running = False
    
    #Catch all for invalid input entry
    else:
        print("Sorry, you entered an invalid character. Please try again. ")
    



