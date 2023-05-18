#IT 412 - Eric Lovell - Practice Lecture Problem 4
import os.path
import json
#Load data from a file called my_car.json
json_file = 'text_files/my_car.json'

#Check to see if file exists
if os.path.isfile(json_file):
    file_exists = True
    #Check for data
    line_count = 0
    with open(json_file) as json_obj:
        for line in json_obj:
            line_count += 1
    if line_count >= 1:
        data_exists = True
    else: 
        data_exists = False
else:
    file_exists = False

#If the file doesn't exist or there is no data in it. Prompt the user for the model of there car and store it in json file
if file_exists == False or data_exists == False:
    car_model = input("Enter the model of your car: ")
    car_data = {"model" : car_model}
    with open(json_file, "w") as json_obj:
        json.dump(car_data, json_obj)
#If the file exists and there is data it, print out the contents
if file_exists and data_exists:
    with open(json_file) as json_obj:
        car_data = json.load(json_obj)
    
    print(car_data)
    
#Ask user if they would like to change the car model, if so modify and write to json file
user_continue = input("Would you like to change the model of your car? (Y/N): ")
user_continue = user_continue.lower()
if user_continue == 'y':
    car_model = input("Enter the model of you car: ")
    car_data = {"model" : car_model}
    with open(json_file, "w") as json_obj:
        json.dump(car_data, json_obj)
