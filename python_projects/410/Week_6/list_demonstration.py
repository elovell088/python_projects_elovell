#IT 410 - Eric Lovell - List Demonstration Lecture Assignment#

#Create a list of marvel movies example
favorite_marvel_movies = ["Avengers", "Thor:Ragnorak", "Captain America: Winter Soldier", "Guardians of the Galaxy"]

#Adding values to a list example
favorite_marvel_movies.append("Black Panther")

print(favorite_marvel_movies)

#DEL command example - removes by index
del favorite_marvel_movies [1]

print(favorite_marvel_movies)

#Remove command example - removes by value
favorite_marvel_movies.remove("Guardians of the Galaxy")

print(favorite_marvel_movies)

#Modifying values within a list example *Index values may change as items are being removed*
favorite_marvel_movies[1] = "Captain America: Civil War"

print (favorite_marvel_movies)

#Adding these values back to make a longer list for sort() and reverse() methods
favorite_marvel_movies.append("Guardians of the Galaxy")

favorite_marvel_movies.append("Thor:Ragnorak")

print(favorite_marvel_movies)

#Testing sort() method
favorite_marvel_movies.sort()

print(favorite_marvel_movies)

#Testing reverse() method
favorite_marvel_movies.reverse()

print(favorite_marvel_movies)

