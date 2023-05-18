#IT 410 - Eric Lovell - Working with Dictionaries Lecture Assignment# 

#Declare a simple dictionary example
pizza_preferences = {}

pizza_preferences['name'] = "sandeep"
pizza_preferences['toppings'] = "mushrooms"

print(pizza_preferences)


#Declare a simple dictionary using inline method example
pizza_inline_method = {'name' : 'sandeep', 'toppings' : 'mushrooms'}

print(pizza_inline_method)


#Make list out of dictionaries, lists within dictionaries example
pizza_list_dictionary = [{'name' : 'sandeep', 'toppings' : 'mushrooms', 'pizza_type' : 'round'},
                         {'name' : 'benny', 'toppings' : ['pepperoni', 'sausage'], 'pizza_type' : 'sqaure'},
                         {'name' : 'jim', 'toppings' : 'sausage', 'pizza_type' : 'deep dish'},
                         {'name' : 'bart', 'toppings' : ['anchovies','spinach', 'mushrooms'], 'pizza_type' : 'thin crust'}]

print(pizza_list_dictionary)


#How to search for specific key pair value
for person in pizza_list_dictionary:
    if person['name'] == "sandeep":
        print(person['toppings'])
    else:
        print("This is not sandeep")


#Using bool variable search for values in dictionary
for person in pizza_list_dictionary:
    
    mushrooms_found = False

    if type(person['toppings']) is str:
        if(person['toppings']) == "mushrooms":
            mushrooms_found = True
    
    elif type(person['toppings']) is list:
        if("mushrooms" in person['toppings']):
            mushrooms_found = True

    if mushrooms_found:
         print(person['name'] + " likes mushrooms")


#remove a value from a dictionary 
print(pizza_list_dictionary)

for person in pizza_list_dictionary:
    
    mushrooms_found = False

    if type(person['toppings']) is str:
        if(person['toppings']) == "sausage":
            mushrooms_found = True
    
    elif type(person['toppings']) is list:
        if("sausage" in person['toppings']):
            mushrooms_found = True

    if mushrooms_found:
         pizza_list_dictionary.remove(person)

print(pizza_list_dictionary)



