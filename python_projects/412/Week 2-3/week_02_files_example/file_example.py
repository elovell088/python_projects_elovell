#IT 412 - Eric Lovell - File Example Practice Lecture Assignment

import os.path
import shutil
import time
#How to open and display a text file example
with open("text_files/SacramentocrimeJanuary2006.csv") as csv_file:
    for line in csv_file:
        print(line)


#How to modify a csv file and split up into a list format example
with open("text_files/SacramentocrimeJanuary2006.csv") as csv_file:
    for line in csv_file:
        temp_line = line.split(",")
        place_counter = 0
        #How to remove substrings from csv file and clean up the file example
        while place_counter < len(temp_line):
            temp_line[place_counter] = temp_line[place_counter][1:-1]
            #How to pull specific information from the file example
            if place_counter == 0:
                print(temp_line[place_counter])
            if place_counter == 1:
                print(temp_line[place_counter])
            if place_counter == 5:
                print(temp_line[place_counter] + "\n\n")
            place_counter += 1


#How to remove comments from a python file example
temp_output = ""
with open("text_files/pet.py") as python_file:
    for line in python_file:
        temp_line = line.strip()
        if temp_line.startswith("#") or temp_line.startswith('"""'):
            pass
        else:
            temp_output = temp_output + line

print(temp_output)


#How to modify contents of a file and output the content to a new file
temp_output = ""
with open("text_files/pet.py") as python_file:
    for line in python_file:
        temp_line = line.strip()
        if temp_line.startswith("#") or temp_line.startswith('"""'):
            pass
        else:
            temp_output = temp_output + line
#Code that will create a back up file if the file already exists example
if os.path.isfile("text_files\cleaned_output.py"):
    shutil.copy2("text_files\cleaned_output.py", "text_files\cleaned_output.py.backup" + str(time.time()))

with open("text_files\cleaned_output.py", "w") as file_output:
    file_output.write(temp_output)

