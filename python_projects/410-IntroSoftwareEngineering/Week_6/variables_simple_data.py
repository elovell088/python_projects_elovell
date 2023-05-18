#IT 410 - Eric Lovell - Variables and Simple Data Assignment#

#1.) Store my first name as a variable using lowercase
my_first_name = "eric"

#2.) Store my last name as a variable using uppercase
my_last_name = "LOVELL"

#3.) Print out "Hello, firstname + lastname" converting first to upper and last to lower -- 4.) Prints out two new lines
print("Hello, " + my_first_name.upper() + " " + my_last_name.lower() + "\n\n")

#5.) Print quote with quotations included in output
print("\"Start by doing what's necessary; then do what's possble; and suddenly you are doing the impossible - Francis of Assisi\"")

#6.) Store two decimal numbers as variables
decimal_number_one = 3.3

decimal_number_two = 4.4

#7.) Store one addition, subtraction, multiplication, divsion as variables using decimal variables
addition_result = decimal_number_one + decimal_number_two

subtraction_result = decimal_number_one - decimal_number_two

multiplication_result = decimal_number_one * decimal_number_two

division_result = decimal_number_one / decimal_number_two

#8.) Print out results of each equation showing "variable plus variable equals result"
print(str(decimal_number_one) + " plus " + str(decimal_number_two) + " equals " + str(addition_result))

print(str(decimal_number_one) + " minus " + str(decimal_number_two) + " equals " + str(subtraction_result))

print(str(decimal_number_one) + " multipled by " + str(decimal_number_two) + " equals " + str(multiplication_result))

print(str(decimal_number_one) + " divided by " + str(decimal_number_two) + " equals " + str(division_result))

#9.) Store current month as string and day as numeric
current_month = "November"

current_day = 10

#10.) Outputs "Today is day <variable> of the month of <month>" newline and tabbed twice
print("\n\t\tToday is day " + str(current_day) + " of the month of " + current_month + ".")
