#IT 410 - Eric Lovell - User Input Demonstration Lecture Assignment#

#Basic input example
area_code = input("Please enter your area code: ")

print("Your area code is: " + area_code)


#Introducing blank value checks example
if area_code:
    print("Your area code is: " + area_code)
else:
    print("You did not enter an area code.")


#Introducing type check example
if area_code:
    try:
        int(area_code)
        print("Your area code is: " + area_code)
    except:
        print("You did not enter a valid area code.")
    

#Length of value check example
if area_code:
    try:
        int(area_code)
        if len(area_code)== 3:
            print("Your area code is: " + area_code)
        
        else:
            print("Your inputted area code isn't long enough")

    except:
        print("You did not enter a valid area code.")

else:
        print("You did not enter an area code.")





