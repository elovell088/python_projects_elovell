#IT 412 - Eric Lovell - Final Project Main
from classes.modify_database import *
from classes.setup import Setup
from classes.database_access import DB_Connect

modify = ModifyDatabase()
setup = Setup()
#database_connection = DB_Connect('root', '', 'python_projects')


#Pull ID info from database, Upload to config file - setup_config.json
setup.clearScreen()
setup.sync_database()

#File to enter into Database
import_file = "text_files/customer_export.txt"

#Start Program
program_running = True
while program_running:
    database_connection = DB_Connect('root', '', 'python_projects')
    setup.programPrompts()
    user_selection = input("\nSelect from the prompts above - Please enter the number: ")
    
    #Option 1.) IMPORT DATA

    if user_selection == '1':
        setup.clearScreen()
        modify.importData(import_file)
    
    #Option 2.) SHOW DATA
    elif user_selection == '2':
        setup.clearScreen()
        modify.getDatabase()
    
    #Option 3.) ADD RECORD
    elif user_selection == '3':
        setup.clearScreen()
        modify.addRecord()
    
    #Option 4.) EDIT RECORD
    elif user_selection == '4':
        setup.clearScreen()
        modify.editRecord()
    
    #Option 5.) Terminate program
    elif user_selection == '5':
        program_running = False
    
    #Catch all for invalid input entry
    else:
        print("Sorry, you entered an invalid character. Please try again. ")
    
