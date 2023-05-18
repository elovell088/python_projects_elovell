#IT 414 - Eric Lovell - Regex Functions
import re

def searchForFloat(passed_string):
    """Function that searches a string value for the pattern 'first name'
    Arguments:
        passed_string {String Value} -- String value that the function will iterate through
    Returns:
        True -- If the pattern is found | False -- if the pattern is not found"""
    
    floatRegEx = re.compile(r'\d{1,3}(,\d{3})*\.\d{2}')
    searchForFloats = floatRegEx.search(passed_string)

    if searchForFloats is None:
        return False
    else:
        return True


def searchForDate(passed_string):
    """Function that searches a string value for the pattern 'first name'
    Arguments:
        passed_string {String Value} -- String value that the function will iterate through
    Returns:
        True -- If the pattern is found | False -- if the pattern is not found"""
    
    dateRegEx = re.compile(r'\d{1,2}\/\d{1,2}\/\d{4}')
    searchForDate = dateRegEx.search(passed_string)

    if searchForDate is None:
        return False
    else:
        return True
    

def searchForAlpha(passed_string):
    """Function that searches a string value for the pattern 'first name'
    Arguments:
        passed_string {String Value} -- String value that the function will iterate through
    Returns:
        True -- If the pattern is found | False -- if the pattern is not found"""
    
    alphaRegEx = re.compile(r'[a-zA-Z]+')
    searchForAlpha = alphaRegEx.search(passed_string)

    if searchForAlpha is None:
        return False
    else:
        return True


