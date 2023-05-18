#IT 410 - Eric Lovell - Problem 2 - Main 3#

from functions.temp_conversion import fahrenheit_to_celcius as f
from functions.temp_conversion import celsius_to_fahrenheit as c
#Ask user which type of conversion they would like to perform
conversion_method = input("Which value would you like to convert? - Fahrenheit (F) or Celsius (C): ")
conversion_method = conversion_method.lower()
#If statement for conversion of fahrenheit to celsius
if conversion_method == 'f':
    fahrenheit = input("Please enter fahrenheit value: ")
    fahrenheit = float(fahrenheit)

    converted_value = f(fahrenheit)
    print("Conversion: "+ str(converted_value) + " degrees celsius")
#If statement for conversion of celsius to fahrenheit
elif conversion_method == 'c':
    celsius = input("Please enter celsius value: ")
    celsius = float(celsius)

    converted_value = c(celsius)
    print("Conversion: "+ str(converted_value) + " degrees fahrenheit")
#Catch all if user enters invalid entry
else:
    print("You entered an invalid value. ")
