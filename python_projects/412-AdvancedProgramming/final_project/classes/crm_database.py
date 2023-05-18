#IT 412
import json
from classes.mailing_database import mailingDatabase
from classes.database_access import DB_Connect
from classes.inputs import Inputs
from classes.setup import Setup


#Create instance of classes
#Mailings = DB_Connect('root', '', 'python_projects')
#crm_data = DB_Connect('root', '', 'python_projects')
user_input = Inputs()
setup = Setup()
get_mail_info = mailingDatabase()
connect_to_database = DB_Connect('root', '', 'python_projects')

class crmDatabase():
    """Virtual representation of CRM database"""

    def __init__(self):
        """Constructor for the crmDatabase class"""

    def displayCustomerMailing(self, passed_id):
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



    def displayCustomer(self, passed_id):
        """Displays an individual customers information from the CRM database
        Arguments:
            passed_id {String Value} -- String value containing crm id information
        Returns:
            None -- Directly prints customer information to the console"""

        query_result = connect_to_database.executeSelectQuery("SELECT * FROM crm_data WHERE crm_id='" + passed_id + "'")
        print("\nCustomer Information:\n")
        for record in query_result:
            print("1. First Name: " + record["f_name"])
            print("2. Last Name: " + record["l_name"])            
            print("3. Street: " + record["address"])
            print("4. City: " + record["city"])
            print("5. State: " + record["state"])
            print("6. Zip Code: " + str(record["zip"]))

            try:
                print("7. Company: " + record["company"])
            except:
                print("7. Company: None")

            print("8. Primary Phone: " + record["primary_phone"])
            try:  
                print("9. Secondary Phone: " + record["secondary_phone"])
            except:
                print("9. Secondary Phone: None")
            try:  
                print("10. Email: " + record["email_address"])
            except:
                print("10. Email: None")



    def displayCustomerMailing(self, passed_id):
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



    def findRecord(self, passed_id):
        """Method that finds a record in the CRM database
        Arguments:
            passed_vin {String Value} -- String value that contains VIN number to search for in database
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
        

    def generateInsertCRMQuery(self, passed_customer):
        """Method that generates an insert query for crm
        Arguments:
            passed_pustomer {customer_object} -- Instance of Customer Class
        Returns:
            ret_query_string {String Value} -- String value that holds an sql insert statement generated from Customer Class Attributes """

        insert_string = "INSERT INTO crm_data (crm_id, f_name, l_name, address, city, state, zip,"

        value_string = " VALUES ("
        value_string += "'" + passed_customer.crm_id + "',"
        value_string += "'" + passed_customer.f_name + "',"
        value_string += " '" + passed_customer.l_name + "',"
        value_string += " '" + passed_customer.address + "',"
        value_string += " '" + passed_customer.city + "',"
        value_string += " '" + passed_customer.state + "',"
        value_string += " '" + passed_customer.zip + "',"
        
        if passed_customer.company:
            insert_string += " company,"
            value_string += " '" + passed_customer.company + "', "
        
        #Primary Phone
        insert_string += " primary_phone"
        value_string += " '" + passed_customer.primary_phone + "'"

        if passed_customer.secondary_phone:
            insert_string += ", secondary_phone"
            value_string += ", '" + passed_customer.secondary_phone+ "'"
        
        if passed_customer.email_address:
            insert_string += ", email_address"
            value_string += ", '" + passed_customer.email_address + "'"
        
        insert_string += ")"
        value_string += ")"
        ret_query_string = insert_string + value_string
        
        return ret_query_string
    

    def getCRMDatabase(self):
        """Method that displays all entries within the database in a clean format
        Arguments:
            None
        Returns:
            output_string {String Value} -- String variable containing information within the CRM database"""
        
        database_values = setup.load_data("text_files/customers.json")

        print("\nCRM Database")
        output_string = ""
        for record in database_values:
            output_string += "\nCustomer ID: " + str(record['crm_id']) + " | "
            output_string += "First Name: " + record['f_name'] + " | "
            output_string += "Last Name: " + record['l_name'] + " | "

            output_string += "Street Address: " + record['address'] + " | "
            output_string += "City: " + record['city'] + " | "
            output_string += "State: " + record['state'] + " | "
            output_string += "Zip: " + str(record['zip']) + " | "

            try:
                output_string += "Company: " + record['company_name'] + " | "
            except:
                output_string += "Company: None | "

            output_string += "Primary Phone: " + record['primary_phone'] + " | "

            try:
                output_string += "Secondary Phone: " + record['secondary_phone'] + " |"
            except:
                output_string += "Secondary Phone: None |"
            
            try:
                output_string += "Email: " + record['email_address'] + " |\n"
            except:
                output_string += "Email: None |\n"
        

        return(output_string)

        
    
    def updateFirstName(self, passed_id):
        """Method that updates the first name of a customer in both databases
        Arguments:
            passed_id {String Value} -- String value that holds a passed CRM ID
        Returns:
            None -- Directly updates value in the database, then displays changed values"""
        
        f_name = user_input.getFirstName()
        l_name_holder =  connect_to_database.executeSelectQuery("SELECT l_name FROM crm_data WHERE crm_id=" + passed_id )
        l_name_dict = l_name_holder[0]
        l_name = l_name_dict["l_name"]

        full_name = f_name + " " + l_name

        mail_id = get_mail_info.getMailID(passed_id)

        connect_to_database.executeQuery("UPDATE Mailings SET name='" + full_name + "' WHERE mail_id='" + str(mail_id) + "'")
        connect_to_database.conn.commit()
        connect_to_database.executeQuery("UPDATE crm_data SET f_name='" + f_name + "' WHERE crm_id='" + passed_id + "'")
        connect_to_database.conn.commit()

        self.displayCustomer(passed_id)
        self.displayCustomerMailing(str(mail_id))

    
    def updateLastName(self, passed_id):
        """Method that updates the last name of a customer in both databases
        Arguments:
            passed_id {String Value} -- String value that holds a passed CRM ID
        Returns:
            None -- Directly updates value in the database, then displays changed values"""
        
        l_name = user_input.getLastName()
        f_name_holder =  connect_to_database.executeSelectQuery("SELECT f_name FROM crm_data WHERE crm_id='" + passed_id + "'")
        f_name_dict = f_name_holder[0]
        f_name = f_name_dict["f_name"]

        full_name = f_name + " " + l_name

        mail_id = get_mail_info.getMailID(passed_id)

        connect_to_database.executeQuery("UPDATE Mailings SET name='" + full_name + "' WHERE mail_id='" + str(mail_id) + "'")
        connect_to_database.executeQuery("UPDATE crm_data SET l_name='" + l_name + "' WHERE crm_id='" + passed_id + "'")
        connect_to_database.conn.commit()


        self.displayCustomer(passed_id)

        
              
    def updateAddress(self, passed_id):
        """Method that updates the street address of a customer in both databases
        Arguments:
            passed_id {String Value} -- String value that holds a passed CRM ID
        Returns:
            None -- Directly updates value in the database, then displays changed values"""
        
        address = user_input.getStreetAddress()
        city_holder =  connect_to_database.executeSelectQuery("SELECT city FROM crm_data WHERE crm_id='" + passed_id + "'")
        city_dict = city_holder[0]
        city = city_dict["city"]

        state_holder =  connect_to_database.executeSelectQuery("SELECT state FROM crm_data WHERE crm_id='" + passed_id + "'")
        state_dict = state_holder[0]
        state = state_dict["state"]

        zip_holder =  connect_to_database.executeSelectQuery("SELECT zip FROM crm_data WHERE crm_id='" + passed_id + "'")
        zip_dict = zip_holder[0]
        zip = zip_dict["zip"]

        mailing_address = address + ", " + city + ", " + state + " " + str(zip) 

        mail_id = get_mail_info.getMailID(passed_id)

        connect_to_database.executeQuery("UPDATE Mailings SET address='" + mailing_address + "' WHERE mail_id='" + str(mail_id) + "'")
        connect_to_database.executeQuery("UPDATE crm_data SET address='" + address + "' WHERE crm_id='" + passed_id + "'")
        connect_to_database.conn.commit()
        
        self.displayCustomer(passed_id)
        


    def updateCity(self, passed_id):
        """Method that updates the city of a customer in both databases
        Arguments:
            passed_id {String Value} -- String value that holds a passed CRM ID
        Returns:
            None -- Directly updates value in the database, then displays changed values"""
        
        city = user_input.getCity()
        address_holder = connect_to_database.executeSelectQuery("SELECT address FROM crm_data WHERE crm_id='" + passed_id + "'")
        address_dict = address_holder[0]
        address = address_dict["address"]

        state_holder = connect_to_database.executeSelectQuery("SELECT state FROM crm_data WHERE crm_id='" + passed_id + "'")
        state_dict = state_holder[0]
        state = state_dict["state"]

        zip_holder =  connect_to_database.executeSelectQuery("SELECT zip FROM crm_data WHERE crm_id='" + passed_id + "'")
        zip_dict = zip_holder[0]
        zip = zip_dict["zip"]

        mailing_address = address + ", " + city + ", " + state + " " + str(zip) 

        mail_id = get_mail_info.getMailID(passed_id)

        connect_to_database.executeQuery("UPDATE Mailings SET address='" + mailing_address + "' WHERE mail_id='" + str(mail_id) + "'")
        connect_to_database.executeQuery("UPDATE crm_data SET city='" + city + "' WHERE crm_id='" + passed_id + "'")
        connect_to_database.conn.commit()

        self.displayCustomer(passed_id)



    def updateState(self, passed_id):
        """Method that updates the state of a customer in both databases
        Arguments:
            passed_id {String Value} -- String value that holds a passed CRM ID
        Returns:
            None -- Directly updates value in the database, then displays changed values"""
        
        state = user_input.getState()

        address_holder =  connect_to_database.executeSelectQuery("SELECT address FROM crm_data WHERE crm_id='" + passed_id + "'")
        address_dict = address_holder[0]
        address = address_dict["address"]

        city_holder =  connect_to_database.executeSelectQuery("SELECT city FROM crm_data WHERE crm_id='" + passed_id + "'")
        city_dict = city_holder[0]
        city = city_dict["city"]

        zip_holder =  connect_to_database.executeSelectQuery("SELECT zip FROM crm_data WHERE crm_id='" + passed_id + "'")
        zip_dict = zip_holder[0]
        zip = zip_dict["zip"]

        mailing_address = address + ", " + city + ", " + state + " " + str(zip) 

        mail_id = get_mail_info.getMailID(passed_id)

        connect_to_database.executeQuery("UPDATE Mailings SET address='" + mailing_address + "' WHERE mail_id='" + str(mail_id) + "'")
        connect_to_database.executeQuery("UPDATE crm_data SET state='" + state + "' WHERE crm_id='" + passed_id + "'")
        connect_to_database.conn.commit()

        self.displayCustomer(passed_id)


    def updateZip(self, passed_id):
        """Method that updates the zip code of a customer in both databases
        Arguments:
            passed_id {String Value} -- String value that holds a passed CRM ID
        Returns:
            None -- Directly updates value in the database, then displays changed values"""
        
        zip = user_input.getZip()
        
        state_holder =  connect_to_database.executeSelectQuery("SELECT state FROM crm_data WHERE crm_id='" + passed_id + "'")
        state_dict = state_holder[0]
        state = state_dict["state"]

        address_holder =  connect_to_database.executeSelectQuery("SELECT address FROM crm_data WHERE crm_id='" + passed_id + "'")
        address_dict = address_holder[0]
        address = address_dict["address"]

        city_holder =  connect_to_database.executeSelectQuery("SELECT city FROM crm_data WHERE crm_id='" + passed_id + "'")
        city_dict = city_holder[0]
        city = city_dict["city"]

        mailing_address = address + ", " + city + ", " + state + " " + zip 

        mail_id = get_mail_info.getMailID(passed_id)

        connect_to_database.executeQuery("UPDATE Mailings SET address='" + mailing_address + "' WHERE mail_id='" + str(mail_id) + "'")
        connect_to_database.executeQuery("UPDATE crm_data SET zip='" + zip + "' WHERE crm_id='" + passed_id + "'")
        connect_to_database.conn.commit()

        self.displayCustomer(passed_id)



    def updateCompany(self, passed_id):
        """Method that updates the company of a customer in both databases
        Arguments:
            passed_id {String Value} -- String value that holds a passed CRM ID
        Returns:
            None -- Directly updates value in the database, then displays changed values"""
        
        company = user_input.getCompanyName()
        mail_id = get_mail_info.getMailID(passed_id)

        connect_to_database.executeQuery("UPDATE Mailings SET company='" + company + "' WHERE company='" + str(mail_id) + "'")
        connect_to_database.executeQuery("UPDATE crm_data SET company='" + company + "' WHERE crm_id='" + passed_id + "'")
        connect_to_database.conn.commit()

        self.displayCustomer(passed_id)



    def updatePrimaryPhone(self, passed_id):
        """Method that updates the primary phone number of a customer in both databases
        Arguments:
            passed_id {String Value} -- String value that holds a passed CRM ID
        Returns:
            None -- Directly updates value in the database, then displays changed values"""
        
        primary_phone = user_input.getPhoneNumber()

        connect_to_database.executeQuery("UPDATE crm_data SET primary_phone='" + primary_phone + "' WHERE crm_id='" + passed_id + "'")
        connect_to_database.conn.commit()

        self.displayCustomer(passed_id)

        

    def updateSecondaryPhone(self, passed_id):
        """Method that updates the secondary phone number of a customer in both databases
        Arguments:
            passed_id {String Value} -- String value that holds a passed CRM ID
        Returns:
            None -- Directly updates value in the database, then displays changed values"""
        secondary_phone = user_input.getSecPhone()
        
        connect_to_database.executeQuery("UPDATE crm_data SET secondary_phone='" + secondary_phone + "' WHERE crm_id='" + passed_id + "'")
        connect_to_database.conn.commit()

        self.displayCustomer(passed_id)



    def updateEmailAddress(self, passed_id):
        """Method that updates the email address of a customer in both databases
        Arguments:
            passed_id {String Value} -- String value that holds a passed CRM ID
        Returns:
            None -- Directly updates value in the database, then displays changed values"""
        
        email_address = user_input.getEmail()

        connect_to_database.executeQuery("UPDATE crm_data SET email_address='" + email_address + "' WHERE crm_id='" + passed_id + "'")
        connect_to_database.conn.commit()

        self.displayCustomer(passed_id)