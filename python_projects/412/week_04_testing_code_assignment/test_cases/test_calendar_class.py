#IT 412 - Eric Lovell - Test the Calendar Class

import unittest
from classes.calendar import Calendar
from classes.event import Event

class TestCalendarClass(unittest.TestCase):
    """Test the calendar class"""

    def setUp(self):
        """Create an instance of the Calendar class for testing all class functions"""

        self.test_calendar = Calendar("Test Calendar", "Eric Lovell")
        self.test_event = Event('TestEvent', '09-04-2023', '10:00', 'recurring' )

    
    def test_add_event_success(self):
        """Test adding an event to the calendar list"""

        self.test_calendar.addEvent(self.test_event)
        self.assertIn(self.test_event, self.test_calendar.all_events)


    def test_remove_event_success(self):
        """Test removing an event from the calendar list"""

        self.test_calendar.addEvent(self.test_event)
        self.test_calendar.removeEvent(self.test_event.name)
        self.assertNotIn(self.test_event, self.test_calendar.all_events)
    