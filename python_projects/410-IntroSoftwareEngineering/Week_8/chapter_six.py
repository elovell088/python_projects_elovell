#IT 410 - Eric Lovell - Chapter 6 problems#


#Problem 6-1

#Use dictionary to store information about my favorite movie.
my_favorite_movie = {} 
 
my_favorite_movie['title'] = "wolf of wall street"
my_favorite_movie['rating'] = "r"
my_favorite_movie['director'] = "Martin Scorcese"
my_favorite_movie['year_released'] = "2013"
my_favorite_movie['lead_actor'] = "leonardo dicaprio"
my_favorite_movie['production_company'] = "paramount pictures"



#Problem 6-2

my_product = {'item_number' : '1001', 'product_name' : 'head phones', 'product_price' : 89.99}
#Take current price and increase by 30%
my_product['product_price'] += (my_product['product_price'] * .30)
#Print a message that the price of the item has been increased by 30% - include name
print("The price of " + str(my_product['product_name']) + " has increased by 30 percent -- New price: $" + str(my_product['product_price']))



#Problem 6-3

#Use dictionary from 6-1 and print out all the keys and values using a loop
for key, value in my_favorite_movie.items():
    print("Key: " + key.title())
    print("Value: " + value.title() + "\n")



#Problem 6-4

#Create a list of three of more dictionary items. Each dictionary item should contain a word and it's definition. 
#Create two lists - one containing names and the other containing definitions 
words_and_definitions = [{'word' : 'control', 'definition' : 'the power to influence or direct peoples behavior or the course of events'},
                         {'word' : 'power', 'definition' : 'the capacity or ability to direct or influence the behavior of others or course of events'},
                         {'word' : 'subvert', 'definition' : 'to undermine the power and authority of an estabilished system or institution'}]

#Neatly print out word/definition pair using for loop
count_index = 0
output_string = ""

for words in words_and_definitions:
    output_string = output_string + "Word Index: " + str(count_index)
    output_string = output_string + " | Word: " + words["word"].title()
    output_string = output_string + " | Definition: " + words["definition"] + "\n"

    count_index = count_index + 1

print(output_string)



#Problem 6-5

#Start with the dictionary created for problem 6-1. Add a key to it that stores a list of other actors/
my_favorite_movie['co_stars'] = ['jonah hill', 'jon bernthal', 'margot robbie', 'cristin milioti']

for star in my_favorite_movie['co_stars']:
    print(star.title())




