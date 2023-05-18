#IT 412 - Eric Lovell - Practice Lecture Problem 3
import os.path
#Modify code from Problem 1 to silently fail if input or output file was not found

input_file = 'text_files/5_favorite_movies.txt'
output_file = 'text_files/clean_output.txt'
new_output = ''

try:
    with open(input_file) as txt_file:
        for line in txt_file:
            new_line = line.rstrip() + " is a movie I like\n"
            new_output += new_line

except FileNotFoundError:
    pass
    
#Write out new output to a single new output file
with open(output_file, 'w') as file_object:
    if os.path.isfile(output_file):
        file_object.write(new_output.rstrip())
        

    


        