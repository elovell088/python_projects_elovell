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


def multiplyTwoNumbers(passed_list):
    """Divde the two numbers"""
    multiply_results = []
    numbers_ok = True
    passed_number1 = 1
    passed_number2 = 1

    for multiply_vals in passed_list:
        numbers_ok = True
        try:
            passed_number1 = int(multiply_vals['top_number'])
        except:
            print("The first parameter is not an integer")
            numbers_ok = False
        try:
            passed_number2 = int(multiply_vals['bottom_number'])
        except:
            print("The second parameter is not an integer")
            numbers_ok = False
    
        if numbers_ok:
            multiply_result = passed_number1 * passed_number2
            multiply_results.append(multiply_result)

    return multiply_results
