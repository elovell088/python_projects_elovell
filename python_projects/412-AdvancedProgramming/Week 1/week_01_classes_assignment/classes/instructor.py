from classes.person import Person

class Instructor(Person):
    """Class that inherits person and represents an instructor"""
    def __init__(self, name, email, id, type, degree, institution):
        """Initialize Instructor variables"""
        super().__init__(name, email, id, type)
        self.degree = degree
        self.institution = institution
    
    def displayInformation(self,passed_name, passed_list):
        """Displays all collected information for a individual instructor with clean output
        Arguments:
            passed_list {List} -- Passed list to find all the instructor information to print
        Returns:
            output_string {String value} -- Constains string values for all collection for an instructor with clean output"""

        count_index = 0
        output_string = "\nInstructor Information: \n"
        while count_index < len(passed_list):
            if passed_name == passed_list[count_index].name:
                output_string = output_string + "Index: " + str(count_index)
                output_string = output_string + " | Type: " + passed_list[count_index].type.title() 
                output_string = output_string + " | Name: " + passed_list[count_index].name.title()
                output_string = output_string + " | Email: " + passed_list[count_index].email
                output_string = output_string + " | ID: " + passed_list[count_index].id
                output_string = output_string + " | Degree: " + passed_list[count_index].degree.title()
                output_string = output_string + " | Institution: " + passed_list[count_index].institution.title() + "\n"
            
            count_index += 1
        

        return output_string