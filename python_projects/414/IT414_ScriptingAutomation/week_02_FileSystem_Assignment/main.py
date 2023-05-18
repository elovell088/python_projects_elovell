from functions.file_system_functions import *

#Program Prompt
print("\n\nWelcome to File Copier :)")
input("Press Enter to begin: ")

#Start Program
program_running = True
while program_running:
    #Gather folder names for the folder to copy and the folder to copy to
    file_to_copy = input("\n\nWhat is the folder would you like to copy?: ")
    file_to_copy_to = input("What folder would you like to copy to?: ")
    
    #Execute copyFile() Function 
    copyFiles(file_to_copy, file_to_copy_to)

    #Print copy folder success message
    destination_path = getPath(file_to_copy_to)
    print("\nSuccessfully copied files to " + destination_path)

    #Provide a method to terminate program
    user_decision = input('\n\nWould you like to copy another folder? (Y/N): ')
    user_decision = user_decision.lower()

    if user_decision == 'y':
        pass
    else:
        program_running = False
