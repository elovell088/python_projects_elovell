#IT414 - Eric Lovell - Excel Functions
import requests
from regex.regex_functions import *
import requests


def getHTML(passed_url):
    """"""
    request = requests.get(passed_url)

    if request.status_code == 200:
        erp_data = open("downloads/erp_data.html", "wb")
        for data_chunk in request .iter_content(100000):
            erp_data.write(data_chunk)


def getProductList(passed_html_strings):
    """"""
    product_list = []
    temp_list = []
    
    for item in passed_html_strings:
        isAlpha = searchForAlpha(item.text)
        if isAlpha:
            temp_list.append(item.text.strip())

    del temp_list[0:6]
    count = 3

    while count < len(temp_list):
        product_list.append(temp_list[count])
        
        count += 3
    
    return(product_list)



def getQuantityList(passed_html_strings):
    """"""
    quantity_list = []

    for item in passed_html_strings:
        isFloat = searchForFloat(item.text)
        isDate = searchForDate(item.text)
        isAlpha = searchForAlpha(item.text)
        if isFloat or isDate:
            pass
        elif isAlpha:
            pass
        else:
            quantity_list.append(item.text.strip())  

    return quantity_list