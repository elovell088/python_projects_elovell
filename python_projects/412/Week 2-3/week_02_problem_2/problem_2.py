#IT 412 - Eric Lovell - Practice Lecture Problem 2
import os.path

file_name = "text_files/dinner_menu.txt"
#Write a while loop that prompts user forwhat they'd like for dinner throughout next week
program_running = True
while program_running:
    dinner_item = input("What would you like for dinner next week?: ")
    #Add selection to to a file called dinner_menu.txt
    if os.path.isfile(file_name):
        with open(file_name, "a") as txt_file:
            txt_file.write(dinner_item + "\n")
    else:
        with open(file_name, "w") as txt_file:
            txt_file.write(dinner_item)
    #Ask user if they want to make another dinner entry, if not, terminate program
    user_continue = input("Would you like to make another entry? (Y/N): ")
    user_continue = user_continue.lower()
    if user_continue == 'n':
        program_running = False