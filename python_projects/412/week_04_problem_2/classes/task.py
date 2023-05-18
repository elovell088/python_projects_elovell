#IT 412 - Eric Lovell -Task Class for Lecture Problem 2

class Task():
    """Virtual Representation for a task"""

    def __init__(self, name, description, default_time):
        """Constructor for the Task class"""
        self.name = name
        self.description = description
        self.default_time = default_time

    
    def increase_time(self, passed_default=1):
        """Method that increases the default time of a task"""
        
        self.default_time += passed_default

    
    def decrease_time(self, passed_default=1):
        """Method that decrease the default time of a task"""

        self.default_time = self.default_time - passed_default
    

    def reset_time(self):
        """Method that resets the time value back to zero"""

        self.default_time = 0

        
