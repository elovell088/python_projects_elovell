#IT 410 - Eric Lovell - While Loops Assignment#

def name_validation(passed_name):
    """Validates name information entered by user"""

    if passed_name:
        return True
    else:
        print("invalid")
        return False

name_val = input("enter a vluee")
name_validation(name_val)

