#IT 412 - Eric Lovell - Final Project Reformat Class
import json
from classes.setup import Setup
from classes.database_access import DB_Connect

setup = Setup()
connect = DB_Connect('root', '', 'python_projects')
class Reformat:
    """Class that holds methods to reformat a file into json and csv format"""

    def __init__(self):
        """Constructor for Reformat Class"""

    
    def customerJSON(self, passed_customer):
        """File that appends a dictionary item to a JSON File"""
               
        data_for_json = {}
        data_for_json['f_name'] = passed_customer.f_name
        data_for_json['l_name'] = passed_customer.l_name
        data_for_json['address'] = passed_customer.address
        data_for_json['city'] = passed_customer.city
        data_for_json['state'] = passed_customer.state
        data_for_json['zip'] = passed_customer.zip
        try:
            data_for_json['company'] = passed_customer.company
        except:
            data_for_json['company'] = 'None'

        data_for_json['primary_phone'] = passed_customer.primary_phone
        
        try:
            data_for_json['secondary_phone'] = passed_customer.secondary_phone
        except:
            data_for_json['secondary_phone'] = 'None'
        try:
            data_for_json['email_address'] = passed_customer.email_address
        except:
            data_for_json['email_address'] = 'None'

        data_for_json['crm_id'] = passed_customer.crm_id
        data_for_json['mail_id'] = passed_customer.mail_id
        
        return data_for_json


    def dataForCSV(self, passed_file):
        """Method that reformats data from a text file to data that can be input into a CSV File
        Arguments:
            passed_file {Text File} -- Text file that contains information to be reformatted into a CSV File
        Returns:
            data_for_file {Comma Separated Values} -- Variable containing reformatted values"""
        
        data_for_file = ""
        with open(passed_file) as txt_file:
            for line in txt_file:
                temp_list = []
                temp_list.append(line)

                clean_data_list = self.removeCharacters(temp_list)
                
                count = 0
                while count < len(clean_data_list):
                    data_for_file += clean_data_list[count] + ", "
                    count += 1
                data_for_file += "\n"
            
            return data_for_file

    
    
    def dataForJSON(self, passed_file):
        """Method that reformats data from a text file to data that can be input into a JSON File
        Arguments:
            passed_file {Text File} -- Text file that contains information to be reformatted into a JSON File
        Returns:
            data_for_file {Dictionary Object} -- Variable containing reformatted values in dictionary format"""
        
        data_for_file = []
        crm_id = 10000
        mail_id = 20000
        with open(passed_file) as txt_file:
            for line in txt_file:
                temp_list = []
                temp_list.append(line)
                clean_data_list = self.removeCharacters(temp_list)

                customer_dict = {"f_name" : clean_data_list[0],
                                 "l_name" : clean_data_list[1],
                                 "address" : clean_data_list[3],
                                 "city" : clean_data_list[4],
                                 "state" : clean_data_list[5],
                                 "zip" : clean_data_list[6],
                                 "company" : clean_data_list[2],
                                 "primary_phone" : clean_data_list[7],
                                 "secondary_phone" : clean_data_list[8],
                                 "email_address" : clean_data_list[9],
                                 ######ADDED#######
                                 "crm_id" : str(crm_id),
                                 "mail_id" : str(mail_id)
                                 }
                
                data_for_file.append(customer_dict)
                crm_id += 1
                mail_id += 1
            
            return data_for_file



    def removeJSON(self, passed_file, passed_id):
        """Method at modifies customers.json
        Arguments:
            
        Returns: 
        """
        data = setup.load_data(passed_file)
        count = 0
        for record in data:
            if record['crm_id'] == passed_id:
                del data[count]
            count += 1

        with open(passed_file, "w") as json_obj:
            json.dump(data, json_obj)


    def reformatCSV(self, passed_file, passed_data):
        """Method that writes reformatted CSV data into a CSV File
        Arguments:
            passed_file {New CSV File} -- String value containing path the new csv file location
            passed_data {Comma Separated Values} -- Variable containing reformatted comma separated values
        Returns:
            None -- Takes new data and directly writes it to new file"""

        with open(passed_file, "w") as csv_file:
            csv_file.write(passed_data)

    
    
    def reformatJSON(self, passed_file, passed_data):
        """Method that writes reformatted JSON data into a JSON File
        Arguments:
            passed_file {New JSON File} -- String value containing path the new JSON file location
            passed_data {Dictionary Obejct} -- Variable containing reformatted values in dictionary format
        Returns:
            None -- Takes new data and directly writes it to new file"""     

        with open(passed_file, "w") as json_obj:
            json.dump(passed_data, json_obj)    
                
    

    def removeCharacters(self, passed_list):
        """Method that removes character from text file
        Arguments:
            passed_list {List Object} -- List Object containing customer values
        Returns:
            ret_list {List Object} -- List Object containings new customer values, removing duplicates and unncessary columns"""
        
        ret_list = []

        temp_line = ""
        for character in passed_list[0]:
                    if character == '#':
                        pass
                    elif character == '|':
                        ret_list.append(temp_line)
                        temp_line = ""
                    else:
                        temp_line += character
        
        del ret_list[5]
        del ret_list[-1]
       
        return ret_list
        


    def updateJson(self, passed_id):
        """Method that updates the customer.json after an entry has been modified
        Arguments:
            
        Returns:
            """
        
        new_value = connect.executeSelectQuery("SELECT * FROM crm_data WHERE crm_id =" + passed_id)
        new_value_dict = new_value[0]

        data = setup.load_data("text_files/customers.json")

        list_index = 0
        record_found = False
        while not record_found:
            for record in data:
                if record['crm_id'] == passed_id:
                    record_found = True
                    delete_index = list_index
                    break

                list_index += 1

        if record_found:
            del data[delete_index]
            data.insert(delete_index, new_value_dict)

            with open("text_files/customers.json", "w") as json_obj:
                json.dump(data, json_obj)

        else:
            print("Record was not found.")
        
