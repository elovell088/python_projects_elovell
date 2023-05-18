#IT 414 - Eric Lovell - Regex Functions
import re


def findAllRelativeRoot(passed_string):
    """"""
    relativeRootRegex = re.compile(r'(\.\.){2}(/)')

    relativeRootList = relativeRootRegex.findall(passed_string)

    relative_root_return_list = []
    for root in relativeRootList:
        temp_root = ""
        for item in root:
            temp_root += str(item)
        relative_root_return_list.append(temp_root)
    
    return(relative_root_return_list)



def findAllInstall(passed_string):
    """"""
    installRegEx = re.compile(r'install')

    installList = installRegEx.findall(passed_string)
    
    install_return_list = []
    for install in installList:
        install_return_list.append(install)
 
    return install_return_list


def findAllPhpLogin(passed_string):
    """"""

def findAllSelect(passed_string):
    """"""
    selectRegEx = re.compile(r'select')

    selectList = selectRegEx.findall(passed_string)
    
    select_return_list = []
    for select in selectList:
        select_return_list.append(select)
 
    return select_return_list


def processFiles():
    """"""
    



def searchforHttpStatus(passed_string):
    """"""
    httpStatusRegEx = re.compile(r' 403 ')
    
    searchForHttpStatus = httpStatusRegEx.search(passed_string)

    if searchForHttpStatus is None:
        return False
    else:
        return True



def searchForInstall(passed_string):
    """"""
    installRegEx = re.compile(r'install')
    searchForInstall = installRegEx.search(passed_string)

    if searchForInstall is None:
        return False
    else:
        return True
        


def searchForRelativeRoot(passed_string):
    """"""
    relativeRootRegEx = re.compile(r'(\.\.){2}(/)')

    searchForRelativeRoot = relativeRootRegEx.search(passed_string)

    if searchForRelativeRoot is None:
        return False
    else:
        return True

def searchForScript(passed_string):
    """"""
    scriptRegEx = re.compile(r'(c:\|/)')
    searchForScript = scriptRegEx.search(passed_string)


def searchForSelect(passed_string):
    """"""
    selectRegEx = re.compile(r'select')
    searchForSelect = selectRegEx.search(passed_string)

    if searchForSelect is None:
        return False
    else:
        return True
        """
        if passed_string == searchForSelect: #.group():
            return True
        else:
            return False
        """

def searchForLoginPhp(passed_string):
    """/wp-login.php?action=register"""
    
    loginPhpRegEx = re.compile(r'/wp-login\.php\?action=register')
    searchForLoginPhp = loginPhpRegEx.search(passed_string)

    if searchForLoginPhp is None:
        return False
    else:
        return True



    """
    testForInstall = findAllInstall.search(passed_date)

    if test is None:
        print("You did not enter a proper date.")
        return False
    else:
        if passed_date == dateTest.group():
            print("You entered a proper date!")
            return True
        else:
            print("You did not enter a proper date")
            return False
    """



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