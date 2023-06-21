#Chat box test - written by: Eric Lovell
#Tests MCC chat bot to ensure the correct responses based on specific input
#THIS IS FILE FOR TESTING - NOT YET FINALIZED

from selenium import webdriver
from selenium.webdriver.common.by import By

import webbrowser
import time

# Create a new instance of the Chrome driver
url = "https://www.macomb.edu/"
browser = webdriver.Chrome()
browser.get(url)

time.sleep(1)

file_path = 'index.html'
 # Path to your Chrome executable

# Open the HTML file in Chrome
webbrowser.open(file_path)

time.sleep(5)

"""
# Find the message box by class name
message_box = browser.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div[2]/div/div[2]/div[5]/div/form/input")
message_box.send_keys(question)

send_button = browser.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div[2]/div/div[2]/div[5]/div/button")
send_button.click()

time.sleep(.05)
"""

"""
message_box.send_keys("How do I submit a dental claim?")
send_button.click()

time.sleep(2)

message_box.send_keys("Where are the HR policies located?")
send_button.click()

send_button = browser.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div[2]/div/div[2]/div[5]/div/button")
send_button.click()
time.sleep(1)
get_chat_history = browser.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div[2]/div/div[2]/div[3]")
chat_history = get_chat_history.text

time.sleep(2)
print(chat_history)
print("\n\nSPLIT\n\n")
pattern = re.compile(r'^(You said: |You said:|Sent at|Bot true said:|Bot true said: )|(Just now)\s*$', re.MULTILINE)
date_and_time_regex = re.compile(r'\b[a-zA-Z]+\s+\d+\s+at\s+\d{1,2}:\d{2}\s+(?:AM|PM)\b')
# Remove matched substrings using compiled pattern with re.sub
output_string = pattern.sub('', chat_history)

# Print the output
print(output_string)
"""