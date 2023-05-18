#IT 410 - Eric Lovell - Working with Conditions Assignment#


#1.) Create a single list that contains the following values
employee_information = [1121, "Jackie Grainger", 22.22, 1122, "Jignesh Thrakkar", 25.25, 1127, 
                        "Dion Green", 28.75, False, 24.32, 1132, "Jacob Gerber", "Sarah Sanderson", 
                        23.45, 1137, True, "Brandon Heck", 1138, 25.84, True, 1152, "David Toma", 
                        22.65, 23.75, 1157, "Charles King", False, "Jackie Grainger", 1121, 22.22, 
                        False, 22.65, 1152, "David Toma"]

#2.) Sort the data into three different lists
employee_numbers = []
employee_names = []
employee_salary = []
#For loop to iterate through employee information list
for value in employee_information:
#3.) Conditional statements to distribute values to appropriate list - NO DUPLICATES
    if type(value) is int and value not in employee_numbers:
        employee_numbers.append(value)
    
    elif type(value) is str and value not in employee_names:
        employee_names.append(value)
    
    elif type(value) is float and value not in employee_salary:
        employee_salary.append(value)


#4.)Mulitply each value in employee_salary by 1.3 and store in another list
#Create list for total hourly rate
total_hourly_rate = []
#For loop to mulitply each value in employee_salary and append to total_hourly_rate
for value in employee_salary:
    value_plus_benefits = value * 1.3
    total_hourly_rate.append(value_plus_benefits)
#Find max value in total_hourly_rate list. If over 37.30, print message about it being a budget concern.
highest_salary = max(total_hourly_rate)
if highest_salary > 37.30:
    print("The employee's total salary of " + str(highest_salary) + " may be a budget concern.")


#5.) Determine if anyones salary is between 28.15 and 30.65. Add to new list called underpaid salaries
#Create list
underpaid_salaries = []
#For loop to interate through total_hourly rate and condition statement to append values to new list
for value in total_hourly_rate:
    if value > 28.15 and value < 30.65:
        underpaid_salaries.append(value)


#6.) For each value the employee_salary list, calculate raise, and add to new list called company raises
company_raises = []
#For loop to iterate through list and conditional statements to calculate proper raise amount and add to new list.
for value in employee_salary:
    if value > 22 and value < 24:
        five_percent_raise = value + (value * .05)
        company_raises.append(five_percent_raise)
    
    elif value > 24 and value < 26:
        four_percent_raise = value + (value * .04)
        company_raises.append(four_percent_raise)
    
    elif value > 26 and value < 28:
        three_percent_raise = value + (value * .03)
        company_raises.append(three_percent_raise)
    
    else:
        two_percent_raise = value + (value * .02)
        company_raises.append(two_percent_raise)

        
#7.)Create my own complex condition using four tests, one line, comment behavior
user_name = "elovell"
user_id = "12345"
typed_password = "ilovecodinggg"
actual_password = "ilovecoding"
secret_question_result = "pizza"
email_authentication_pass = True
#Behavior involves someone logging into their account. Can log in with username or user id.
#If they type their password incorrectly, they have the option to pass two security authentications via secret question and email authentication

#if user_name equals elovell or 12345 and password does not equal ilovecoding and secret question equals pizza and user passes email authentication 
if(user_name == "elovell" or user_id == "12345") and (typed_password != actual_password) and (secret_question_result == "pizza" and email_authentication_pass == True ):
    print("Logging on user: elovell")



#Test Output
#print(employee_numbers)
#print(employee_names)
#print(employee_salary)
#print(total_hourly_rate)
#print(underpaid_salaries)
#print(company_raises)

