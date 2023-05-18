#IT 410 - Eric Lovell - Chapter 2 Problems#

#Problem 2-1

#Declare variable for my favorite restaurant
my_favorite_restaurant = "Lucianos"

#Print variable
print(my_favorite_restaurant)

#Change variable value to favorite dish at the restaurant
my_favorite_restaurant = "Fettuccini Alfredo"

#Print variable after change 
print(my_favorite_restaurant)



#Problem 2-2

#Declare variable for last business I made purchase from
last_business = "Walgreens"

#Declare variable for items purchased on last trip
last_purchase = "bottled water"

#Print out message using these two variables 
print("The last time I went to " + last_business + " I purchased a " + last_purchase + ".")



#Problem 2-3

#Declare variable for my favorite car
favorite_car = "dodge ram"

#Print using lower method
print(favorite_car.lower())

#Print using upper method
print(favorite_car.upper())

#Print using title method
print(favorite_car.title())



#Problem 2-4

#Declare variable with favorite quote, add \t\n to beginning and end of it
favorite_quote = "Never trust a computer you can't throw out a window"

#Add \t\n to beginning and end using concatenation
favorite_quote = "\t\n" + favorite_quote + "\t\n"

#Print out quote
print(favorite_quote)

#Apply lstrip() to quote
favorite_quote = favorite_quote.lstrip()

#Print result of lstrip() quote
print(favorite_quote)

#Apply strip() to quote
favorite_quote = favorite_quote.strip()

#Print result of strip() quote
print(favorite_quote)



#Problem 2-5

#Create my own math problem and store the result as a variable
my_math_problem_result = 3 * 3 / 3 + 3 - 3 

#Print a message that says "The result of my math problem is: (stored result)"
print("The result of my math problem is: " + str(my_math_problem_result) + ".")

