#IT 410 - Eric Lovell - Working with numeric lists and ranges lecture assignment#

#Create a numeric list with range() method
numbers = list(range(1,11))

print(numbers) 

#Iterate through numerica list to output every other number
odd_numbers = list(range(1,11,2))

print(odd_numbers)

#Create for loop to divide every 945 by every other number in list
numbers_example = list(range(1,11,2))

for number in numbers_example:
    print(945/number)

#Print the minimum number in list example
print(min(numbers))

#Print the maximum number in list example
print(max(numbers))

#Print the summ of all the number in a list example
print(sum(numbers))

