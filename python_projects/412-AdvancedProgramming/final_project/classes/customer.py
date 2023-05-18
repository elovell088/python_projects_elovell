#IT 412 - Eric Lovell - Final Project Customer Class
from classes.setup import Setup

setup = Setup()

class Customer:
    """Class that is a virtual representation of a customer"""

    def __init__(self, f_name, l_name, address, city, state, zip, primary_phone, company="", secondary_phone="", email_address=""  ):
        """Constructor for the customer class"""

        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.primary_phone = primary_phone
        self.company = company
        self.secondary_phone = secondary_phone
        self.email_address = email_address

        self.crm_id = self.load_crm_id()
        self.mail_id = self.load_mail_id()
    
    
    def load_crm_id(self):
        """Method that looks for available crm_id for the database in the set_config file. Automatically assigns new customer a crm_id
        Arguments:
            None -- Data is pulled from file directory
        Returns:
            ret_crm_id {String Value} -- String value containing crm_id for new customer instance"""
        
        config_data = setup.load_data("setup_files/setup_config.json")
        ret_crm_id = config_data["crm_id"]

        return ret_crm_id


    def load_mail_id(self):
        """Method that looks for available mail_id for the database in the set_config file. Automatically assigns new customer a mail_id
        Arguments:
            None -- Data is pulled from file directory
        Returns:
            ret_mail_id {String Value} -- String value containing mail_id for new customer instance"""
        
        config_data = setup.load_data("setup_files/setup_config.json")
        ret_mail_id = config_data["mail_id"]

        return ret_mail_id
