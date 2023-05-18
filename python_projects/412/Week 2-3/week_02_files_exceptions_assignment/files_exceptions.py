#IT 412 - Eric Lovell - Files and Exceptions Assignment
from functions.files_exceptions_functions import *

#Files program will work with
json_file = 'text_files/basic_config.json'
override_file = 'text_files/config_override.json'
backup_file = 'text_files/config_override.json.backup'

#Check for proper file to load
current_file = check_file(json_file, override_file)

#Startup display
startup_display(current_file)

#Start main program logic
program_running = True
while program_running:
    #Starting configurations, these change as modifications are saved
    original_config = load_data(current_file)
    current_config = load_data(current_file)

    #While loop to hold all the changes since last save
    changes_complete = False
    while not changes_complete:
        #Display prompts and input statement for user     
        program_prompts()
        prompt_choice = input("Please choose from the above prompts: ")
        
        #--ADD_DATA()--#
        if prompt_choice == 'a':
            new_config = add_data(current_config)
            print(display_data(new_config))
        
        #--MODIFY_DATA()--#
        elif prompt_choice == 'm':
            new_config = modify_data(current_config)
            print(display_data(new_config))
        
        #--REMOVE_DATA()--#
        elif prompt_choice == 'r':
            new_config = remove_data(current_config)
            print(display_data(new_config))

        #--SAVE_DATA() and BACKUP_DATA()--#
        elif prompt_choice == 's':
            save_message = input("Save current configurations? (Y/N): ")
            save_message = save_message.lower()
            
            if save_message == 'y':
                save_data(new_config, override_file)
                backup_data(original_config, backup_file)
                current_file = override_file
                print(display_data(new_config))
                changes_complete = True

        #--DISCARD DATA LOGIC--#
        elif prompt_choice == 'd':
            warning_message = input("Are you sure you want to discard your changes? (Y/N):")
            warning_message = warning_message.lower()
            
            if warning_message == 'y':
                current_config = change_configs(original_config)
                print(display_data(current_config))              

        #--TERMINATE PROGRAM LOGIC--#
        elif prompt_choice == 'x':
            warning_message = input("Are you sure you want to exit? Any unsaved changes will be lost. (Y/N):")
            warning_message = warning_message.lower()
            
            if warning_message == 'y':
                changes_complete = True
                program_running = False
        
        #Catch all if user enters values not in the prompt selection
        else:
            print("\nSorry, you entered an invalid character.")
    




