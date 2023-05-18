#IT 410 - Eric Lovell - Complex Condition Statements Lecture Assignment#


#Create numeric list to test examples
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_number_list = []
even_number_list = []

#Create numeric list with duplicates to test nesting if statement example
duplicate_number_list = [1, 1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7, 8, 9, 9, 9, 10]
odd_no_duplicates = []
even_no_duplicates = []

#For loop to iterate through numeric list and determine which are odd and even via modulo example
for value in number_list:
    if value % 2 == 1:
        print(str(value) + " is odd")
    elif value % 2 == 0:
        print(str(value) + " is even")


#For loop to iterate through numeric list to determine even or odd and add values to the appropriate list example
for value in number_list:
    if value % 2 == 1:
        odd_number_list.append(value)
    elif value % 2 == 0:
        even_number_list.append(value)

#Print the lists to show appropriate numbers were added 
print("The list of odd numbers is..")
print(odd_number_list)
print("The list of even numbers is..")
print(even_number_list)

#Nesting if statements to return clean list with no duplicates example
for value in duplicate_number_list:
    if value not in odd_no_duplicates and value not in even_no_duplicates:
        if value % 2 == 1:
            odd_no_duplicates.append(value)
        elif value % 2 == 0:
            even_no_duplicates.append(value)

#Print list to show no duplicates have been added to list
print("The list of odd numbers with no duplicates is..")
print(odd_no_duplicates)
print("The list of even numbers with no duplicates is..")
print(even_no_duplicates)