#IT 410 - Eric Lovell - Classes Assignment#

#Create class for person and general organizational information
class Person:
    """Class that represents a person and their general information"""
    def __init__(self, name, email, id, type):
        """Initialize person variables"""
        self.name = name
        self.email = email
        self.id = id
        self.type = type
                
#Create instructor class that inherits person and initializes its own unique variables
class Instructor(Person):
    """Class that inherits person and represents an instructor"""
    def __init__(self, name, email, id, type, degree, institution):
        """Initialize Instructor variables"""
        super().__init__(name, email, id, type)
        self.degree = degree
        self.institution = institution
    #Function that appends instructor information to list
    def append_instructor_info(self, passed_list):
        """Appends student information to list"""
        
        passed_list.append({'type' : self.type,
                            'id' : self.id, 
                            'name' : self.name, 
                            'email' : self.email, 
                            'degree' : self.degree,
                            'institution' : self.institution})

#Create student class that inherits person and initializes its own unique variables
class Student(Person):
    """Class that inherits person and represents a student"""
    def __init__(self, name, email, id, type, program):
        """Initialize Student variables"""
        super().__init__(name, email, id, type)
        self.program = program
    #Function that appends student information to list
    def append_student_info(self, passed_list):
        """Appends student information to list"""
        
        passed_list.append({'type' : self.type, 
                            'id' : self.id, 
                            'name' : self.name, 
                            'email' : self.email, 
                            'program' : self.program})
#Create class that holds methods for displaying values in clean output
class CleanOutput():
    """Class for displaying clean output"""
    def __init__(self):
        """Initialize class"""
    #Function that displays an individuals collected information. Search by name
    def displayInformation(self, passed_name, passed_list):
        """Displays information with a clean output"""

        count_index = 0
        output_string = ""
        for search in passed_list:
            if search['name'] == passed_name:
                #Print out information if search criteria involves a student
                if search['type'] == 'student':
                    print("\n Student Information: ")
                    output_string = output_string + " |  Student ID: " + search['id']
                    output_string = output_string + " |  Name: " + search['name'].title()
                    output_string = output_string + " |  Email: " + search['email']
                    output_string = output_string + " |  Program: " + search['program'].title() + "  |" + "\n"
                                
                    count_index = count_index + 1
                #Print out information if search criteria involves an instructor
                else:
                    print("\n Instructor Information: ")
                    output_string = output_string + " |  Instructor ID: " + search['id']
                    output_string = output_string + " |  Name: " + search['name'].title()
                    output_string = output_string + " |  Email: " + search['email']
                    output_string = output_string + " |  Degree: " + search['degree'].title()
                    output_string = output_string + " |  Institution: " + search['institution'].title()+ "  |" + "\n"
                            
                    count_index = count_index + 1
                
            else:
                print("\nSorry, name was not found.")

        return output_string
    
    #Function that displays all information in the college records list with clean output prints instructors, then students.
    def displayList(self, passed_list):
        """Display all information within a list using clean output"""
        count_index = 0
        output_string = ""
        
        print("\n College Records:")
        #Print all instructor entries
        for search in passed_list:
            if search['type'] == 'instructor':
                output_string = output_string + " |  " + search['type'].upper()
                output_string = output_string + " |  Instructor ID: " + search['id']
                output_string = output_string + " |  Name: " + search['name'].title()
                output_string = output_string + " |  Email: " + search['email']
                output_string = output_string + " |  Degree: " + search['degree'].title()
                output_string = output_string + " |  Institution: " + search['institution'].title() + "  |" + "\n"
                            
                count_index = count_index + 1
                
        #Print all student entries
        for search in passed_list:
            if search['type'] == 'student':
                output_string = output_string + " |  " + search['type'].upper()
                output_string = output_string + " |  Student ID: " + search['id']
                output_string = output_string + " |  Name: " + search['name'].title()
                output_string = output_string + " |  Email: " + search['email']
                output_string = output_string + " |  Program: " + search['program'].title() + "  |" + "\n"
                            
                count_index = count_index + 1

        return output_string

#Create class that holds methods to validate a persons information
class Validator():
    """Class for validating user input"""
    def __init__(self):
        """Initialize class"""
    #Function that validates name input
    def validate_name(self):
        """Validates user input for their name"""
        bad_characters = ['@', '#', '(', ')', '_', ',', '/', '\\','!', '"', '$', '%', '^', '&', '*', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}' ]

        name = input("Please enter name: ")
        character_found = False
        while not character_found:
            for character in name:
                if character in bad_characters:
                    character_found = True
                    break 
            if not name or name.isspace():
                character_found = True
            
            if name.isdigit():
                character_found = True
            
            if character_found == True:
                name = input("Sorry, you entered an invalid character. Please try again: ")
                character_found = False
            else:
                name = name.lower()
                return name
    #Function that validates email input
    def validate_email(self):
        """Validates user input for their email"""
        bad_characters = ['#', '(', ')', ',', '/', '\\', '\'','!', '"', '$', '%', '^', '&', '*', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}' ]

        email = input("Please enter your email: ")
        character_found = False
        while not character_found:
            for character in email:
                if character in bad_characters:
                    character_found = True
                    break 
            if not email or email.isspace():
                character_found = True
            
            if character_found == True:
                email = input("Sorry, you entered an invalid character. Please try again: ")
                character_found = False
            else:
                return email
    #Function that validtes id input
    def validate_id(self, person_type):
        """Validate ID input"""
        if person_type == 'student':
            id = input("Please enter your student ID: ")
            validated = False
            while not validated:
                if id.isdigit() and len(id) <= 7:
                    validated = True
                else:
                    id = input("Sorry, you entered invalid characters. Please try again: ")
                    validated = False
            
            return id
        else:
            id = input("Please enter your instructor ID: ")
            validated = False
            while not validated:
                if id.isdigit() and len(id) <= 5:
                    validated = True
                else:
                    id = input("Sorry, you entered invalid characters. Please try again: ")
                    validated = False
            
            return id
    #Create function to validate program, degree, and institution
    def validate_string(self, passed_string):
        """Validates string input for bad characters"""
        bad_characters = ['@', '#', '(', ')', '_', ',', '/', '\\','!', '"', '$', '%', '^', '&', '*', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}' ]

        character_found = False
        while not character_found:
            for character in passed_string:
                if character in bad_characters:
                    character_found = True
                    break 
            if not passed_string or passed_string.isspace():
                character_found = True
            
            if passed_string.isdigit():
                character_found = True
            
            if character_found == True:
                passed_string = input("Sorry, you entered an invalid character. Please try again: ")
                character_found = False
            else:
                return passed_string

            
#--START PROGRAM--#

#List that will hold all the student ane instructor values
college_records = []
#Flag that allows user to terminate program
program_running = True
while program_running:
    #Determine person type
    person_type = input("Are you are a student? (Y/N): ")
    person_type = person_type.lower()

    #Start gathering and validating student information
    if person_type == 'y':
        person_type = 'student'
        student_name = Validator().validate_name()
        student_email = Validator().validate_email()
        student_id = Validator().validate_id(person_type)
        student_program = input("Please enter your program of study: ")

        #Create instance with gathered information
        current_student = Student(student_name, student_email, student_id, person_type, student_program)
        current_student.append_student_info(college_records)
    #Start gathering and validating instructor information
    else:    
        person_type = 'instructor'
        instructor_name = Validator().validate_name()
        instructor_email = Validator().validate_email()
        instructor_id = Validator().validate_id(person_type)
        check_degree = input("Please enter the highest degree you have earned: ")
        instructor_degree = Validator().validate_string(check_degree)
        check_institution = input("Please enter the last institution you graduated from: ")
        instructor_institution = Validator().validate_string(check_institution)

        #Create instance with gathered information
        current_instructor = Instructor(instructor_name, instructor_email, instructor_id, person_type, instructor_degree, instructor_institution)
        current_instructor.append_instructor_info(college_records)


    #Ask user if they would like to view a previous entry - displayInformation method
    view_entry = input("Would you like to view a previous entry? (Y/N):")
    view_entry = view_entry.lower()

    while view_entry != 'n':
        query_name = Validator().validate_name()
        successful_query = CleanOutput().displayInformation(query_name, college_records)
        print(successful_query)
        view_entry = input("Would you like to view another previous entry? (Y/N):")

    #Ask user if they would like to make another entry to the college records list
    user_terminate = input("Would you like to make another entry? (Y/N): ")
    if user_terminate != 'n':
        person_type = ''
        program_running = True
    else:
        #Display all records in college records list - then terminate program
        end_program_display = CleanOutput().displayList(college_records)
        print(end_program_display)
        program_running = False
    
