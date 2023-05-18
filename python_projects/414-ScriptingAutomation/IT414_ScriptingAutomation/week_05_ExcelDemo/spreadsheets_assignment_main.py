#IT 414 - Eric Lovell - Spreasheets Assignment Main
from regex.regex_functions import *
from functions.webscrape_functions import *
from functions.excel_functions import *
from functions.ezsheets_functions import *
import requests
from bs4 import BeautifulSoup

my_url = "https://ool-content.walshcollege.edu/CourseFiles/IT/IT414/MASTER/Week05/WI20-Assignment/sales_data.html"

request = requests.get(my_url)

try:
    getHTML(my_url)
except:
    pass

#Manipulating data pulled from webpage
webpage = open("downloads/erp_data.html")
erp_soup = BeautifulSoup(webpage, "lxml")
my_strings = erp_soup.findAll("td", {"height" : ["30"]})
my_numerical_data = erp_soup.findAll("td", {"align" : ["right"]})

product_list = getProductList(my_strings)
quantity_list = getQuantityList(my_numerical_data)

spreadSheetSetup(product_list, quantity_list)
createEZSheets(product_list, quantity_list)
#getAverage(quantity_list)


