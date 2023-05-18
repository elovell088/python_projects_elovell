#IT 410 - Eric Lovell - Working with Functions Lecture#

#Create a basic function
def divideTwoNumbers(passed_number1, passed_number2):
    """Divde the two numbers"""

    divide_result = passed_number1 / passed_number2

    print(divide_result)

divideTwoNumbers(10, 5)

#Create a basic function with input validation
def divideTwoNumbers(passed_number1, passed_number2):
    """Divde the two numbers"""
    passed_number1 = int(passed_number1)
    passed_number2 = int(passed_number2)
    divide_result = passed_number1 / passed_number2

    print(divide_result)

divideTwoNumbers(10, 5)

#Create a basic function with input validation and Try/Except Blocks and return - Error in example
def divideTwoNumbers(passed_number1, passed_number2):
    """Divde the two numbers"""
    try:
        passed_number1 = int(passed_number1)
    except:
        print("The first parameter is not an integer")
        return
    try:
        passed_number2 = int(passed_number2)
    except:
        print("The second parameter is not an integer")
        return
    
    
    divide_result = passed_number1 / passed_number2

    print(divide_result)

divideTwoNumbers(10, 'cheese')

#Create a basic function with input validation and Try/Except Blocks and return - Error in example
def divideTwoNumbers(passed_number1, passed_number2):
    """Divde the two numbers"""
    try:
        passed_number1 = int(passed_number1)
    except:
        print("The first parameter is not an integer")
        return
    try:
        passed_number2 = int(passed_number2)
    except:
        print("The second parameter is not an integer")
        return
    
    
    divide_result = passed_number1 / passed_number2

    print(divide_result)

#Optional paremeters with default value example
def divideTwoNumbers(passed_number1, passed_number2=2):
    """Divde the two numbers"""
    try:
        passed_number1 = int(passed_number1)
    except:
        print("The first parameter is not an integer")
        return
    try:
        passed_number2 = int(passed_number2)
    except:
        print("The second parameter is not an integer")
        return
    
    
    divide_result = passed_number1 / passed_number2

    print(divide_result)

#Returning value from function into main example
def divideTwoNumbers(passed_number1, passed_number2=2):
    """Divde the two numbers"""
    try:
        passed_number1 = int(passed_number1)
    except:
        print("The first parameter is not an integer")
        return
    try:
        passed_number2 = int(passed_number2)
    except:
        print("The second parameter is not an integer")
        return
    
    
    divide_result = passed_number1 / passed_number2
    
    return divide_result

division_result = divideTwoNumbers(10, 5)
print("The result of the division is " + str(division_result))


#Passing a list into a function example
def divideTwoNumbers(passed_list):
    """Divde the two numbers"""
    divide_results = []
    numbers_ok = True
    passed_number1 = 1
    passed_number2 = 1

    for divide_vals in passed_list:
        numbers_ok = True
        try:
            passed_number1 = int(divide_vals['top_number'])
        except:
            print("The first parameter is not an integer")
            numbers_ok = False
        try:
            passed_number2 = int(divide_vals['bottom_number'])
        except:
            print("The second parameter is not an integer")
            numbers_ok = False
    
        if numbers_ok:
            divide_result = passed_number1 / passed_number2
            divide_results.append(divide_result)

    return divide_results


division_list = [{'top_number' : 1, 'bottom_number' : 2,}, {'top_number' : 9, 'bottom_number' : 3}]
the_result = divideTwoNumbers(division_list)
print("The result of the division is: ")
print(the_result)
