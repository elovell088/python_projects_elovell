#IT 410 - Eric Lovell - Working With Lists Assignment


#1.) Create a list of all courses I have taken at walsh - lowercase 
my_completed_walsh_courses = ["statistical methods for business", "business communication methods", "professional communication", 
"systems analysis and design", "networks and operating systems", "database design and development", "server virtualization"]

#2.) Sort list and print each element with message - "I have taken course at Walsh college" - course is all uppercase
my_completed_walsh_courses.sort()

for course in my_completed_walsh_courses:
    print("I have taken " + course.upper() + " at Walsh College.")

#3.) Add courses that I plan to take next term and re-sort
my_completed_walsh_courses.append("advanced programming")

my_completed_walsh_courses.append("digital and network forensics")

my_completed_walsh_courses.append("security op and awareness")

my_completed_walsh_courses.sort()

#Print out each element in list - add message before print - The is my course of study with upcoming courses added
print("This is my course of study with upcoming courses added:")

for course in my_completed_walsh_courses:
    print(course)

#4.) Remove any course you have taken already from the list ane print each course removed add message "I do not have to take"
print("I do not have to take these courses:")

print(my_completed_walsh_courses.pop(1))

print(my_completed_walsh_courses.pop(1))

print(my_completed_walsh_courses.pop(2))

print(my_completed_walsh_courses.pop(2))

print(my_completed_walsh_courses.pop(3))

print(my_completed_walsh_courses.pop(3))

print(my_completed_walsh_courses.pop(3))

#5.) Print out each item left on list on its own line print I play to take the following courses next term
print("I plan to take the following courses next term")

print(my_completed_walsh_courses)

#6.) Create a list of numbers from 1 to 1000 that are divisble by 6
divisible_by_six = list(range(6, 1000, 6))

print(divisible_by_six)

#7.) Print out the first 20 numbers in list and print message above "Here are twenty numbers divisible by 6"
print("Here are twenty numbers divisible by 6.")

print(divisible_by_six[0:20])

#8.) Calculate the maximum number of the original list and store in a variable
max_number_divisible_six = max(divisible_by_six)

#9.) Print max number with message "The maximum value in the list is: "
print("The maximum value in the list is: " + str(max_number_divisible_six))

#10.) Calculate sum of values between the 10th value and 50th - store as variable - print with message "Here is the sum"
sum_of_values = sum(divisible_by_six[9:50])

print("Here is the sum of several values in the list: " + str(sum_of_values))

#11.) Overwrite variable that originally contained list of courses with the large number list from requirement 6
my_completed_walsh_courses = divisible_by_six

