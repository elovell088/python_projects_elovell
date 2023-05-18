import pyperclip
import re


def displayData():
    """"""
    allData = str(pyperclip.paste())
    coordList = findAllCoords(allData)
    dollarList = findAllDollars(allData)
    ccList = findAllCC(allData)

    output_string = ""
    count = 0
    while count < len(ccList):
        output_string += str(count) + coordList[count] + " | " + dollarList[count] + " | " + ccList[count] + "\n"
        count += 1
    
    return output_string


def findAllCC(passed_string):
    """"""
    ccRegEx = re.compile(r'\d{3,4} ?\d{3,10} ?\d* ?\d*\d')

    ccList = ccRegEx.findall(passed_string)

    cc_return_list = []
    for cc in ccList:
        cc_return_list.append(cc)
 
    return cc_return_list


def findAllCoords(passed_string):
    """Function that """
    coordRegEx = re.compile(r'(-{0,1}\b\d{1,3})(\.)(\d{3,5})\b(, )(-{0,1}\b\d{1,3})(\.)(\d{3,5})\b')

    coordList = coordRegEx.findall(passed_string)

    coord_return_list = []
    for coord in coordList:
        temp_coord = ""
        for item in coord:
            temp_coord += str(item)
        coord_return_list.append(temp_coord)


    return coord_return_list


def findAllDollars(passed_string):
    """"""
    dollarRegEx = re.compile(r'\$\d,\d\d\d\b')

    dollarList = dollarRegEx.findall(passed_string)

    dollar_return_list = []
    for dollar in dollarList:
        temp_dollar = ""
        for item in dollar:
            temp_dollar += str(item)
        dollar_return_list.append(temp_dollar)


    return dollar_return_list


###--VALIDATION FUNCTIONS--###
def validateCC(passed_cc):
    """"""
    ccRegEx = re.compile(r'\d{3,4} ?\d{3,10} ?\d* ?\d*\d')
    if re.match(ccRegEx, passed_cc):
        return True
    else:
        return False
    

def validateCoord(passed_coord):
    """"""
    coordRegEx = re.compile(r'(-{0,1}\b\d{1,3})(\.)(\d{3,5})\b(, )(-{0,1}\b\d{1,3})(\.)(\d{3,5})\b')
    if re.match(coordRegEx, passed_coord):
        return True
    else:
        return False
    

def validateDollar(passed_dollar):
    """"""
    dollarRegEx = re.compile(r'\${1}\d*,*\d*\d*\d\b')
    if re.match(dollarRegEx, passed_dollar):
        return True
    else:
        return False