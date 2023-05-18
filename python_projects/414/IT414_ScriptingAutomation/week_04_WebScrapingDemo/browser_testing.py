from selenium import webdriver
from selenium.webdriver.common.by import By
import time

my_browser = webdriver.Chrome("chromedriver.exe")
my_browser.get("https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week04/WI20-website-testing-sites/demonstration/")

email_field = my_browser.find_element(By.ID, 'inputEmail')
#email_field.send_keys("admin@myhome.com")
email_field.send_keys("admin@myhome.com")

password_field = my_browser.find_element(By.ID,'inputPassword')
password_field.send_keys("superSecure")

submit_button = my_browser.find_element(By.ID, 'my_submit')
submit_button.click()

error_alert = my_browser.switch_to.alert
error_alert.accept()

password_field.clear()
password_field.send_keys("superSecur3")
submit_button.click()

checkboxes = my_browser.find_elements(By.TAG_NAME, "input")
for item in checkboxes:
    item_type = item.get_attribute("type")
    if item_type == "checkbox":
        item_val = item.get_attribute("value")
        if item_val == "Galaxy J-7" or item_val == "Galaxy-Tab-A-2016":
            item.click()

save_button = my_browser.find_element(By.ID, "save_button")
save_button.click()

block_alert = my_browser.switch_to.alert
block_text = block_alert.text
block_alert.accept()

if "Galaxy J-7" in block_text and "Galaxy-Tab-A-2016" in block_text:
    my_browser.save_screenshot("screenshot.png")

page_buttons = my_browser.find_elements(By.TAG_NAME, "button")

for button in page_buttons:
    if button.text == "Logout":
        button.click()
        break
    
my_browser.close()
time.sleep(120000)