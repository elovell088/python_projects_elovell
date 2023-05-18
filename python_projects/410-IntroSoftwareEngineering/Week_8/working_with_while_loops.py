#IT 410 - Eric Lovell - Working with While Loops Lecture Assignment#

#Nested while loop example 
program_running = True

#Append numbers to this list
phone_numbers = []
print()

while program_running:

    area_code = input("Please enter your area code: ")

    area_code_ok = False
    
    while not area_code_ok:
        if area_code:
            try:
                int(area_code)
                if len(area_code)== 3:
                    print("Your area code is: " + area_code)
                    area_code_ok = True
                else:
                    area_code_ok = False

            except:
                area_code_ok = False
        
        else:
            area_code_ok = False

        if not area_code_ok:
            
            area_code = input("Area Code was not properly formatted. Please try again: ")
    
    #end area code processing
    #begin processing first part of phone number
    phone_first_part = input("Please enter the first three digits of your phone number: ")

    phone_first_ok = False
    
    while not phone_first_ok:
        if phone_first_part:
            try:
                int(phone_first_part)
                if len(phone_first_part)== 3:
                    print("The first part of your phone number: " + phone_first_part)
                    phone_first_ok = True
                else:
                    phone_first_ok = False

            except:
                phone_first_ok = False
        
        else:
            phone_first_ok = False
 
        if not phone_first_ok:
            
            phone_first_part = input("First part of phone number was not properly formatted. Please try again: ")


    #End first part of phone number processing
    #Begin processing last part of phone number
    phone_last_part = input("Please enter the last four digits of your phone number: ")

    last_part_ok = False
    
    while not last_part_ok:
        if phone_last_part:
            try:
                int(last_part_ok)
                if len(phone_last_part)== 4:
                    print("The first part of your phone number: " + phone_last_part)
                    last_part_ok = True
                else:
                    last_part_ok = False

            except:
                last_part_ok = False
        
        else:
            last_part_ok = False
 
        if not last_part_ok:
            
            phone_last_part = input("Last part of phone number was not properly formatted. Please try again: ")


    phone_numbers.append({'area_code' : area_code, 'first_part' : phone_first_part, 'last_part' : phone_last_part})

    add_another_number = input("Do you wish to add another phone number (Y or N)? ")

    if add_another_number == "N":
        break
    else: 
        continue

print(phone_numbers)
