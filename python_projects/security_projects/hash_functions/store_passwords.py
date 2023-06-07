#IT 463 - Eric Lovell - Hash functions for storing passwords securely

from functions.hash_functions import *
import json

#Create list for dictionaries
credentials = []

#While loop until credential list is complete
list_complete = False
while not list_complete:
    username = input("Please enter username: ")
    password = input("Please enter password: ")

    #Hash Password
    hashed_password = createHash(password)

    #Append dictionary to list
    temp_dictionary = {"username" : username, "password" : hashed_password}
    credentials.append(temp_dictionary)


    ask_user = input("\nContinue?(Y/N): ")
    ask_user.lower().strip()
    print("\n")

    if ask_user == "n":
        list_complete = True

#Save to file
with open("password_store.json", "w") as password_store:
    json.dump(credentials, password_store)

