#IT 410 - Eric Lovell - Basic Condition Statements Lecture Assignment#


#Declaring variables to test conditional statements
variable1 = 23
variable2 = "String Value"
variable3 = 3.14159
variable4 = 15

#Equals conditional statement example
if variable1 == 23:
    print("Variable 1 is equal to 23")

#Less than conditional statement example
if variable4 < 23:
    print("Variable 4 is less than 23")

#Less than or equal to conditional statement example
if variable1 <= 23:
    print("Variable 1 is less than or equal to 23")

#Greater than or equal to conditional statement example
if variable4 >= 10:
    print("Variable 4 is greater than or equal to 10")

#Type function, elif, and else example
if type(variable3) is int:
    print("The variable is an integer")

elif type(variable3) is str:
    print("The variable is a string")

elif type(variable3) is float:
    print("The variable is a float")

else:
    print("The variable is something else.")