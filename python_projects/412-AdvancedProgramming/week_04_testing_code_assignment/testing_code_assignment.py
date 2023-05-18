#IT 412 - Eric Lovell - Main body for Week 4-5 Testing Code Assignment

from classes.event import Event
from classes.calendar import Calendar

program_running = True
while program_running:
    #Welcome prompt - Start gathering calendar information from user
    print("\nWelcome to the Event Calender App!\n")
    calendar_name = input("To begin, please enter the name of your new calendar: ")
    calendar_owner = input("Please enter the name of the owner: ")
    #Create instance of calendar class with input information
    new_calendar = Calendar(calendar_name, calendar_owner)
    
    #Start main program functions
    modifying_calendar = True
    while modifying_calendar:
        new_calendar.program_prompts()
        prompt_choice = input("Please choose from the prompts above: ")

        #ADD EVENT METHOD (Calendar Class)
        if prompt_choice == 'a':
            #Start gathering name, date, time, and type info from user and store them in the new_event instance 
            new_event = Event()
            event_name = input("Enter the event name: ")
            new_event.name = new_event.get_name(event_name)
            event_date = input("Enter the event date - (ex. mm-dd-yyyy): ")
            new_event.date = new_event.get_date(event_date)
            event_time = input("Enter the event time - (ex. hh:mm): ")
            new_event.time = new_event.get_time(event_time)

            print("Select event type from the prompts below: ")
            event_type = input("| (s) - Single Occurence | (r) - Recurring | (f) - Fixed Number of Meetings |: ")
            new_event.type = new_event.get_type(event_type)
            #Add new instance to the calendar list
            new_calendar.addEvent(new_event)

        #DISPLAY CALENDAR METHOD (Calendar Class)
        elif prompt_choice == 'd':
            new_calendar.displayCalendar(new_calendar.all_events)

        #REMOVE EVENT METHOD (Calendar Class)
        elif prompt_choice == 'r':
            remove_event = input("Enter the name of the event you would like to remove: ")
            new_calendar.removeEvent(remove_event)
        #TERMINATE PROGRAM
        elif prompt_choice == 'x':
            modifying_calendar = False
            program_running = False
