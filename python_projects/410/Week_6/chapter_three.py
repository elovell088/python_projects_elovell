#IT 410 - Eric Lovell - Chapter 3 Problems#


#Problem 3-1

#Create a list of last 4 books I have read
last_four_books = ["the universal one", "the secret life of trees", "technological slavery", "the spirit molecule"]
#Print each book, out at a time, in title case , with the message "I just read in front of it" No loops
print("I just read: " + last_four_books[0].title())
print("I just read: " + last_four_books[1].title())
print("I just read: " + last_four_books[2].title())
print("I just read: " + last_four_books[3].title())


#Problem 3-2

#Make list of top 4 favorite tv shows
top_four_tv_shows = ["south park", "the white lotus", "stranger things", "invincible"]
#One got cancelled and replace it with a new show
top_four_tv_shows[1] = "the boys"
#Add two more shows, 1 must be added using append()
top_four_tv_shows.append("the flash")
#Add second show using the insert method. Cannot be added in the first or last position
top_four_tv_shows.insert(2, "bob's burgers")
#Remove last item from the list using pop() and print
popped_tv_show = top_four_tv_shows.pop()

print(popped_tv_show)
#Use a del statement to remove the first three shows then print whatever is left
del top_four_tv_shows[0:3]

print(top_four_tv_shows)


#Problem 3-3

#Store collection in variable
rocket_league_esports_teams = ["spacestation gaming", "dignitas", "optic gaming", "gen g", "faze clan"]
#Write a program that stores the following 4 methods
#Printing list using len function
print(len(rocket_league_esports_teams))
#Sorting list with the sort method 
rocket_league_esports_teams.sort()
#printing sorted list
print(rocket_league_esports_teams)
#Printing temporary sorted list with the sorted function
print(sorted(rocket_league_esports_teams))
#Performing reverse sort witih reverse method
rocket_league_esports_teams.reverse()
#printing reverse sorted list
print(rocket_league_esports_teams)


#Problem 3-4

#Write code that has indexing error
classmate_names = ["Andrew", "Salih", "Nick", "Devon", "Boban"]

del classmate_names[5]

print(classmate_names)
#Write code to fix and comment out
#del classmate_names[4]

#print(classmate_names)


