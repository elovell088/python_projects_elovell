#Testing RegEx
from functions.regex_functions import *
import pyperclip

# dateValid = False
# while not dateValid:
#     date = input("Please input the date: ")
#     dateValid = isValidDate(date)

#     if not dateValid:
#         date = input("Please input the date: ")
#         dateValid = isValidDate(date)

date_string = str(pyperclip.paste())
print(date_string)
#date_string = input("Please input some text: ")
my_dates = findAllDates(date_string)

print(my_dates)

output_string = ""
for date in my_dates:
    output_string = output_string + date + "\n"

pyperclip.copy(output_string)