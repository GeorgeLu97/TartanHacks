import icalendar

class Event:
    def __init__(self, component):
        pass

class Schedule:
    def __init__(self,filename):
        self.events = []
        with open(filename, "rb") as inf:
            schedule = icalendar.Calendar.from_ical(inf.read())
        for component in schedule.walk():
            if component.name != "VEVENT":
                self.events.append(Event(component))
