#IT 410 - Eric Lovell - Looping over Lists Lecture Assignment#

#Declare list of strings
list_of_chores = ["Take Out Trash", "Wash Dishes", "Cut Grass", "Dust Coffee Table"]

#For loop to iterate through all items in list example
for chore in list_of_chores:
    chore = chore + " (10 minutes)"
    print(chore + " - Done!")

print("All chores are done!")

#Create a slice to target specific item in list example
for chore in list_of_chores[1:2]:
    chore = chore + " (10 minutes)"
    print(chore + " - Done!")

print("One chore is done!")

#Create slice to target multiple specified items in list example
for chore in list_of_chores[1:3]:
    chore = chore + " (10 minutes)"
    print(chore + " - Done!")

print("A few chores are done!")

