#IT 414 - Eric lovell - Web Scraping Functions
from regex.regex_functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import shutil
import time

#Get webpage.html
my_browser = webdriver.Chrome("chromedriver.exe")
my_browser.get("https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week04/WI20-website-testing-sites/assignment/index.php")

#Error messages
fname_error_messages = ["First name is required", "Please check the length of the first name field"]
lname_error_messages = ["Last name is required", "Please check the length of the last name field"]
phone_error_messages = ["Phone number is required", "Your phone number is an incorrect format"]
email_error_messages = ["Your email address is in an incorrect format"]

#Lists that contains invalid entries
invalid_first_names = ['', ' ', 'ab', 'morethantenchars', '1']
invalid_last_names = ['', ' ', 'a', 'morethanfifteenchars', '1']
invalid_emails = ['eric', 'erci@yahoo', '@gmail.com', 'student01@  gmail']
invalid_phone_numbers = ['', ' ', '111-222-333333', '11111111111', '1111-222-22222']

#Lists containing valid entries
valid_first_names = ["Eri", "Henry", "Billy", "Batman", "tenletters"]
valid_last_names = ["Lo", "Petz", "Schnier", "Van-trues", "fifteenletterss"]
valid_emails = ["test1@gmail.com", "test2@gmail.com", "test3@gmail.com", "test4@gmail.com", "test5@gmail.com"]
valid_phones = ['111-222-4444', '1234567891', '333$333$4444', '111^222^3333', '111>222>3333']

#File path to images folder
image_file_path = "week_04_WebScrapingAssignment/images/"



#--TEST FOR INVALID INPUT--#
def invalid_email_test(passed_test_count):
    """Function that tests the email field of a webpage with invalid email strings
    Arguments:
        passed_test_count {Integer} -- Integer value representing the test number. Is input into file name
    Returns:
        None -- Performs necessary key strokes and mouse clicks, and screenshots each test"""
    
    for email in invalid_emails:
        #Find elements and send keys to field
        email_field = my_browser.find_element(By.ID, "emailAddress")
        email_field.send_keys(email)

        #Save Screenshot
        my_browser.save_screenshot("screenshot.png")
        shutil.move("./screenshot.png", image_file_path + "email_screenshot-" + str(passed_test_count) + ".png")

        #Find and click submit buitton
        my_submit_button = my_browser.find_element(By.ID, "my_submit")
        my_submit_button.click()

        #Search for Errors
        error_alert_exists = False
        try:
            error_alert = my_browser.switch_to.alert
            error_messages = error_alert.text
            error_alert_exists = searchForEmail(error_messages)
            error_alert.accept()
        except:
            pass

        if error_alert_exists:
            shutil.move(image_file_path + "email_screenshot-" + str(passed_test_count) + ".png", image_file_path + "passed_email_screenshot-" + str(passed_test_count) + ".png")
        
        passed_test_count += 1
        email_field.clear()
        time.sleep(.1)


def invalid_fname_test(passed_test_count):
    """Function that tests the first name field of a webpage with invalid first name strings
    Arguments:
        passed_test_count {Integer} -- Integer value representing the test number. Is input into file name
    Returns:
        None -- Performs necessary key strokes and mouse clicks, and screenshots each test"""
    
    for name in invalid_first_names:
        #Find elements and send keys to field
        first_name_field = my_browser.find_element(By.ID, "firstName")
        first_name_field.send_keys(name)

        #Save Screenshot
        my_browser.save_screenshot("screenshot.png")
        shutil.move("./screenshot.png", image_file_path + "fname_screenshot-" + str(passed_test_count) + ".png")

        #Find and click submit buitton
        my_submit_button = my_browser.find_element(By.ID, "my_submit")
        my_submit_button.click()

        #Search for Errors
        error_alert_exists = False
        try:
            error_alert = my_browser.switch_to.alert
            error_messages = error_alert.text
            error_alert_exists = searchForFirstName(error_messages)
            error_alert.accept()
        except:
            pass

        if error_alert_exists:
            shutil.move(image_file_path + "fname_screenshot-" + str(passed_test_count) + ".png", image_file_path + "passed_fname_screenshot-" + str(passed_test_count) + ".png")
        
        passed_test_count += 1
        first_name_field.clear()
        time.sleep(.1)



def invalid_lname_test(passed_test_count):
    """Function that tests the last name field of a webpage with invalid last name strings
    Arguments:
        passed_test_count {Integer} -- Integer value representing the test number. Is input into file name
    Returns:
        None -- Performs necessary key strokes and mouse clicks, and screenshots each test"""
    for name in invalid_last_names:
        #Find elements and send keys to field
        last_name_field = my_browser.find_element(By.ID, "lastName")
        last_name_field.send_keys(name)

        #Save Screenshot
        my_browser.save_screenshot("screenshot.png")
        shutil.move("./screenshot.png", image_file_path + "lname_screenshot-" + str(passed_test_count) + ".png")

        #Find and click submit buitton
        my_submit_button = my_browser.find_element(By.ID, "my_submit")
        my_submit_button.click()

        #Search for Errors
        error_alert_exists = False
        try:
            error_alert = my_browser.switch_to.alert
            error_messages = error_alert.text
            error_alert_exists = searchForLastName(error_messages)
            error_alert.accept()
        except:
            pass

        if error_alert_exists:
            shutil.move(image_file_path + "lname_screenshot-" + str(passed_test_count) + ".png", image_file_path + "passed_lname_screenshot-" + str(passed_test_count) + ".png")
        
        passed_test_count += 1
        last_name_field.clear()
        time.sleep(.1)




def invalid_phone_test(passed_test_count):
    """Function that tests the phone field of a webpage with invalid phone strings
    Arguments:
        passed_test_count {Integer} -- Integer value representing the test number. Is input into file name
    Returns:
        None -- Performs necessary key strokes and mouse clicks, and screenshots each test"""
    for phone in invalid_phone_numbers:
        #Find elements and send keys to field
        email_field = my_browser.find_element(By.ID, "phoneNumber")
        email_field.send_keys(phone)

        #Save Screenshot
        my_browser.save_screenshot("screenshot.png")
        shutil.move("./screenshot.png", image_file_path + "phone_screenshot-" + str(passed_test_count) + ".png")

        #Find and click submit buitton
        my_submit_button = my_browser.find_element(By.ID, "my_submit")
        my_submit_button.click()

        #Search for Errors
        error_alert_exists = False
        try:
            error_alert = my_browser.switch_to.alert
            error_messages = error_alert.text
            error_alert_exists = searchForPhone(error_messages)
            error_alert.accept()
        except:
            pass

        if error_alert_exists:
            shutil.move(image_file_path + "phone_screenshot-" + str(passed_test_count) + ".png", image_file_path + "passed_phone_screenshot-" + str(passed_test_count) + ".png")
        
        passed_test_count += 1
        email_field.clear()
        time.sleep(.1)


def successful_entry_test():
    """Function that tests all fields with valid strings and submits. Brings user thanks you page, which is screenshot.
    Arguments:
        None
    Returns:
        None -- Performs necessary key strokes and mouse clicks, and screenshots each test"""
    
    #Find necessary elements on page for testing
    first_name_field = my_browser.find_element(By.ID, "firstName")
    last_name_field = my_browser.find_element(By.ID, "lastName")
    email_address_field = my_browser.find_element(By.ID, "emailAddress")
    phone_number_field = my_browser.find_element(By.ID, "phoneNumber")

    #Send key Strokes
    first_name_field.send_keys(valid_first_names[0])
    last_name_field.send_keys(valid_last_names[0])
    email_address_field.send_keys(valid_emails[0])
    phone_number_field.send_keys(valid_phones[0])

    #Save Screenshot
    my_browser.save_screenshot("correct_input_test.png")
    shutil.move("correct_input_test.png", image_file_path + "correct_input_test.png")

    #Find and click submit buitton
    my_submit_button = my_browser.find_element(By.ID, "my_submit")
    my_submit_button.click()

    #Save screenshot of the thank you page
    my_browser.save_screenshot("screenshot.png")
    shutil.move("screenshot.png", image_file_path + "Success-thankyoupage.png")

    #Close Browser
    my_browser.close()

    #Keeps browser from closing
    time.sleep(1)

    

#--TEST FOR VALID INPUT--#
def valid_email_test(passed_test_count):
    """Function that tests the email field of a webpage with valid email strings
    Arguments:
        passed_test_count {Integer} -- Integer value representing the test number. Is input into file name
    Returns:
        None -- Performs necessary key strokes and mouse clicks, and screenshots each test"""
    for email in valid_emails:
        #Find elements and send keys to field
        email_field = my_browser.find_element(By.ID, "emailAddress")
        email_field.send_keys(email)

        #Save Screenshot
        my_browser.save_screenshot("screenshot.png")
        shutil.move("./screenshot.png", image_file_path + "email_screenshot-" + str(passed_test_count) + ".png")

        #Find and click submit buitton
        my_submit_button = my_browser.find_element(By.ID, "my_submit")
        my_submit_button.click()

        #Search for Errors
        error_alert_exists = False
        try:
            error_alert = my_browser.switch_to.alert
            error_messages = error_alert.text
            error_alert_exists = searchForEmail(error_messages)
            error_alert.accept()
        except:
            pass

        if error_alert_exists:
            shutil.move(image_file_path + "email_screenshot-" + str(passed_test_count) + ".png", image_file_path + "passed_email_screenshot-" + str(passed_test_count) + ".png")
        
        passed_test_count += 1
        email_field.clear()
        time.sleep(.1)


def valid_fname_test(passed_test_count):
    """Function that tests the first name field of a webpage with valid first name strings
    Arguments:
        passed_test_count {Integer} -- Integer value representing the test number. Is input into file name
    Returns:
        None -- Performs necessary key strokes and mouse clicks, and screenshots each test"""
    
    for name in valid_first_names:
        #Find elements and send keys to field
        first_name_field = my_browser.find_element(By.ID, "firstName")
        first_name_field.send_keys(name)

        #Save Screenshot
        my_browser.save_screenshot("screenshot.png")
        shutil.move("./screenshot.png", image_file_path + "fname_screenshot-" + str(passed_test_count) + ".png")

        #Find and click submit buitton
        my_submit_button = my_browser.find_element(By.ID, "my_submit")
        my_submit_button.click()

        #Search for Errors
        error_alert_exists = False
        try:
            error_alert = my_browser.switch_to.alert
            error_messages = error_alert.text
            error_alert_exists = searchForFirstName(error_messages)
            error_alert.accept()
        except:
            pass

        if error_alert_exists:
            shutil.move(image_file_path + "fname_screenshot-" + str(passed_test_count) + ".png", image_file_path + "passed_fname_screenshot-" + str(passed_test_count) + ".png")
        
        passed_test_count += 1
        first_name_field.clear()
        time.sleep(.1)


def valid_lname_test(passed_test_count):
    """Function that tests the last name field of a webpage with valid last name strings
    Arguments:
        passed_test_count {Integer} -- Integer value representing the test number. Is input into file name
    Returns:
        None -- Performs necessary key strokes and mouse clicks, and screenshots each test"""
    
    for name in valid_last_names:
        #Find elements and send keys to field
        last_name_field = my_browser.find_element(By.ID, "lastName")
        last_name_field.send_keys(name)

        #Save Screenshot
        my_browser.save_screenshot("screenshot.png")
        shutil.move("./screenshot.png", image_file_path + "lname_screenshot-" + str(passed_test_count) + ".png")

        #Find and click submit buitton
        my_submit_button = my_browser.find_element(By.ID, "my_submit")
        my_submit_button.click()

        #Search for Errors
        error_alert_exists = False
        try:
            error_alert = my_browser.switch_to.alert
            error_messages = error_alert.text
            error_alert_exists = searchForLastName(error_messages)
            error_alert.accept()
        except:
            pass

        if error_alert_exists:
            shutil.move(image_file_path + "lname_screenshot-" + str(passed_test_count) + ".png", image_file_path + "passed_lname_screenshot-" + str(passed_test_count) + ".png")
        
        passed_test_count += 1
        last_name_field.clear()
        time.sleep(.1)


def valid_phone_test(passed_test_count):
    """Function that tests the phone field of a webpage with valid phone strings
    Arguments:
        passed_test_count {Integer} -- Integer value representing the test number. Is input into file name
    Returns:
        None -- Performs necessary key strokes and mouse clicks, and screenshots each test"""
    
    for phone in valid_phones:
        #Find elements and send keys to field
        email_field = my_browser.find_element(By.ID, "phoneNumber")
        email_field.send_keys(phone)

        #Save Screenshot
        my_browser.save_screenshot("screenshot.png")
        shutil.move("./screenshot.png", image_file_path + "phone_screenshot-" + str(passed_test_count) + ".png")

        #Find and click submit buitton
        my_submit_button = my_browser.find_element(By.ID, "my_submit")
        my_submit_button.click()

        #Search for Errors
        error_alert_exists = False
        try:
            error_alert = my_browser.switch_to.alert
            error_messages = error_alert.text
            error_alert_exists = searchForPhone(error_messages)
            error_alert.accept()
        except:
            pass

        if error_alert_exists:
            shutil.move(image_file_path + "phone_screenshot-" + str(passed_test_count) + ".png", image_file_path + "passed_phone_screenshot-" + str(passed_test_count) + ".png")
        
        passed_test_count += 1
        email_field.clear()
        time.sleep(.1)



    