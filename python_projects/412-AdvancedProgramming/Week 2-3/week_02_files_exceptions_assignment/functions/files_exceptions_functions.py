import json
import os.path
import time


def add_data(passed_data):
    """Function that prompts user for new values and adds them to a JSON configuration object
    
    Arguments:
        passed_data {Dictionary Item} -- Dictionary object containing current configurations loaded from JSON file
    Returns:
        passed_data {Dictionary Item} -- Dictionary object containing updated configurations with added values"""
   
    add_key = input("Please enter key for the item you would like to add: ")
    add_key = add_key.lower()
    
    input_validated = False
    while not input_validated:
        #Begin with input validation, checks to see if 'add_key' exists in 'passed_data'
        validation_result = validate_data(add_key, 'add', passed_data)
        #If returned True, validation passed, start adding data logic
        if validation_result == True:
            add_value = input("Please enter the value for the new key: ")
            passed_data[add_key] = add_value
            input_validated = True
        #If return False, validation failed, prompt user for new key
        else:
            add_key = input("Sorry, that key already exist. Please try again: ")

    return(passed_data)


def backup_data(backup_data, backup_file):
    """Function that back ups the previous JSON configurations to a backup file
    
    Arguments:
        backup_data {Dictionary Item} -- Dictionary object containing configurations from JSON file
        backup_file {File Path} -- String value containing path to backup_file location
    Returns:
        None -- Saves contents to new backup file and prints message that configurations were saved"""

    backup_file = backup_file + str(time.time())
    with open(backup_file, "w") as json_obj:
        json.dump(backup_data, json_obj)
        print("Previous configurations backed up to: " + backup_file + "\n")


def change_configs(config_data):
    """Function that updates the configuration data object with proper/newest data
    
    Arguments:
        config_data {Dictionary Item} -- Dictionary object containing data loaded from JSON file with new data
    Returns:
        new_config {Dictionary Item} -- Dictionary object containing data from config_data argument"""
    
    #Create dictionary object for new configurations
    new_config = {}
    #Copy data from config_data into new_config dictionary object
    for key, value in config_data.items():
        new_config[key] = value
    
    return new_config


def check_file(passed_original_file, passed_modified_file):
    """Function that determines the current json file being loaded into the program

    Arguments:
        passed_original_file {File Path} -- String value that contains path to basic_configs file
        passed_modified_value {File Path} -- String value that contains path to override_configs file
    Returns:
        current_file {File Path} -- String value for path of the current file the program should work with"""
    
    #If basic_config and override_configs exist, override_configs is the current_file the program should work with
    if os.path.isfile(passed_original_file) and os.path.isfile(passed_modified_file):
        current_file = passed_modified_file
    #If only basic_json exists, basic_json is the current_file the program should work with
    else: 
        current_file = passed_original_file
    
    return current_file


def display_data(passed_data):
    """Function to display data within a json file
    
    Arguments:
        passed_data {Dictionary Item} -- Dictionary object containing items for display output
    Returns:
        output_string {String Values} - String value containing clean output from data within passed_data argument"""

    count = 1
    output_string = '\nCurrent Configuration\n'
    for key in passed_data:
        output_string = output_string + str(count) + ". " + key.title() + " - "
        output_string = output_string.rstrip() + ' "' + passed_data[key] + '"\n'
        count += 1
    
    return(output_string.rstrip())


def load_data(passed_file):
    """Function that loads the contents of a file
    
    Arguments:
        passed_file {File Path} -- String value that contains path to the file for loading
    Returns:
        config_data {Dictionary Item} -- Dictionary object containing configurations loaded from JSON file
        None -- If file doesn't exist, it is caught in 'except' and prints message stating it doesn't exist"""
    
    #Try loading file to a dictionary object
    try:
        with open(passed_file) as json_obj:
            config_data = json.load(json_obj)
            return (config_data)
    #If the file doesn't exist. Catch the error and print message   
    except FileNotFoundError:
        print("Sorry, this file doesn't exist.")


def modify_data(passed_data):
    """Function that prompts user for values to modify from the content within JSON configuration object
    
    Arguments:
        passed_data {Dictionary Item} -- Dictionary object containing current configurations loaded from JSON file
    Returns:
        passed_data {Dictionary Item} -- Dictionary object containing updated configurations with modified values"""
    
    modify_key = input("Please enter the key for the item you would like to modify: ")
    modify_key = modify_key.lower()

    input_validated = False
    while not input_validated:
        #Begin input validation, checks to see if 'modify_key' exists in 'passed_data'
        validation_result = validate_data(modify_key, 'modify', passed_data)
        #If returned True, value passed validation, start modification logic
        if validation_result == True:
            modify_value = input("Please enter the new value: ")
            passed_data[modify_key] = modify_value
            input_validated = True
        #If return False, value failed validation, prompt user for new key
        else:
            modify_key = input("Sorry, that key doesn't exist. Please try again: ")

    return(passed_data)


def program_prompts():
    """Function that provides prompts to the user with clean output
    
    Arguments:
        None
    Returns:
        None -- Directly prints prompt with clean output"""

    output_string = ''
    output_string = output_string + "\nPrompts\n"
    output_string = output_string + "|'m' to modify existing configurations | 'r' to remove configurations   | 'a' to add configurations |\n"
    output_string = output_string + "|'s' to save current configurations    | 'd' to discard current changes | 'x' to terminate program  |\n"

    print(output_string)


def remove_data(passed_data):
    """Function that removes key/pair values from JSON configurations
    
    Arguments:
        passed_data {Dictionary Item} -- Dictionary object containing current configurations loaded from JSON file
    Returns:
        passed_data {Dictionary Item} -- Dictionary object containing updated configurations with removed values"""

    remove_key = input("Please enter the key you would like to remove: ")
    remove_key = remove_key.lower()

    input_validated = False
    while not input_validated:
        #Start validation for input values equal to safe mode, memory, error log
        validate = validate_data(remove_key, 'remove', passed_data)
        if validate == False:
            remove_key == input("\nSorry, you cannot remove that configuration. Please try again: ")
        #If input value passes validation but key does not exist 
        elif remove_key not in passed_data and validate == False:
            remove_key = input("\nSorry, this key doesn't exist. Please try again: ")
        #If validation passes and key exists in configuration
        else:
            del passed_data[remove_key]
            input_validated = True
    
    return passed_data


def save_data(new_data, new_file):
    """Function that saves the newest JSON configurations to config_override file
    
    Arguments:
        new_data {Dictionary Item} -- Dictionary object containing configurations from JSON file
        new_file {File Path} -- String value containing path to backup_file location
    Returns:
        None -- Overwrites contents within new_file, saves file, and prints message that configurations were saved"""
    
    with open(new_file, "w") as json_obj:
        json.dump(new_data, json_obj)
        print("\nNew configurations saved to: " + new_file)


def startup_display(passed_file):
    """Function at start up that loads data from a JSON file and displays clean content
    
    Arguments:
        passed_file {File Path} -- String value that contains path for the file to work with
    Returns:
        None - Directly prints the contents of the current file with clean output"""
    
    loaded_data = load_data(passed_file)
    display = display_data(loaded_data)
    print(display)
        

def validate_data(passed_value, passed_type, passed_data):
    """Function that validates input information from user regarding the removal of values
    
    Arguments:
        passed_value {String Value} -- String value that is to be validated
        passed_type {String Value} -- String value indicating the type of validation to execute
        passed_data {Dictionary Item} -- Dictionary object containing items to compare for validation
        
    Returns:
        True -- if value passes validation | False -- if value fail validation"""
    
    #Validation process called from remove_data() function
    if passed_type == 'remove':
        bad_keys = ['safe mode', 'memory', 'error log']

        if passed_value not in bad_keys:
            return True
        else:
            return False
    
    #Validation process called from add_data() function
    elif passed_type == 'add':
        if passed_value not in passed_data:
            return True
        else:
            return False
    
    #Validation process called from modify_data() function
    elif passed_type == 'modify':
        if passed_value in passed_data:
            return True
        else:
            return False


    