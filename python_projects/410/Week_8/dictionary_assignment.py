#IT 410 - Eric Lovell - Dictionary Assignment#

#--Employee Information List--#
employee_information = [1121, "Jackie Grainger", 22.22, 1122, "Jignesh Thrakkar", 25.25, 1127, 
                        "Dion Green", 28.75, False, 24.32, 1132, "Jacob Gerber", "Sarah Sanderson", 
                        23.45, 1137, True, "Brandon Heck", 1138, 25.84, True, 1152, "David Toma", 
                        22.65, 23.75, 1157, "Charles King", False, "Jackie Grainger", 1121, 22.22, 
                        False, 22.65, 1152, "David Toma"]

#--Employee Numbers, Employee Names, Emp[loyee Salary--#
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

#-- Total Hourly Rate--#
total_hourly_rate = []
#For loop to mulitply each value in employee_salary and append to total_hourly_rate
for value in employee_salary:
    value_plus_benefits = value * 1.3
    total_hourly_rate.append(value_plus_benefits)

#--COMPANY RAISES--#
company_raises = []
#For loop to iterate through list and conditional statements to calculate proper raise amount and add to new list.
for value in employee_salary:
    if value > 22 and value < 24:
        five_percent_raise = value + (value * .05)
        company_raises.append(five_percent_raise)
    
    elif value >= 24 and value <= 26:
        four_percent_raise = value + (value * .04)
        company_raises.append(four_percent_raise)
    
    elif value > 26 and value < 28:
        three_percent_raise = value + (value * .03)
        company_raises.append(three_percent_raise)
    
    else:
        two_percent_raise = value + (value * .02)
        company_raises.append(two_percent_raise)


#Start process to combine these lists into a list of dictionaries
#Create list to hold dictionaries
updated_employee_information = []
#Count index to iterate through various items 
count_index = 0
#Loop to create dictionaries and append to new list
for temp_number in employee_numbers:
    updated_employee_information.append({'number' : temp_number, 'name' : employee_names[count_index],
                                         'salary' : employee_salary[count_index], 'hourly_rate' : total_hourly_rate[count_index],
                                         'salary_plus_raise' : company_raises[count_index]})
    count_index = count_index + 1

#Loop for clean output
count_index = 0
output_string = ""
for item in updated_employee_information:
    output_string = output_string + "Employee Index: " + str(count_index)
    output_string = output_string + " | Number: " + str(item['number'])
    output_string = output_string + " | Name: " + item['name'].title()
    output_string = output_string + " | Base Salary: $" + str(item['salary'])
    output_string = output_string + " | Total Hourly Rate: $" + str(item['hourly_rate'])
    output_string = output_string + " | Salary Plus Raise: $" + str(item['salary_plus_raise']) + "\n"

    count_index = count_index + 1

print(output_string)
