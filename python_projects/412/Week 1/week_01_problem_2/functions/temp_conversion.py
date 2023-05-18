#IT 410 - Eric Lovell - Functions for week 1 problem 2 - Temperature conversion 

#Function to convert fahrenheit to celcius
def fahrenheit_to_celcius(passed_float):
    """Converts a fahrenheit value to a celcius value
    Arguments:
        passed_float [Float value] -- Fahrenheit value that consists of a float
    Returns: 
        celcius [Float value] -- Returns the converted value"""
    
    celsius = (passed_float - 32) * 5 / 9

    return celsius


#Function to convert celsius to fahrenheit
def celsius_to_fahrenheit(passed_float):
    """Conerts a celsius value to a fahrenheit value
    Arguments:
        passed_float [Float value] -- Celsius value that consists of a float
    Returns:
        fahrenheit [Float Value] -- Returns the converted value"""

    fahrenheit = (passed_float * 9 / 5) + 32

    return fahrenheit
    
     