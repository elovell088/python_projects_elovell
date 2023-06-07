#IT463 - Eric Lovell - Authencation Functions
from functions.hash_functions import *
import json

#Load password storage file
with open("password_store.json", "r") as file_load:
    stored_passwords = json.load(file_load)

#User input
username_input = input("Please enter your username: ")
password_input = input("Please enter your password: ")

#Hash password input
hashed_password = createHash(password_input)

authenticated = False
for item in stored_passwords:
    if item["username"] == username_input:
        if item["password"] == hashed_password:
            authenticated = True
        break

if authenticated:
    print("You have been authenticated")
else:
    print("Authentication failed.")