#IT 412 - Eric Lovell - Function Library for Week 4 Problem 1

def getMonth():
    """Prompts the user to provide input for the month"""

    ret_month = input("Please enter the month: ")
    month_validated = False
    while not month_validated:
        month_validated = validate_month(ret_month) 
        
        if not month_validated:
            ret_month = input("You entered an invalid character. Please try again: ")
            month_validated = validate_month(ret_month)
    
    return ret_month

def getDay():
    """Prompts the user to provide input for the day"""

    ret_day = input("Please enter the day: ")
    day_validated = False
    while not day_validated:
        validation_result = validate_day(ret_day)
        if validation_result == True:
            day_validated = True
            return ret_day
        else:
            ret_day = input("You entered an invalid character. Please try again: ")


def getYear():
    """Prompts the user to provide input for the year"""

    ret_year = input("Please enter the year: ")
    year_validated = False
    while not year_validated:
        validation_result = validate_year(ret_year)
        if validation_result == True:
            year_validated = True
            return ret_year
        else:
            ret_year = input("You entered an invalid character. Please try again: ")


def validate_month(passed_month):
    """Validates whether or not a person's input for month is valid"""

    passed_month = passed_month.strip()

    if passed_month:
        try:
            passed_month = int(passed_month)
            if passed_month <= 12:
                return True
            else:
                return False

        except:
            return False
    else:
        return False

def validate_day(passed_day):
    """Validates whether or not a person's input for day of the month is valid"""

    passed_day = passed_day.strip()

    if passed_day:
        try:
            passed_day = int(passed_day)
            if passed_day <= 31:
                return True
            else:
                return False

        except:
            return False
    else:
        return False

def validate_year(passed_year):
    """Validates whether or not a person's input for year is valid"""

    passed_year = passed_year.strip()

    if passed_year:
        try:
            passed_year = int(passed_year)
            return True

        except:
            return False
    else:
        return False


def cleanOutput(passed_month, passed_day, passed_year):
    """Returns clean date output"""

    output_string = passed_month.strip() + "/" + passed_day.strip() + "/" + passed_year.strip()

    return output_string


