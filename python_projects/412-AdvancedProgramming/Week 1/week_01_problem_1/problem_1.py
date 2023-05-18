from functions.song_functions import *

#Create an empty list called playlist and introduce while loop where users are asked to add songs to playlist
playlist = []
#Flag used to terminate while loop
program_running = True
#While loop to gather user input for song title
while program_running:
    playlist_completed = False
    song_title = input("Please enter the song title: ")
    #Nested while loop to gather user input for artist name
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