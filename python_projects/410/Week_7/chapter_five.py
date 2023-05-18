#IT 410 - Eric Lovell - Chapter 5 Problems Assignment#


#Problem 5-1 

#Create variables to use for six conditional tests
my_favorite_colors = ["red", "orange", "yellow", "green", "purple", "blue", "black"]

your_favorite_colors = ["red", "orange", "yellow", "magenta", "blue"]

least_favorite_color = "brown"

the_best_color = "red"

numeric_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number_variable_1 = 3

number_variable_2 = 33

float_variable = 3.33

#1.) I expect the expression below to evaluate to True
print(my_favorite_colors < your_favorite_colors and the_best_color > least_favorite_color)

#2.) I expect the expression below to evaluate to True
print((number_variable_1 or number_variable_2) in numeric_list)

#3.) I expect the expression below to evaluate to True
print(type(float_variable) is float and type(number_variable_1) is int)

#4.) I expect the expression below to evaluate to False
print(number_variable_2 >= sum(numeric_list) or number_variable_2 <= number_variable_1)

#5.) I expect the expression below to evaluate to False
print(the_best_color not in (my_favorite_colors and your_favorite_colors))

#6.) I expect the expression below to evaluate to False
print(numeric_list[2] == float_variable or least_favorite_color in (my_favorite_colors or your_favorite_colors))



#Problem 5-2

#Pick a number from 1 to 10 and store it as a variable
my_number = 3
#Pick another number 
my_other_number = 8

#If statmenet to determine if odd - Evaluate to True
if my_number % 2 == 1:
    print("You chose an odd number!")
#If statement for my other number - Evaluate to False
if my_other_number % 2 == 1:
    print("You chose an odd number!")



#Problem 5-3

#Choose two numbers to run if test to determine if odd
my_number = 3
my_other_number = 8

#Modify if statement from 5-2 to use if-else - Display message if odd
if my_number % 2 == 1:
    print("You chose an odd number!")
else:
    my_number = my_number + 1
#If number isn't odd - add one to it and print it out
if my_other_number % 2 == 1:
    print("You chose an odd number!")
else:
    my_other_number = my_other_number + 1
    print(my_other_number)



#Problem 5-4

#Create a list of my favorite fruits
my_favorite_fruits = ["apples", "oranges", "bananas", "pears", "peaches"]

#Write if-elif-else chain to check length of list and write message stating how many fruits there are
if len(my_favorite_fruits) == 2:
    print("You like two fruits!")

elif len(my_favorite_fruits) == 3:
    print("You like three fruits!")

elif len(my_favorite_fruits) == 4:
    print("You like four fruits!")

else:
    print("Wow, you like several fruits!")



#Problem 5-5

#Create a list of number from 1-55
one_to_fifty_five = list(range(1,56))

#Pick two numbers and store them as variables
my_number_1 = 3

my_number_2 = 333

#Conditional statement to determine is number 1 is on the list
if my_number_1 in one_to_fifty_five:
    print(str(my_number_1) + " was found!")
else:
    print(my_number_1 + "was not found.")
#Conditional statement to determine if number 2 is on the list
if my_number_2 in one_to_fifty_five:
    print(str(my_number_2) + " was found!")
else:
    print(str(my_number_2) + " was not found.")



#Problem 5-6

#Make a list of my favorite stores
my_favorite_stores = ["walmart", "microcenter", "cabelas", "bass pro shop", "amazon"]
#Make another list of stores currently running sales (Basing this off discount deals I find on groupon.com)
stores_running_sales = ["amazon", "costco", "walmart", "target", "nike"]

#Loop through the list of stores and check to see if any are running a sale
for store in my_favorite_stores:
    #If statement to print message if store is running a sale or if it is not
    if store in stores_running_sales:
        print("Take advantage of this sale currently at " + store.title() + "!")
    else:
        print(store.title() + " isn't currently running a sale.")


