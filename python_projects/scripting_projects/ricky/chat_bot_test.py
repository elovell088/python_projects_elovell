#Worlds Best Script - Written by: Eric Lovell

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser
import time
from pathlib import Path

# Create a new instance of the Chrome driver
url = "https://www.macomb.edu/"
browser = webdriver.Chrome()
browser.get(url)


time.sleep(1)
browser.close()

root_path = Path.cwd()
for dirpath, dirnames, filenames in os.walk(root_path):
    for filename in filenames:
        if filename == 'index.html':
            full_path = os.path.join(dirpath, filename)
        else:
            full_path = ""
print(full_path)
"""
file_path = 'C:/Users/Eric Lovell/Documents/Python Projects/python_projects_elovell/python_projects/scripting_projects/ricky/index.html'

 # Path to your Chrome executable
fifty_count = 0
while fifty_count < 2:
    time.sleep(1)
    webbrowser.open_new(full_path)
    fifty_count += 1
"""


"""
#CrashSystem LOLOL
never_ending_count = 0
while never_ending_count < 1:
# Open the HTML file in Chrome
    webbrowser.open(file_path, new=2)
"""

"""
count = 0
while count < 5:
    next_url = "https://www.macomb.edu/programs-courses/index.html"
    browser.get(next_url)

    next_url = "https://www.macomb.edu/programs-courses/area-interest/index.html"
    browser.get(next_url)

    next_url = "https://www.macomb.edu/programs-courses/area-interest/business-hospitality-culinary.html"
    browser.get(next_url)

    next_url = "https://www.macomb.edu/programs-courses/area-interest/health.html"
    browser.get(next_url)

    next_url = "https://www.macomb.edu/programs-courses/area-interest/science-math.html"
    browser.get(next_url)

    next_url = "https://www.macomb.edu/programs-courses/area-interest/undecided.html"
    browser.get(next_url)

    next_url = "https://www.macomb.edu/programs-courses/area-interest/public-safety.html"
    browser.get(next_url)

    count += 1
"""