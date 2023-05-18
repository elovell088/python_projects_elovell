from classes.database_access import DB_Connect
from classes.inputs import Inputs
from classes.setup import Setup
import json
#from classes.crm_database import crmDatabase

#Create instance of classes
#Mailings = DB_Connect('root', '', 'python_projects')
#crm_data = DB_Connect('root', '', 'python_projects')
user_input = Inputs()
setup = Setup()
connect_to_database = DB_Connect('root', '', 'python_projects')
#crm_info = crmDatabase()

class mailingDatabase():
    """Virtual representation of CRM database"""

    def __init__(self):
        """Constructor for the crmDatabase class"""

    def generateInsertMailQuery(self, passed_customer):
        """Method that generates an insert query for Mailing Database
        Arguments:
            passed_customer {Customer Object} -- Instance of customer class
        Returns:
            ret_query_string {String Value} -- String value constaing insert query statement for the Mailing Database"""
        
        insert_string = "INSERT INTO Mailings (mail_id, name, company, address"

        value_string = " VALUES ("
        value_string += "'" + passed_customer.mail_id + "',"
        value_string += "'" + passed_customer.f_name + " " + passed_customer.l_name + "',"

        if passed_customer.company:
            value_string += " '" + passed_customer.company + "',"
        else:
            value_string += "'" + passed_customer.f_name + " " + passed_customer.l_name + "',"

        value_string += " '" + passed_customer.address + ", " 
        value_string += passed_customer.city + ", "
        value_string += passed_customer.state + " "
        value_string += passed_customer.zip + "'"
        
        insert_string += ")"
        value_string += ")"
        ret_query_string = insert_string + value_string
        
        return ret_query_string
    

    def generateUpdateMailQuery(self):
        """Method that generates and executes an update query for Mailing Database
        Arguments:
            None -- collects input from user and sends it to the specified update method
        Returns:
            None -- Updates new values within the database and displays them to user"""
        
        selected_customer = input("Please enter the Mail ID of the customer you would like to modify: ")
        customer_found = self.findRecord(selected_customer)
        
        #If the customer is found, display the values and ask user which one they would like to edit. 
        if customer_found:
            self.getCustomerMailing(selected_customer)
            changes_complete = False
            while not changes_complete:
                user_choice = input("\nEnter the number of the attribute you would like to modify (Enter 'x' to return to Main Menu): ")
                #Option 1 - Update First Name
                if user_choice == '1':
                    self.updateFirstName()
                #Option 2 - Update Last Name
                elif user_choice == '2':
                    self.updateLastName()
                #Option 3 - Update Address
                elif user_choice == '3':
                    self.updateAddress()
                #Option 4 - Update City
                elif user_choice == '4':
                    self.updateCity()
                #Option 5 - Update State
                elif user_choice == '5':
                    self.updateState()
                #Option 6 - Update Zip
                elif user_choice == '6':
                    self.updateZip()
                #Option 7 - Update Company
                elif user_choice == '7':
                    self.updateCompany()
                #Option 11 - Terminate program                  
                elif user_choice == 'x':
                    changes_complete = True
                    
                else:
                    #Catch all for invalid input character
                    print("Sorry, you entered and invalid character. Please try again..\n")
                    
        else:
            print("\n**Sorry, the CRM ID "+ selected_customer + " does not exist in the database..")

    

    def displayMailing(self, passed_id):
        """Displays an individual customers information from Mailing Database
        Arguments:
            passed_id {String Value} -- String value containing mail id information
        Returns:
            None -- Directly prints customer information from Mailing Database"""

        #Select entry where the VIN equals the selected value. Put into variable.
        query_result = connect_to_database.executeSelectQuery("SELECT * FROM Mailings WHERE mail_id='" + passed_id + "'")
        print("\nMailing Information:\n")
        for record in query_result:
            print("1. Name: " + record["name"])

            try:
                print("2. Company: " + record["company"])
            except:
                print("2. Company: None")
            
            print("3. Address: " + record["address"])


    def getMailingDatabase(self):
        """Method that displays all entries within the database in a clean format
        Arguments:
            None -- Information is collected from a select query
        Returns:
            output_string {String Value} -- String variable containing information within the CRM database"""
        
        #show_records = connect_to_database.executeSelectQuery("SELECT * FROM Mailings")
        database_values = setup.load_data("text_files/customers.json")
        print("\nMailings Database")
        output_string = ""
        for record in database_values:
            output_string += "\nMail ID: " + str(record['mail_id']) + " | "
            output_string += "Name: " + record['f_name'] + " " + record['l_name'] + " | "
            try:
                output_string += "Company: " + record['company'] + " | "
            except:
                output_string += "Company: " + record['f_name'] + " " + record['l_name'] + " | "
            output_string += "Address: " + record['address'] + ", " + record['city'] + ", " + record['state'] + " " + record['zip'] +  " | "
        
        return(output_string)




    def get_crm_id(self, passed_id):
        """Method that finds and returns the mail ID of the customer when only the mail_id is known
        Arguments:
            passed_id {String Value} -- String value containing ID information
        Returns:
            ret_crm_id {String Value} -- String value containing Mail ID"""

        mail_info_list = connect_to_database.executeSelectQuery("SELECT * from MAILINGS WHERE mail_id =" + passed_id)
        crm_info = connect_to_database.executeSelectQuery("SELECT * FROM crm_data")
        print(mail_info_list)

        for key, value in mail_info_list[0].items():
            if key == "name":
                name = value.split()
                print(name)
                for value in name:
                    f_name = name[0]
                    l_name = name[1]
     
        print(f_name)
        print(l_name)
        
        record_found = False
        for record in crm_info:
            if record["f_name"] == f_name and record["l_name"] == l_name:
                record_found = True
                ret_crm_id = record["crm_id"]
        
        if not record_found:
            print("Sorry, could not find the CRM ID for " + f_name + " " + l_name + ".")
        else:
            return ret_crm_id
        

        

    def getMailID(self, passed_id):
        """Method that finds and returns the mail ID of the customer when only the crm_id is known
        Arguments:
            passed_id {String Value} -- String value containing ID information
        Returns:
            ret_mail_id {String Value} -- String value containing Mail ID"""

        crm_info_list = connect_to_database.executeSelectQuery("SELECT * from crm_data WHERE crm_id =" + passed_id)
        mail_info = connect_to_database.executeSelectQuery("SELECT * FROM Mailings")

        for key, value in crm_info_list[0].items():
            if key == "f_name":
                f_name = value
            if key == "l_name":
                l_name = value
     
        full_name = f_name + " " + l_name
        
        record_found = False
        for record in mail_info:
            if record["name"] == full_name:
                record_found = True
                ret_mail_id = record["mail_id"]
        
        if not record_found:
            print("Sorry, could not find the Mail ID for " + full_name + ".")
        else:
            return ret_mail_id

    
    def updateFullName(self, passed_id):
        """Method that updates the full name of a customer in both databases
        Arguments:
            passed_id {String Value} -- String value that holds a passed Mail ID
        Returns:
            None -- Directly updates value in the database, then displays changed values"""

        f_name = user_input.getFirstName()
        l_name = user_input.getLastName()
        full_name = f_name + " " + l_name

        crm_id = self.get_crm_id(passed_id)

        connect_to_database.executeQuery("UPDATE Mailings SET name='" + full_name + "' WHERE mail_id='" + passed_id + "'")
        connect_to_database.executeQuery("UPDATE crm_data SET f_name='" + f_name + "' WHERE crm_id='" + str(crm_id) + "'")
        connect_to_database.executeQuery("UPDATE crm_data SET l_name='" + l_name + "' WHERE crm_id='" + str(crm_id) + "'")
        connect_to_database.conn.commit()

        self.displayMailing(passed_id)


              
    def updateAddress(self, passed_id):
        """Method that updates the address of a customer in both databases
        Arguments:
            passed_id {String Value} -- String value that holds a passed Mail ID
        Returns:
            None -- Directly updates value in the database, then displays changed values"""
        
        address = user_input.getStreetAddress()
        city = user_input.getCity()
        state = user_input.getState()
        zip = user_input.getZip()

        mailing_address = address + ", " + city + ", " + state + " " + zip

        crm_id = self.get_crm_id(passed_id)

        connect_to_database.executeQuery("UPDATE Mailings SET address='" + mailing_address + "' WHERE mail_id='" + passed_id + "'")
        connect_to_database.executeQuery("UPDATE crm_data SET address='" + address + "', city='" + city + "', state='" + state + "', zip='" + zip + "'  WHERE crm_id='" + str(crm_id) + "'")
        connect_to_database.conn.commit()

        self.displayMailing(passed_id)

    

    def updateCompany(self, passed_id):
        """Method that updates the company of a customer in both databases
        Arguments:
            passed_id {String Value} -- String value that holds a passed Mail ID
        Returns:
            None -- Directly updates value in the database, then displays changed values"""
        
        company = user_input.getCompanyName()

        crm_id = self.get_crm_id(passed_id)

        connect_to_database.executeQuery("UPDATE Mailings SET company='" + company + "' WHERE mail_id='" + passed_id + "'")
        connect_to_database.executeQuery("UPDATE crm_data SET company='" + company + "' WHERE crm_id='" + str(crm_id) + "'")
        connect_to_database.conn.commit()

        self.displayMailing(passed_id)
    
    

