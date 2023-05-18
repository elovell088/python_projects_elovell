#
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time 

request = requests.get(url)

if request.status_code == 200:
    chat_data = open("downloads/weather_data.html", "wb")
    for data_chunk in request .iter_content(100000):
        chat_data.write(data_chunk)