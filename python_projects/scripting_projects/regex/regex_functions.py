#IT 414 - Eric Lovell - Regex for WebScrap Assignment
import re

def searchForBadValues(passed_string):
    """Function that searches a string value for the pattern 'email address'
    Arguments:
        passed_string {String Value} -- String value that the function will iterate through
    Returns:
        True -- If the pattern is found | False -- if the pattern is not found"""
    
    badCharRegEx = re.compile(r'^(You said: |Sent at|Bot true said: )|(Just now)\s*$')
    searchForInstall = badCharRegEx.findall(passed_string)

    if searchForInstall is None:
        return False
    else:
        return True


def searchForFirstName(passed_string):
    """Function that searches a string value for the pattern 'first name'
    Arguments:
        passed_string {String Value} -- String value that the function will iterate through
    Returns:
        True -- If the pattern is found | False -- if the pattern is not found"""
    
    installRegEx = re.compile(r'First name|first name')
    searchForInstall = installRegEx.search(passed_string)

    if searchForInstall is None:
        return False
    else:
        return True
    

def searchForLastName(passed_string):
    """Function that searches a string value for the pattern 'last name'
    Arguments:
        passed_string {String Value} -- String value that the function will iterate through
    Returns:
        True -- If the pattern is found | False -- if the pattern is not found"""
    
    installRegEx = re.compile(r'Last name|last name')
    searchForInstall = installRegEx.search(passed_string)

    if searchForInstall is None:
        return False
    else:
        return True
    

def searchForPhone(passed_string):
    """Function that searches a string value for the pattern 'email address'
    Arguments:
        passed_string {String Value} -- String value that the function will iterate through
    Returns:
        True -- If the pattern is found | False -- if the pattern is not found"""
    
    installRegEx = re.compile(r'phone number|Phone number')
    searchForInstall = installRegEx.search(passed_string)

    if searchForInstall is None:
        return False
    else:
        return True