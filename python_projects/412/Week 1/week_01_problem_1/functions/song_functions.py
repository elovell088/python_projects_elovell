#Problem 8-5 Functions

#Modify function from 8-4 to return a dictionary item in the discussed format
def song_information(passed_title, passed_artist):
    """Prints out message stating the song title and artist.
    Arguments:
        passed_title {any string value} -- Appeneds the song title to message
        
        passed_artist {any string or deafult value} -- appends the artist name or returns default value of 'Unknown'
    Returns 
        return_dictionary {dictionary value} -- returns dictionary of song information"""
    
    return_dictionary = {'song_title' : passed_title, 'song_artist' : passed_artist}

    return return_dictionary

#Introduce function that will loop through a list of dictionaries and print out each entry.
def loop_dictionary_list(passed_list):
    """Prints out message stating the song title and artist.
    Arguments:
        passed_list {list value} -- Provides list for to loop through and print
        
    Returns 
        Nothing -- Just prints list with clean output"""

    count_index = 0
    output_string = ""

    for item in passed_list:
        output_string += "Song Index: " + str(count_index)
        output_string += " | Title: " + item['song_title'].title()
        output_string += " | Artist: " + item['song_artist'].title() + "\n"

        count_index += 1
    
    print(output_string)

#Create an empty list called playlist and introduce while loop where users are asked to add songs to playlist
playlist = []

program_running = True