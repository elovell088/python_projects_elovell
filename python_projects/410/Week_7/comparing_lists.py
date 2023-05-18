#IT 410 - Eric Lovell - Comparing Lists Lecture Assignment#


#Creating lists to test examples
list1 = ["five", "six", "seven"]
list2 = ["five", "six", "seven"]

list3 = ["five", "six", "seven", "eight"]

list4 = ["five", "ape", "seven"]
list5 = ["five", "ape", "seven", "eight"]

num_list_1 = [1 , 2, 3]
num_list_2 = ["1", "2", "3"]

#Comparing lists that are the same example
if list1 == list2:
    print("The lists are the same.. Yay")

#Comparing lists that are not the same example - returns false
if list1 == list3:
    print("The lists are the SAME")

#Comparing lists of different data types example - returns false
if num_list_1 == num_list_2:
    print("These LISTS are the same")

#Print numerical and string list to see how output is different
print(num_list_1)
print(num_list_2)

#Example of how words earlier in the alphabet are less than words later in alphabet
# age < babe - returns true

#Comparing lists to see which is less example
if list1 < list3:
    print("List 1 is less than list 3")

#Comparing lists to see which if less or equal to example
if list1 <= list2:
    print("List 1 is less or equal to list 2")

#Example of how lists are determined to be greater than or less than on another
#Returns false because "ape"-a is earlier in the alphabet than two-t
if list1 < list4:
    print("Wow, this list is less.")

#Returns true because "two"-t in list1 comes after "ape"-a in the alphabet meaning it is greater than
if list1 > list4:
    print("Wow, List 1 this is greater than list 2.")

#Example of how list is still greater than list 4 even though list 4 has more values in it. 
if list1 > list5:
    print("Wow, List 1 is still greater than list 5 even though list 5 have more values in it.")

#Testing conditional statements on the number of items in two different lists example
if len(list5) > len(list1):
    print("list 5 has more values in it than list 1")