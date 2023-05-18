with open('./questions_um.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        # Add '"' to the beginning of the line
        new_line = '"' + line.strip()
        
        # Add '",\n' to the end of the string
        new_line += '",\n'
        
        # Write the new line to the output file
        outfile.write(new_line)
