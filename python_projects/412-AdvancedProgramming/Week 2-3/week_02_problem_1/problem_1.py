#IT 412 - Eric Lovell - Week 2/3 Problem 1

#Create text file with 5 favorite movies, open in python and append phrase "is a movie to each line
new_output = ''
with open('text_files/5_favorite_movies.txt') as txt_file:
    for line in txt_file:
        new_line = line.rstrip() + " is a movie I like\n"
        new_output += new_line
    #test output
    print(new_output)
    
#Write out new output to a single new output file
with open('text_files/clean_output.txt', 'w') as file_object:
    file_object.write(new_output.rstrip())
        
        