from classes.validator import *
from classes.student import *
from classes.instructor import *

class Collect:
    """Class for collecting user information - Information is also validated by using Validator() class"""
    def __init__(self):
        """Initialize class"""
    
    def cleanOutput(self, passed_list):
        """Prints content of a list with clean output
        Arguments:
            passed_list {List} -- List that will be printed with clean output
        Returns:
            None -- Prints entire list with clean output"""
   
        count_index = 0
        output_string = ""
        print("\nCollege Records: ")
        while count_index < len(passed_list):
            output_string = output_string + "Index: " + str(count_index)
            output_string = output_string + " | Type: " + passed_list[count_index].type.title() 
            output_string = output_string + " | Name: " + passed_list[count_index].name.title()
            output_string = output_string + " | Email: " + passed_list[count_index].email
            output_string = output_string + " | ID: " + passed_list[count_index].id
            if passed_list[count_index].type == 'student':
                output_string = output_string + " | Program: " + passed_list[count_index].program.title() + "\n"
            else:
                output_string = output_string + " | Degree: " + passed_list[count_index].degree.title()
                output_string = output_string + " | Institution: " + passed_list[count_index].institution.title() + "\n"

            count_index += 1
        
        print(output_string)


    def collect_degree(self):
        """Collects input for highest degree that an instructor has earned and validates for bad characters using Validator() class
        Arguments:
            -- None
        Returns:
            person_degree {String value} -- Validated string value representing a persons highest degree earned"""
        
        person_degree = input("Please enter the highest degree you have earned: ")
        degree_validated = False
        while not degree_validated:
            validator = Validator()
            validator_result = validator.validate_string(person_degree)
            if validator_result == False:
                return person_degree
            else:
                person_degree = input("Sorry, you entered an invalid value. Please try again: ")


    def collect_email(self):
        """Collects input for a persons email and validates for bad characters using Validator() class
        Arguments:
            -- None
        Returns:
            person_email {String value} -- Validated string value representing a persons email"""

        person_email = input("Please enter your email: ")
        email_validated = False
        while not email_validated:
            validator = Validator()
            validator_result = validator.validate_email(person_email)

            if validator_result == False:
                return person_email
            else:
                person_email = input("Sorry, you entered an invalid value. Please try again: ")


    def collect_id(self, passed_type):
        """Collects input for a persons ID and validates for bad characters using Validator() class
        Arguments:
            passed_type {String value} -- String value for person type (Student or Instructor). Both have differing max length requirements for ID values
        Returns:
            person_id {String value} -- Validated string value representing a persons ID"""

        person_id = input("Please enter your ID: ")
        id_validated = False
        while not id_validated:
            validator = Validator()
            validator_result = validator.validate_id(passed_type, person_id)
            if validator_result == True:
                return person_id
            else:
                person_id = input("Sorry, you entered an invalid value. Please try again: ")


    def collect_institution(self):
        """Collects input for a persons email and validates for bad characters using Validator() class
        Arguments:
            -- None
        Returns:
            person_institution {String value} -- Validated string value representing a persons last institution they graduated from"""

        person_institution = input("Please enter the last institution you graduated from: ")
        institution_validated = False
        while not institution_validated:
            validator = Validator()
            validator_result = validator.validate_string(person_institution)
            if validator_result == False:
                return person_institution
            else:
                person_institution = input("Sorry, you entered an invalid value. Please try again: ")

    def collect_name(self):
        """Collects input for a persons name and validates for bad characters using Validator() class
        Arguments:
            -- None
        Returns:
            person_name {String value} -- Validated string value representing a persons name"""

        person_name = input("Please enter name: ")
        name_validated = False
        while not name_validated:
            validator = Validator()
            validator_result = validator.validate_name(person_name)
        
            if validator_result == False:
                return person_name
            else:
                person_name = input("Sorry, you entered an invalid value. Please try again: ")
    
    
    def collect_program(self):
        """Collects input for a students current college program and validates for bad characters using Validator() class
        Arguments:
            -- None
        Returns:
            person_program {String value} -- Validated string value representing a students college program"""

        person_program = input("Please enter your program of study: ")
        program_validated = False
        while not program_validated:
            validator = Validator()
            validator_result = validator.validate_string(person_program)
            if validator_result == False:
                return person_program
            else:
                person_program = input("Sorry, you entered an invalid value. Please try again: ")


    def collect_type(self):
        """Collects input for a persons type (student or instructor) and validates for bad characters
        Arguments:
            -- None
        Returns:
            person_type {String value} -- Validated string value representing a persons type (student or instructor)"""

        person_type = input("Are you a student? (Y/N): ")
        person_type = person_type.lower()
        type_validated = False
        while not type_validated:
            if person_type == 'y':
                person_type = 'student'
                return person_type
            elif person_type == 'n':
                person_type = 'instructor'
                return person_type
            else:
                person_type = input("Sorry, you entered an invalid value. Please try again: ")
                person_type = person_type.lower()


    def queryName(self, passed_list):
        """Collects name input that is used to search for an indivudal and display all their collected information. 
        Arguments:
            passed_list {String value} -- List that is iterated through to verify user's search query is valid
        Returns:
            None - prints an individuals information with clean output from displayInformation method"""

        view_entry = input("Would you like to view a previous entry? (Y/N): ")
        view_entry = view_entry.lower()
        if view_entry == 'y':
            search_list = True
            while search_list:
                c = Collect()
                search_name = c.collect_name()
                name_found = False
                while not name_found:
                    for name in passed_list:
                        if name.name == search_name and name.type == 'student':
                            student_info = Student(name.name, name.email, name.id, name.type, name.program)
                            print_info = student_info.displayInformation(search_name, passed_list)
                            print(print_info)
                            name_found = True
                            break
                        if name.name == search_name and name.type == 'instructor':
                            instructor_info = Instructor(name.name, name.email, name.id, name.type, name.degree, name.institution)
                            print_info = instructor_info.displayInformation(search_name, passed_list)
                            print(print_info)
                            name_found = True
                            break
                
                    if name_found == False:
                            print("Sorry, no information was found for: " + str(search_name) + " -- Try again.")
                            search_name = c.collect_name()

                continue_search = input("Would you like to view another entry? (Y/N): ")
                continue_search = continue_search.lower()
                if continue_search == 'n':
                    break
