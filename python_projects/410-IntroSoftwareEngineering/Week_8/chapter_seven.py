#IT 410 - Eric Lovell - Chapter Seven Practice Problems#


#Problem 7-1

#Write a program that asks a user what their favorite restaurant is. 
users_favorite_restaurant = input("Please enter the name of your favorite restaurant: ")
#Check to see if user input a value and checking for white space characters.
if users_favorite_restaurant and not users_favorite_restaurant.isspace():
    print("Let me help you find the closest " + users_favorite_restaurant.title() + ".")
else:
    print("You didn't enter a value.")



#Problem 7-2

#Write a program that asks a user for two numbers.

users_first_number = input("Please enter first whole number: ")
#Check for invalid input like white space, strings, floats.
if users_first_number and not users_first_number.isspace():
    users_second_number = input("Please enter second whole number: ")
    if not users_first_number.isspace() and not users_second_number.isspace():
            multiplication_result = int(users_first_number) * int(users_second_number)
    else:
        print("You didn't enter a whole number.")    
else:
    print("You didn't enter a whole number.")



#Problem 7-3

#Write a while loop that asks a user what they are having for dinner. 
#Add flag for while loop and list to input user values
program_running = True
dinner_items = []
#While loop to terminate prgram
while program_running:
    
    food_item_ok = False
    #while loop for string validation
    while not food_item_ok:
        food_item = input("What are you having for dinner?: ")
    #Check to make sure value is input, check for white space, make sure only upper or lower case letters
        if food_item:         
                try:
                    #Check for invalid entries like only numbers, or only space, tabs, newlines.
                    if food_item.isspace() or food_item.isdigit():
                        food_item_ok = False
                    else:
                        dinner_items.append(food_item.lower())
                        food_item_ok = True
                except:
                    food_item_ok = False
        else:
            food_item_ok = False

        if not food_item_ok:
            print("You entered an invalid value! Please try again: ")

    add_another_food_item = input("Would you like to add another food item? (Y/N): ")
    add_another_food_item = add_another_food_item.lower()
    
    if add_another_food_item != "n":
        program_running = True
    else:
        program_running = False

count_index = 1
output_string = ""

print("Dinner Items:")
for food in dinner_items:
    output_string = output_string + "Food Item: " + str(count_index)
    output_string = output_string + " | " + food.title()
    output_string = output_string + "\n"

    count_index = count_index + 1

print(output_string)



#Problem 7-4 
#Create dictionary variable for carnival rides and prices.
#Problem 7-4 
#Create dictionary variable for carnival rides and prices.
carnival_rides = [{'number' : '1', 'name' : 'ferris wheel', 'price' : 2.00},
                  {'number' : '2','name' : 'tilt-a-whirl', 'price' : 3.00},
                  {'number' : '3','name' : 'pirate ship', 'price' : 3.50}] 
#Create string variable to ask user which ride they would like to go on
message_to_user = "What ride would you like to go on?"
message_to_user += "\nEnter the number 1 for: Ferris Wheel"
message_to_user += "\nEnter the number 2 for: Tilt-a-Whirl"
message_to_user += "\nEnter the number 3 for: Pirate Ship"
message_to_user += "\n"
#Create flag to break the loop
program_running = True

while program_running:

    users_choice = input(message_to_user)
    #Create flag to validate input
    users_input_ok = False
    
    #Check for proper string value begins
    for ride in carnival_rides:
        
            if ride['name'] == users_choice.lower():
                users_input_ok = True
                break

    #Int Validation checks begins
    while not users_input_ok:

        if users_choice:
            try:
                int(users_choice)
                if (len(users_choice)) == 1 and (int(users_choice) >= 1 and int(users_choice) <= 3):
                    users_input_ok = True

                else:
                    users_input_ok = False
            
            except:
                users_input_ok = False

        else:
            users_input_ok = False
        
        if not users_input_ok:
            users_choice = input("This ride wasn't found. Please try again: ")  
     
    #Input Validation complete
    #Process output for ride and price information.
    for ride in carnival_rides:   
        if ride['number'] == users_choice or ride['name'] == users_choice.lower():
            print("You chose the " + ride['name'].title() + " | Ticket Total: $" + str(ride['price']) + "0")


    program_running = False



#Problem 7-5

#Create a list of items you think you will need the next time you go to the grocery store.
list_of_items = ['eggs', 'bread', 'milk', 'eggs', 'cheese', 'crackers', 'eggs']

program_running = True

while program_running:
    for item in list_of_items:
        if item == 'eggs':
            list_of_items.remove(item)

        if 'egg' not in list_of_items:
            program_running = False

print(list_of_items)

