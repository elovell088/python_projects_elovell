#IT 410 - Eric Lovell - Chapter 8 Practice Problems#


#Problem 8-1

#Write function that accepts the name of your favorite radio station
def favoriteRadioStation(passed_radio_station):
    """Prints out message stating favorite radio station
    Arugments:
        passed_radio_station {any string value} -- Will be appended to a message
        
    Returns:
        Nothing - just prints out message"""


    print("Let me tune in " + passed_radio_station + ".")
        
favorite_radio_station = input("What is your favorite radio station?: ")
if favorite_radio_station and not favorite_radio_station.isspace():
    favoriteRadioStation(favorite_radio_station)
else:
    print("You did not enter a value.")


#Problem 8-2

#Write a function called print_business_cards
def print_business_cards(passed_name, passed_quantity, passed_tag):
    """Prints out message stating how many business cards, who they are for, and a tagline.
    Arguments:
        passed_name {any string value} -- Appends name to printed message
        
        passed_quantity {integer value} -- Appends number of business cards to printed message
        
        passed_tag {any string value} -- Appends tagline to printed message 
    Returns:
        Nothing - just prints message"""
    #Print statement for the function
    print("Number of Business Cards: " + str(passed_quantity) + " | Name: " + passed_name.title() + " | Tagline: " + passed_tag)

#Call the function three times passing different arguments into it
print_business_cards("tyler durden", 200, "You do not talk about fight club!")
print_business_cards("Ave Ventura", 500, "When nature calls!")
print_business_cards("jordan belfort", 300, "Get rich by selling penny stocks!")


#Problem 8-3

#Re-write function from 8-2 to default to 100
def print_business_cards(passed_name, passed_tag, passed_quantity=100):
    """Prints out message stating how many business cards, who they are for, and a tagline.
    Arguments:
        passed_name {any string value} -- Appends name to printed message
        
        passed_quantity {integer value} -- Appends number of business cards to printed message
        
        passed_tag {any string value} -- Appends tagline to printed message 
    Returns:
        Nothing - just prints message"""
    #Print statement for the function
    print("Number of Business Cards: " + str(passed_quantity) + " | Name: " + passed_name.title() + " | Tagline: " + passed_tag)

#Call the function three times passing different arguments into it
print_business_cards("tyler durden", "You do not talk about fight club!", 150)
print_business_cards("Ave Ventura", "When nature calls!")


#Problem 8-4

#Write function that accepts song information (title and artist) Default value for artist. 
def song_information(passed_title, passed_artist="Unknown"):
    """Prints out message stating the song title and artist.
    Argumetns:
        passed_title {any string value} -- Appeneds the song title to message
        
        passed_artitst {any string or deafult value} -- appends the artist name or returns default value of 'Unknown'
    Returns 
        return_message {string value} -- returns the concatenated message"""
    
    return_message = passed_title.title() + " by " + passed_artist.title() + "."

    return return_message

top_rap_song = song_information("humble", "kendrick lamar")
print(top_rap_song)
top_country_song = song_information("country girl", "Luke Bryan")
print(top_country_song)
top_pop_song = song_information("turn it up")
print(top_pop_song)


#Problem 8-5

#Modify function from 8-4 to return a dictionary item in the discussed format
def song_information(passed_title, passed_artist="Unknown"):
    """Prints out message stating the song title and artist.
    Arguments:
        passed_title {any string value} -- Appeneds the song title to message
        
        passed_artitst {any string or deafult value} -- appends the artist name or returns default value of 'Unknown'
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

while program_running:
    playlist_completed = False
    song_title = input("Please enter the song title: ")
    while not playlist_completed:
        if song_title and not song_title.isspace():
            song_artist = input("Please enter the song artist: ")
            if song_artist and not song_artist.isspace():
                #Create dictionary item from user input
                song_dictionary = song_information(song_title, song_artist)
                #Append dictionary to playlist list
                playlist.append(song_dictionary)
            else:
                print("Sorry, you did not enter a value: ")
                break
        else:
            print("Sorry, you did not enter value: ")
            break
        #Provide way for user to break the loop
        user_continue = input("Would you like to add another song to your playlist? (Y/N): ")
        user_continue = user_continue.lower()
        
        if user_continue != "n":
            song_title = input("Please enter song title: ")
        else:
            playlist_completed = True
    
    program_running = False
#Print playlist
loop_dictionary_list(playlist)
