#IT 412 - Eric Lovell - Final Project Modify Database Class
import os.path
import time
import json
from classes.customer import Customer
from classes.database_access import DB_Connect
from classes.inputs import Inputs
from classes.crm_database import crmDatabase
from classes.mailing_database import mailingDatabase
from classes.setup import Setup
from classes.reformat import Reformat

#Create instance of classes
user_input = Inputs()
get_crm_queries = crmDatabase()
get_mailing_queries = mailingDatabase()
setup = Setup()
format = Reformat()
connect_to_database = DB_Connect('root', '', 'python_projects')

class ModifyDatabase:
    """Class that holds methods to modify database"""

    def __init__(self):
        """Constructor for the ModifyDatabase class"""

    def addRecord(self):
        """Method that adds a record to the database
        Arguments: 
            None -- Creates instance of customer class and calls input methods
        Returns:
            None -- Adds the validated input into database"""
    
        new_customer = self.getCustomerInfo()
        
        crm_query = get_crm_queries.generateInsertCRMQuery(new_customer)
        mailing_query = get_mailing_queries.generateInsertMailQuery(new_customer)

        connect_to_database.executeQuery(crm_query)
        connect_to_database.executeQuery(mailing_query)
        connect_to_database.conn.commit()
        
        new_json_data = format.customerJSON(new_customer)
        
        with open("text_files/customers.json") as json_obj:
            customer_data = json.load(json_obj)
        
        customer_data.append(new_json_data)

        with open("text_files/customers.json", "w") as json_obj:
            json.dump(customer_data, json_obj)

        
        setup.update_configs()
        setup.clearScreen()

        print("**NEW CUSTOMER - " + new_customer.f_name + " " + new_customer.l_name + " has been added to the CRM and Mailing Database.**\n\n")


    def backup_data(self):
        """Function that back ups the previous JSON configurations to a backup file
        Arguments:
            None -- Backs up data directly to backup_files directory
        Returns:
            None -- Saves contents to new backup file and prints message that configurations were saved"""

        crm_backup_data = connect_to_database.executeSelectQuery("SELECT * FROM crm_data")
        mail_backup_data = connect_to_database.executeSelectQuery("SELECT * FROM Mailings")

        crm_backup_file = "backup_files/crm_backup_" + str(time.time())
        mail_backup_file = "backup_files/mail_backup_" + str(time.time())
    
        with open(crm_backup_file, "w") as json_obj:
            json.dump(crm_backup_data, json_obj)
            print("Previous CRM database entries backed up to: " + crm_backup_file + "\n")
        
        with open(mail_backup_file, "w") as json_obj:
            json.dump(mail_backup_data, json_obj)
            print("Previous Mailing database entries backed up to: " + mail_backup_file + "\n")



    def editRecord(self):
        """Method that asks user to modify or remove a record
        Arguments:
            None -- Input statement collects necessary information then sends to removeEntry() method or getUpdateQueries() Method
        Returns:
            None -- Calls either removeEntry() Method or getUpdateQueries() method"""
        
        print("\n| 1. Modify Record | 2. Remove Record |\n")
        selected_prompt = input("Please choose from the prompts above. Enter number: ")

        if selected_prompt == '2':
            self.removeEntry()
        
        elif selected_prompt == '1':
            selected_database = input("Which database? |1.) crm_data |2.) Mailings|: ")
            if selected_database == '1':
                self.getCRMUpdateQueries()
            
            elif selected_database == '2':
                self.getUpdateMailQueries()
            
        
        else:
            print("Sorry, you entered an invalid character. Please try again. ")



    def findRecord(self, passed_id):
        """Method that determines if a specific crm_id is in the CRM Database
        Arguments:
            passed_id {Integer Value} -- Integer value that contains CRM ID to search for in database
        Returns:
            [True] -- If vehicle is found in the database | [False] -- if vehicle is NOT found in the database"""

        search_query = connect_to_database.executeSelectQuery("SELECT * FROM crm_data")

        entry_found = False
        for record in search_query:
            if record["crm_id"] == passed_id:
                entry_found = True
                break
        
        if entry_found:
            return True
        else:
            return False
    
    
    
    def findMailingRecord(self, passed_id):
        """Method that determines if a specific mail id is found in the Mailing Database
        Arguments:
            passed_id {Integer Value} -- Integer value that contains CRM ID to search for in database
        Returns:
            [True] -- If vehicle is found in the database | [False] -- if vehicle is NOT found in the database"""
        
        search_query = connect_to_database.executeSelectQuery("SELECT * FROM Mailings")

        entry_found = False
        for record in search_query:
            if record["mail_id"] == passed_id:
                entry_found = True
                break
        
        if entry_found:
            return True
        else:
            return False
        


    def getCSV(self, passed_file):
        """Method that gathers information and sends to a method for csv file generation
        Arguments:
            passed_file {Text File} -- Text File containing values to input into csv file
        Returns:
            None -- checks to see if specific file exists then sends data to Reformat Class methods"""
        
        original_file = "text_files/customers.csv"
        backup_file = "backup_files/customers.csv_Backup_" + str(time.time())

        csv_data = format.dataForCSV(passed_file)

        if os.path.isfile(original_file):
            format.reformatCSV(backup_file, csv_data)
        else: 
            format.reformatCSV(original_file, csv_data)
        

    def getCustomerInfo(self):
        """Method that consists of input statements to collect necessary information to instantiate Customer() Class
        Arguments:
            None -- All information is gather by input statements within method
        Returns:
            customer_info {Customer Object} -- Instance of Customer() Class"""
        
        f_name = user_input.getFirstName()
        setup.clearScreen()
        l_name = user_input.getLastName()
        setup.clearScreen()
        address = user_input.getStreetAddress()
        setup.clearScreen()
        city = user_input.getCity()
        setup.clearScreen()
        state = user_input.getState()
        setup.clearScreen()
        zip = user_input.getZip()
        setup.clearScreen()
        company = user_input.getCompanyName()
        setup.clearScreen()
        primary_phone = user_input.getPhoneNumber()
        setup.clearScreen()
        secondary_phone = user_input.getSecPhone()
        setup.clearScreen()
        email_address = user_input.getEmail()
        setup.clearScreen()
        
        customer_info = Customer(f_name, l_name, address, city, state, zip, primary_phone, company, secondary_phone, email_address)

        return customer_info
    
    
    def getCRMUpdateQueries(self):
        """Method that gathers necessary information from user then sends to proper update method
        Arguments:
            None -- All necessary information at this step is gathered with input statements within method
        Returns:
            None -- Sends information to specific update method"""
        
        selected_customer = input("Please enter the CRM ID of the customer you would like to modify: ")
        customer_found = self.findRecord(int(selected_customer))
        setup.clearScreen()
        #If the customer is found, display the values and ask user which one they would like to edit. 
        if customer_found:
            get_crm_queries.displayCustomer(selected_customer)
            changes_complete = False
            while not changes_complete:
                user_choice = input("\nEnter the number of the attribute you would like to modify (Enter 'x' to return to Main Menu): ")
                setup.clearScreen()
                #Option 1 - Update First Name
                if user_choice == '1':
                    get_crm_queries.updateFirstName(selected_customer)
                #Option 2 - Update Last Name
                elif user_choice == '2':
                    get_crm_queries.updateLastName(selected_customer)
                #Option 3 - Update Address
                elif user_choice == '3':
                    get_crm_queries.updateAddress(selected_customer)
                #Option 4 - Update City
                elif user_choice == '4':
                    get_crm_queries.updateCity(selected_customer)
                #Option 5 - Update State
                elif user_choice == '5':
                    get_crm_queries.updateState(selected_customer)
                #Option 6 - Update Zip
                elif user_choice == '6':
                    get_crm_queries.updateZip(selected_customer)
                #Option 7 - Update Company
                elif user_choice == '7':
                    get_crm_queries.updateCompany(selected_customer)
                #Option 8 - Update Primary Phone
                elif user_choice == '8':
                    get_crm_queries.updatePrimaryPhone(selected_customer)
                #Option 9 - Update Secondary Phone
                elif user_choice == '9':
                    get_crm_queries.updateSecondaryPhone(selected_customer)
                #Option 10 - Update Email Address
                elif user_choice == '10':
                    get_crm_queries.updateEmailAddress(selected_customer)
                #Option 11 - Terminate program                  
                elif user_choice == 'x':
                    changes_complete = True
                else:
                    #Catch all for invalid input character
                    print("Sorry, you entered and invalid character. Please try again..\n")
        
        else:
            print("Sorry, CRM ID: " + selected_customer + " does not exist in the database. Please try again..")



    def getDatabase(self):
        """Method that displays all entries within the database in a clean format
        Arguments:
            None -- Input statements within method determine what datebase to display and calls proper methods
        Returns:
            None -- Prints information within the selected database"""
        print("Choose Database to display:")
        print("\n| 1. CRM Database | 2. Mailings Database |\n")
        selected_database = input("Please choose from the prompts above. Enter the number: ")

        if selected_database == '1':
            crm_db = get_crm_queries.getCRMDatabase()
            print(crm_db)

        elif selected_database == '2':
            mail_db = get_mailing_queries.getMailingDatabase()
            print(mail_db)            
        else:
            print("Sorry, you entered and invalid character.\n")



    def getJSON(self, passed_file):
        """Method that gathers information and sends to a method for json file generation
        Arguments:
            passed_file {Text File} -- Text File containing values to input into json file
        Returns:
            None -- checks to see if specific file exists then sends data to Reformat Class methods"""
        
        original_file = "text_files/customers.json"
        backup_file = "backup_files/customer.json_backup_" + str(time.time())

        json_data = format.dataForJSON(passed_file)

        if os.path.isfile(original_file):
            with open(original_file) as json_obj:
                old_data = json.load(json_obj)
                        
            format.reformatJSON(backup_file, old_data)
            format.reformatJSON(original_file, json_data)

        else: 
            format.reformatJSON(original_file, json_data)



    def getUpdateMailQueries(self):
        """Method that gathers necessary information from user for Mailing database then sends to proper update method
        Arguments:
            None -- All necessary information at this step is gathered with input statements within method
        Returns:
            None -- Sends information to specific update method"""
        
        selected_customer = input("Please enter the Mail ID of the customer you would like to modify: ")
        customer_found = self.findMailingRecord(int(selected_customer))
        
        #If the customer is found, display the values and ask user which one they would like to edit. 
        if customer_found:
            print("Found")
            get_mailing_queries.displayMailing(selected_customer)
            changes_complete = False
            while not changes_complete:
                user_choice = input("\nEnter the number of the attribute you would like to modify (Enter 'x' to return to Main Menu): ")
                #Option 1 - Update First Name
                if user_choice == '1':
                    get_mailing_queries.updateFullName(selected_customer)
                #Option 2 - Update Last Name
                elif user_choice == '2':
                    get_mailing_queries.updateCompany(selected_customer)
                #Option 3 - Update Address
                elif user_choice == '3':
                    get_mailing_queries.updateAddress(selected_customer)
                #Option 11 - Terminate program                  
                elif user_choice == 'x':
                    changes_complete = True
                    
                else:
                    #Catch all for invalid input character
                    print("Sorry, you entered and invalid character. Please try again..\n")
                    
        else:
            print("\n**Sorry, the CRM ID "+ selected_customer + " does not exist in the database..")



    def importData(self, passed_file):
        """Method that takes a text file and imports all the information into both databases, holds methods to create csv and json files
        Arguments:
            passed_file {Text File} -- Text file that holds values to input into database
        Returns:
            None -- Directly imports information from text file into both databases"""
        
        self.getCSV(passed_file)
        self.getJSON(passed_file)
        self.backup_data()
        self.removeDatabase()
        setup.reset_configs()
        customer_data = format.dataForJSON(passed_file)
        list_index = 1
        while list_index < len(customer_data):
            for key, value in customer_data[list_index].items():
                if key == 'f_name':
                    f_name = value
                elif key == 'l_name':
                    l_name = value
                elif key == 'address':
                    address = value
                elif key == 'city':
                    city = value
                elif key == 'state':
                    state = value
                elif key == 'zip':
                    zip = value
                elif key == 'company':
                    company = value
                elif key == 'primary_phone':
                    primary_phone = value
                elif key == 'secondary_phone':
                    secondary_phone = value
                elif key == 'email_address':
                    email_address= value
                
            new_customer = Customer(f_name, l_name, address, city, state, zip, primary_phone, company, secondary_phone, email_address)
            
            #Generate Queries   
            crm_query = get_crm_queries.generateInsertCRMQuery(new_customer)
            mailing_query = get_mailing_queries.generateInsertMailQuery(new_customer)

            #Execute insert query for the required fields in the database entry
            connect_to_database.executeQuery(crm_query)  
            connect_to_database.executeQuery(mailing_query)
            connect_to_database.conn.commit()
            
            setup.update_configs()
            list_index += 1

        print("*Data has been imported into the CRM and Mailing Database.")
        print("*New file created: 'text_files/customers.json")
        print("*New file created: 'text_files/customers.csv\n\n")




    def removeDatabase(self):
        """Method that removes all information from both databases
        Arguments:
            None -- Directly removes information from both databases
        Returns:
            None -- Directly removes information from both databases"""
        
        connect_to_database.executeQuery("DELETE FROM crm_data")
        connect_to_database.executeQuery("DELETE FROM Mailings")
        connect_to_database.conn.commit()
        setup.update_configs()



    def removeEntry(self):
        """Method that removes customer from the CRM and Mailing database
        Arguments:
            None -- Removes customer from both databases
        Returns:
            None -- Removes customer from both databases"""

        selected_entry = input("Enter CRM ID: ")
        entry_found = self.findRecord(int(selected_entry))

        if entry_found:
            setup.clearScreen()
            mail_id = get_mailing_queries.getMailID(selected_entry)
            get_crm_queries.displayCustomer(selected_entry)
            user_warning = input("Are you sure you? (Y/N) *This will permanently erase the customer from all databases: ")
            user_warning = user_warning.lower()
            
            if user_warning == 'y':
                setup.clearScreen()
                format.removeJSON("text_files/customers.json", selected_entry)
                connect_to_database.executeQuery("DELETE FROM crm_data WHERE crm_id='" + selected_entry + "'")
                connect_to_database.executeQuery("DELETE FROM Mailings WHERE mail_id='" + str(mail_id) + "'")
                connect_to_database.conn.commit()

                print("\n" + selected_entry + " has been removed from the CRM database.\n")
                print("\n" + str(mail_id) + " has been removed from the Mailings database.\n")
                
        
        