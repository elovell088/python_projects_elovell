from functions.regex_assignment_functions import *
import pyperclip
import re

program_running = True
while program_running:
    user_choice= input("\n1.) Pull data | 2.) Exit Program: ")
    print("\nPlease select from the prompts above: ")

    if user_choice == '1':
        user_ready = input("\nPlease copy data to clipboard and press Enter: ")
        new_data = displayData()
        print(new_data)
        pyperclip.copy(new_data)
        print("\nExtracted data has been copied to the clipboard.")

    elif user_choice == '2':
        program_running = False
        
    else:
        print("\nYou entered an invalid character. Please try again: ")