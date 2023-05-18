#IT 412 - Eric Lovell - Final Project Program Setup Class
from classes.database_access import DB_Connect
import json
import os.path

#Create instance of databases
#crm_data = DB_Connect('root', '', 'python_projects')
#Mailings = DB_Connect('root', '', 'python_projects')
connect_to_database = DB_Connect('root', '', 'python_projects')

class Setup():
    """Class that holds methods to setup program on launch"""

    def __init__(self):
        """Constructor for the Setup Class"""

    def clearScreen(self):
        """Method that clears the screen for easir visibility
        Arguments:
            None -- Clears screen with new line values
        Returns:
            None -- Clears screen with new line values"""
        
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


    def sync_database(self):
        """Method that accesses database and pulls the last crm and mail id used. Saves local json file for other classes/methods to access
        Arguments:
            None -- Calls other methods within class for information gathering
        Returns:
            None -- Syncs database values with values within the setup_config.json file"""

        self.updateCustomers()
        setup_file = "setup_files/setup_config.json"
        synced_data = {"crm_id" : "10001", "mail_id" : "20001"}

        crm_data_exists = self.check_crm_data()
        mailing_data_exists = self.check_mailing_data()
        
        if crm_data_exists and mailing_data_exists:
            crm_id = self.generate_crm_id()
            mail_id = self.generate_mail_id()
            
            synced_data["crm_id"] = crm_id
            synced_data["mail_id"] = mail_id
            self.save_data(synced_data, setup_file)

        else:
            self.save_data(synced_data, setup_file)

        


    def check_crm_data(self):
        """Method that checks the CRM Database to see if data exists
        Arguments:
            None -- Select query within method collects necessary information
        Returns:
            True -- If data exists | False -- If data does not exist"""
        
        data_exists = connect_to_database.executeSelectQuery("SELECT * FROM crm_data")
        if data_exists:
            return True
        else:
            return False
    

    def check_mailing_data(self):
        """Method that checks the Mailings Database to see if data exists
        Arguments:
            None -- Select query within method collects necessary information
        Returns:
            True -- If data exists | False -- If data does not exist"""
        
        data_exists = connect_to_database.executeSelectQuery("SELECT * FROM Mailings")
        if data_exists:
            return True
        else:
            return False


    def generate_crm_id(self):
        """Method that generates new CRM ID's based off database values
        Arguments:
            None -- Information is collected with a select query
        Returns:
            new_id {String Value} -- String value containing new crm ID"""
        
        search_query = connect_to_database.executeSelectQuery("SELECT * FROM crm_data")
            
        new_id = search_query[-1]['crm_id']
        new_id = int(new_id)
        new_id += 1
        new_id = str(new_id)

        
        return new_id
    

    def generate_mail_id(self):
        """Method that generates new Mail ID's based off database values
        Arguments:
            None -- Information is collected with a select query
        Returns:
            new_id {String Value} -- String value containing new Mail ID"""
        
        search_query = connect_to_database.executeSelectQuery("SELECT * FROM Mailings")
            
        new_id = search_query[-1]['mail_id']
        new_id = int(new_id)
        new_id += 1
        new_id = str(new_id)

        
        return new_id
   

    def load_data(self, passed_file):
        """Function that loads the contents of a file
        Arguments:
            passed_file {File Path} -- String value that contains path to the file for loading
        Returns:
            config_data {Dictionary Item} -- Dictionary object containing configurations loaded from JSON file
            None -- If file doesn't exist, it is caught in 'except' and prints message stating it doesn't exist"""
        
        try:
            with open(passed_file) as json_obj:
                config_data = json.load(json_obj)
                return (config_data)

        except FileNotFoundError:
            print("Sorry, this file doesn't exist.")



    def programPrompts(self):
        """Displays available prompts for user
        Arguments:
            None
        Returns:
            None -- Directly prints program prompts to the console"""

        output_string = ''
        output_string = output_string + "\n                     *Prompts*\n"
        output_string = output_string + "| 1. Import Data  | 2. View Database | 3. Add Record  |\n"
        output_string = output_string + "         | 4. Edit Record  | 5. Exit Program  | \n"

        print(output_string)



    def save_data(self, new_data, new_file, silent="n"):
        """Function that saves the newest JSON configurations to setup_files.json   
        Arguments:
            new_data {Dictionary Item} -- Dictionary object containing configurations from JSON file
            new_file {File Path} -- String value containing path to backup_file location
            silent {Optional Value} -- If 'n': message is printed | If 'y': message NOT printed
        Returns:
            None -- Overwrites contents within new_file, saves file, and prints message that configurations were saved"""
        
        if silent == "n":
            with open(new_file, "w") as json_obj:
                json.dump(new_data, json_obj)
                print("\nNew configurations saved to: " + new_file)
        
        if silent == "y":
            with open(new_file, "w") as json_obj:
                json.dump(new_data, json_obj)

    
    def update_configs(self):
        """Method that updates config values in setup_config.json
        Arguments: 
            None -- Information is collecting by loading data within setup_config.json file
        Returns:
            None -- Saves new configurations to the setup_config.json file"""
        
        current_config = self.load_data("setup_files/setup_config.json")
        crm_num = int(current_config["crm_id"])
        mail_num = int(current_config["mail_id"])
        new_crm_num = crm_num + 1
        new_mail_num = mail_num + 1
        current_config["crm_id"] = str(new_crm_num)
        current_config["mail_id"] = str(new_mail_num)

        self.save_data(current_config, "setup_files/setup_config.json", "y")



    def updateCustomers(self):
        """"""
        data_exists = self.check_crm_data()
        if data_exists:
            customers = connect_to_database.executeSelectQuery("SELECT * FROM crm_data")
            
            for customer in customers:
                customer['mail_id'] = customer['crm_id'] + 10000
            
            with open("text_files/customers.json", "w") as json_obj:
                json.dump(customers, json_obj)




    def reset_configs(self):
        """Method that resets config values in setup_config.json back to starting values
        Arguments: 
            None -- Information is collecting by loading data within setup_config.json file
        Returns:
            None -- Resets new configurations to the setup_config.json file"""
        
        current_config = self.load_data("setup_files/setup_config.json")
        current_config["crm_id"] = '10001'
        current_config["mail_id"] = '20001'
        
        self.save_data(current_config, "setup_files/setup_config.json", "y")

    
