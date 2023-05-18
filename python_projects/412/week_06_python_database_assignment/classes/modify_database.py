#IT 412 - Eric Lovell - Modification Class for Week 6-7 Python Database Assignment

#Imports
from classes.database_access import DB_Connect
from classes.validator import Validator

#Instances {Vehicle Database Connection, Input Validator}
vehicle_database = DB_Connect('root', '', 'python_projects')
input_validator = Validator()

class ModifyDatabase():
    """Class containing methods to validate user input, provide prompts, and modify a database"""

    def __init__(self):
        """Constructor for the ModifyDatabase class"""
    

    def addVehicle(self):
        """Method that adds a new vehicle to the database
        Arguments:
            None 
        Returns:
            None -- Adds new vehicle to the database"""

        #REQUIRED
        vin = self.getVin()
        make = self.getMake()
        model = self.getModel()
        sales_price = self.getSalesPrice()
        description = self.getDescription()
        #Create variable to hold the insert and value portions of the query string
        insert_string = "INSERT INTO vehicle_info (vehicle_vin, vehicle_make, vehicle_model, vehicle_sales_price, vehicle_description)"
        value_string = " VALUES ('" + vin + "', '" + make + "', '" + model + "', '" + sales_price + "', '" + description +"')"
        query_string = insert_string + value_string
        #Execute insert query for the required fields in the database entry
        vehicle_database.executeQuery(query_string)
        vehicle_database.conn.commit()

        #OPTIONAL FIELDS
        #Previous owner input statement asking if user would like to enter the previous owner of the vehicle
        previous_owner = input("Would you like to enter the name of the previous owner?(Y/N): ")
        previous_owner = previous_owner.lower()
        if previous_owner == 'y':
            previous_owner = self.getName()
            #Update statement to update the previous owner field from null to a validated value
            vehicle_database.executeQuery("UPDATE vehicle_info SET previous_owner='" + previous_owner + "' WHERE vehicle_vin='" + vin + "'")
            vehicle_database.conn.commit()
        #Price paid input statement asking the user if they would like to enter the price paid for the vehicle
        price_paid = input("Would you like to enter the price paid for the vehicle?(Y/N): ")
        price_paid = price_paid.lower()
        if price_paid == 'y':
            price_paid = self.getPricePaid()
            #Update statement to update the price paid field from null to a validated value
            vehicle_database.executeQuery("UPDATE vehicle_info SET price_paid='" + price_paid + "' WHERE vehicle_vin='" + vin + "'")
            vehicle_database.conn.commit()


    def display_vehicle(self, passed_vin):
        """Displays an individual vehicles information
        Arguments:
            None
        Returns:
            None -- Directly prints vehicle information to the console"""

        #Select entry where the VIN equals the selected value. Put into variable.
        query_result = vehicle_database.executeSelectQuery("SELECT * FROM vehicle_info Where vehicle_vin='" + passed_vin + "'")
        print("\nVehicle Information:\n")
        for record in query_result:
            print("1. VIN Number: " + record["vehicle_vin"])
            print("2. Make: " + record["vehicle_make"])
            print("3. Model: " + record["vehicle_model"])
            print("4. Sales Price: " + record["vehicle_sales_price"])
            print("5. Description: " + record["vehicle_description"])
            try:
                print("6. Previous Owner: " + record["previous_owner"])
            except:
                print("6. Previous Owner: None")
            try:  
                print("7. Price Paid: " + record["price_paid"])
            except:
                print("7. Price Paid: None")


    def editVehicle(self):
        """Method that allows the user to modify vehicle values within the database
        Arguments:
            None -- User will be prompted to enter VIN information within the method
        Returns:
            None -- Updates entries in the database"""
        
        #Determine if the entered VIN number is in the database
        selected_vehicle = self.getVin()
        vehicle_found = self.findVehicle(selected_vehicle)
        
        #If the vechile is found, display the values and ask user which one they would like to edit. 
        if vehicle_found:
            self.display_vehicle(selected_vehicle)
            changes_complete = False
            while not changes_complete:
                user_choice = input("\nEnter the number of the attribute you would like to modify (Enter 'x' to return to Main Menu): ")
                #Option 1 - Update VIN Number
                if user_choice == '1':
                    new_vin = self.getVin()
                    vehicle_database.executeQuery("UPDATE vehicle_info SET vehicle_vin='" + new_vin + "' WHERE vehicle_vin='" + selected_vehicle + "'")
                    vehicle_database.conn.commit()
                    self.display_vehicle(selected_vehicle)
                #Option 2 - Update Make
                elif user_choice == '2':
                    new_make = self.getMake()
                    vehicle_database.executeQuery("UPDATE vehicle_info SET vehicle_make='" + new_make + "' WHERE vehicle_vin='" + selected_vehicle + "'")
                    vehicle_database.conn.commit()
                    self.display_vehicle(selected_vehicle)
                #Option 3 - Update Model
                elif user_choice == '3':
                    new_model = self.getModel()
                    vehicle_database.executeQuery("UPDATE vehicle_info SET vehicle_model='" + new_model + "' WHERE vehicle_vin='" + selected_vehicle + "'")
                    vehicle_database.conn.commit()
                    self.display_vehicle(selected_vehicle)
                #Option 4 - Update Sales Price
                elif user_choice == '4':
                    new_price = self.getSalesPrice()
                    vehicle_database.executeQuery("UPDATE vehicle_info SET vehicle_sales_price='" + new_price + "' WHERE vehicle_vin='" + selected_vehicle + "'")
                    vehicle_database.conn.commit()
                    self.display_vehicle(selected_vehicle)
                #Option 5 - Update Description
                elif user_choice == '5':
                    new_desc = self.getDescription()
                    vehicle_database.executeQuery("UPDATE vehicle_info SET vehicle_description='" + new_desc + "' WHERE vehicle_vin='" + selected_vehicle + "'")
                    vehicle_database.conn.commit()
                    self.display_vehicle(selected_vehicle)
                #Option 6 - Update Previous Owner
                elif user_choice == '6':
                    new_name = self.getName()
                    vehicle_database.executeQuery("UPDATE vehicle_info SET previous_owner='" + new_name + "' WHERE vehicle_vin='" + selected_vehicle + "'")
                    vehicle_database.conn.commit()
                    self.display_vehicle(selected_vehicle)
                #Option 7 - Update Price paid
                elif user_choice == '7':
                    new_price = self.getPricePaid()
                    vehicle_database.executeQuery("UPDATE vehicle_info SET price_paid='" + new_price + "' WHERE vehicle_vin='" + selected_vehicle + "'")
                    vehicle_database.conn.commit()
                    self.display_vehicle(selected_vehicle)  
                #Option 8 - Terminate program                  
                elif user_choice == 'x':
                    changes_complete = True
                
                else:
                    #Catch all for invalid input character
                    print("Sorry, you entered and invalid character. Please try again..\n")
                
        else:
            print("\n**Sorry, the VIN number "+ selected_vehicle + " does not exist in the database..")


    def findVehicle(self, passed_vin):
        """Method that finds a vehicle from the database
        Arguments:
            passed_vin {String Value} -- String value that contains VIN number to search for in database
        Returns:
            [True] -- If vehicle is found in the database | [False] -- if vehicle is NOT found in the database"""
        #Put all values from database in a variable to work with
        search_query = vehicle_database.executeSelectQuery("SELECT * FROM vehicle_info")
        
        vehicle_found = False
        for record in search_query:
            if record["vehicle_vin"] == passed_vin:
                vehicle_found = True
                break

        if vehicle_found:
            return True
        else:
            return False
        

    def getDescription(self):
        """Gathers the description of a vehicle from the user and validates it
        Arguments:
            None -- Gathers information with input statements within the method
        Returns:
            ret_description {String Value} -- String value that contains validated vehicle description information"""

        ret_description = input("Please provide a decription of the vehicle: ")
        
        validate_description = False
        while not validate_description:
            validate_description = input_validator.validate_description(ret_description)

            if not validate_description:
                ret_description = input("Sorry, you entered an invalid character. Please try again: ")
                validate_description = input_validator.validate_description(ret_description)

        return ret_description


    def getMake(self):
        """Gathers the make of a vehicle from user and validates it
        Arguments:
            None -- Gathers information with input statements within the method
        Returns:
            ret_make {String Value} -- String value that contains validated vehicle make information"""

        ret_make = input("Please provide the make of the vehicle: ")
        
        validate_make = False
        while not validate_make:
            validate_make = input_validator.validate_make(ret_make)

            if not validate_make:
                ret_make = input("Sorry, you entered an invalid character. Please try again: ")
                validate_make = input_validator.validate_make(ret_make)

        return ret_make
        

    def getModel(self):
        """Gathers the model of a vehicle from user and validates it
        Arguments:
            None -- Gathers information with input statements located within the method
        Returns:
            ret_model {String Value} -- String value that contains validated vehicle model information"""
    
        ret_model = input("Please provide the model of the vehicle: ")
        
        validate_model = False
        while not validate_model:
            validate_model = input_validator.validate_model(ret_model)

            if not validate_model:
                ret_model = input("Sorry, you entered an invalid character. Please try again: ")
                validate_model = input_validator.validate_model(ret_model)

        return ret_model


    def getName(self):
        """Gathers the name of the person who sold the vehicle from user and validates it
        Arguments:
            None -- Gathers information with input statements within the method
        Returns:
            ret_name {String Value} -- String value that contains information related to the name of the person who sold the car"""

        ret_name = input("Please enter the name of the person(s) who sold the vehicle: ")

        if ret_name == '0':
            return ret_name
        else:
            validate_name = False
            while not validate_name:
                validate_name = input_validator.validate_name(ret_name)

                if not validate_name:
                    ret_name = input("Sorry, you entered an invalid character. Please try again: ")
                    validate_name = input_validator.validate_name(ret_name)

            return ret_name


    def getPricePaid(self):
        """Gathers the price paid for a vehicle from the user and validates it
        Arguments:
            None -- Gathers information with input statements within the method
        Returns:
            ret_price {String Value} -- String value that contains validated information for price paid for the vehicle"""

        ret_price = input("Please provide the purchase price of the vehicle(ex. 1000.00): $")
        
        if ret_price == '0':
            return ret_price
        else:
            validate_price = False
            while not validate_price:
                validate_price = input_validator.validate_price(ret_price)

                if not validate_price:
                    ret_price = input("Sorry, you entered an invalid character or format. Please try again: ")
                    validate_price = input_validator.validate_price(ret_price)

            return ret_price


    def getSalesPrice(self):
        """Gathers the sales price of a vehicle from user and validates it
        Arguments:
            None -- Gathers information with input statements within the method
        Returns:
            ret_price {String Value} -- String value that contains validated vehicle sales price information"""
    
        ret_price = input("Please provide the sales price of the vehicle(ex. 3000.00): $")
        
        validate_price = False
        while not validate_price:
            validate_price = input_validator.validate_price(ret_price)

            if not validate_price:
                ret_price = input("Sorry, you entered an invalid character or format. Please try again: ")
                validate_price = input_validator.validate_price(ret_price)

        return ret_price
    

    def getVin(self):
        """Gathers the VIN number of a vehicle from the user and validates it
        Arguments:
            None -- Gathers information with input statements within the method
        Returns:
            ret_description {String Value} -- String value that contains validated vehicle description information"""

        ret_vin = input("Please provide the vin number of the vehicle: ")
        
        validate_vin = False
        while not validate_vin:
            validate_vin = input_validator.validate_vin(ret_vin)

            if not validate_vin:
                ret_vin = input("Sorry, you entered an invalid character. Please try again: ")
                validate_vin = input_validator.validate_vin(ret_vin)

        return ret_vin
        

    def programPrompts(self):
        """Displays available prompts for user
        Arguments:
            None
        Returns:
            None -- Directly prints program prompts to the console"""

        output_string = ''
        output_string = output_string + "\n                        *Prompts*\n"
        output_string = output_string + "| 1. Show Vehicles   | 2. Add Vehicle  | 3. Edit Vehicle  |\n"
        output_string = output_string + "       | 4. Remove Vehicle  | 5. Exit Program  | \n"

        print(output_string)


    def removeVehicle(self):
        """Method that adds a new vehicle to the database
        Arguments:
            None 
        Returns:
            None -- Removes vehicle from the database"""

        selected_vehicle = self.getVin()
        vehicle_found = self.findVehicle(selected_vehicle)

        if vehicle_found:
            user_warning = input("Are you sure you? (Y/N) *This will permanently erase the vehicle from the database: ")
            user_warning = user_warning.lower()
            
            if user_warning == 'y':
                vehicle_database.executeQuery("DELETE FROM vehicle_info WHERE vehicle_vin='" + selected_vehicle + "'")
                vehicle_database.conn.commit()
                print("\n" + selected_vehicle + " has been removed from the vehicle database.\n")
                

    def showVehicles(self):
        """Method that displays all the vehicles within the database in a clean format
        Arguments:
            None
        Returns:
            None -- Directly prints vehicles along with their additional information"""
        
        show_vehicles = vehicle_database.executeSelectQuery("SELECT * FROM vehicle_info")

        print("\nVehicles")
        output_string = ""
        for vehicle in show_vehicles:
            output_string += "\nVin: " + vehicle['vehicle_vin'] + " | "
            output_string += "Make: " + vehicle['vehicle_make'] + " | "
            output_string += "Model: " + vehicle['vehicle_model'] + " | "
            output_string += "Sales Price: " + vehicle['vehicle_sales_price'] + " | "

            try:
                output_string += "Previous Owner: " + vehicle['previous_owner'] + " | "
            except:
                output_string += "Previous Owner: None | "
            try:
                output_string += "Price Paid: " + vehicle['price_paid'] + " |"
            except:
                output_string += "Price Paid: None |"
            
            output_string += "\nDescription: " + vehicle['vehicle_description'] + "\n"
        
        print(output_string)



    

        
        
