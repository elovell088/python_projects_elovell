#IT 410 - Eric Lovell - Chapter 4 Problems

#Problem 4-1

#Store favorite places to visit in a list 
my_favorite_places = ["Yosemite National Park", "Mackinac Island", "Cathedral Rock", "Glacier National Park"]
#Use a for loop to print out each item, also add phrase "is a nice place to visit" at the end
for place in my_favorite_places:
    print(place + " is a nice place to visit")


#Problem 4-2

#Use a for loop to print the numbers from 90 to 100 inclusive 
for number in range(90,101):
    print(number)


#Problem 4-3

#Create a list of numbers from 100_000 to 1_000_000
large_number_list = list(range(100_000, 1_000_001))
#Calculate and print out the sum of all of these numbers
print(sum(large_number_list))


#Problem 4-4

#Make a list of numbers and place them in random order 
random_numbers_list = [81, 34, 76, 5, 41, 38, 17, 98, 136, 4, 62, 39, 53, 11, 23, 174, 88, 93, 48, 15]
#Print out largest number in the list
print(max(random_numbers_list))
#Print out lowest number in the list
print(min(random_numbers_list))


#Problem 4-5

#Make a list of multiples of 5 between 1 and 100
multiples_of_five = []

#For loop to insert values into list
for numbers in range(1, 20):
    multiple = numbers * 5
    multiples_of_five.append(multiple)
#Print out list
print(multiples_of_five)


#Problem 4-6

#Generate list of values from 20 to 30
numbers_list = list(range(20, 31))
#Print out list
print(numbers_list)

#Use list comprehension to double the number each number in the list.
numbers_list = [value * 2 for value in numbers_list]
#Print out list of doubled values
print(numbers_list)


#Problem 4-7

#Use list generated in problem 4-4
random_numbers_list = [81, 34, 76, 5, 41, 38, 17, 98, 136, 4, 62, 39, 53, 11, 23, 174, 88, 93, 48, 15]
#Print the first 2 values in the list'
print("Printing first two values from list: " + str(random_numbers_list[0:2]))
#Print items 5-10 in the list
print("Printing items 5 - 10 from list: " + str(random_numbers_list[4:10]))
#Print the last 4 items in the list
print("Printing last four items from list: " + str(random_numbers_list[-4:]))


#Problem 4-8

#Make a list of 3 three of my favorite bands
my_favorite_bands = ["Kid Rock", "Kanye West", "Florida Georgia Line"]
#Copy list to another variable
copy_of_favorite_bands = my_favorite_bands[:]
#add a band to the original list
my_favorite_bands.append("Backstreet Boys")
#Print out both lists to show they are different lists
print(my_favorite_bands)

print(copy_of_favorite_bands)


#Problem 4-9

#Store grade values in a tuple
school_grades = (1, 2, 3, 4, 5)
#Attempt to modify tuple value using list syntax
school_grades[1] = 6

