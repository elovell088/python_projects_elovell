#IT 412 - Eric Lovell - Calendar Class for Week 4-5 Assignment

class Calendar():
    """Virtual representation of a calendar"""

    def __init__(self, name, owner):
        """Constructor for the calendar class"""

        self.name = name
        self.owner = owner
        self.all_events = []
        

    def addEvent(self, passed_event):
        """Method that adds an event to the list of events
        Arguments:
            Passed_event {Class Instance} -- Instance of Event Class that will be added to Calendar list
        Return
            None -- Just adds an event to the caldedar list and prints that it has been updated"""

        self.all_events.append(passed_event)
        print("\n Your calendar has been updated with a new event: " + passed_event.name)

    
    def displayCalendar(self, passed_list):
        """Print event information within the calendar with clean output
        Arguments:
            passed_list {List} -- List that will be printed with clean output
        Returns:
            None -- Prints entire list with clean output"""
        
        print("\n" + self.name + ":")

        if len(passed_list) <= 0:
            print("No events to show. ")
        else:
            count_index = 0
            output_string = ""
            while count_index < len(passed_list):
                output_string = output_string + "Event Index: " + str(count_index)
                output_string = output_string + " | Name: " + passed_list[count_index].name
                output_string = output_string + " | Date: " + passed_list[count_index].date
                output_string = output_string + " | Time: " + passed_list[count_index].time
                output_string = output_string + " | Type: " + passed_list[count_index].type.title() + "\n"

                count_index += 1
            
            print(output_string)
        

    def program_prompts(self):
        """Function that provides prompts to the user with clean output
        Arguments:
            None
        Returns:
            None -- Directly prints prompt with clean output"""

        output_string = ''
        output_string = output_string + "\nPrompts\n"
        output_string = output_string + "| 'a' to add new event     | 'r' to remove an event     | \n"
        output_string = output_string + "| 'd' to display calendar  | 'x' to termintate program  | \n"

        print(output_string)
    

    def removeEvent(self, passed_name):
        """Method that removes an event from the list of events
        Arguments:
            passed_name {String Value} -- String value containing the event name to remove from calendar
        Return:
            None -- Just removes the event object from the calendar list and prints message"""

        item_to_remove = passed_name
        
        index_count = 0
        event_found = False
        while index_count < len(self.all_events):
            if item_to_remove == self.all_events[index_count].name:
                self.all_events.remove(self.all_events[index_count])
                event_found = True
            
            index_count += 1
        
        if not event_found:
            print("Sorry, the event, " + item_to_remove + " doesn't exist. ")
        else:
            print("\n" + item_to_remove + " has been removed from the calendar.")
