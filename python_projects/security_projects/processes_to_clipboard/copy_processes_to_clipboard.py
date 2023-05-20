#Security Projects - Copies running processes on system and copies it to clipboard - Written by: Eric Lovell

#REQUIRED:
#pip install psutil
#pip install pyperclip

import psutil
import pyperclip

# Get a list of running processes
processes = psutil.process_iter()

# Create an empty string to store the process information
process_info = ""

# Iterate over each process and append its information to the string
for process in processes:
    process_info += str(process) + "\n"

# Copy the process information to the clipboard
pyperclip.copy(process_info)

print("Process information has been copied to the clipboard.")
