import icalendar
import datetime

class Event:
    '''a event object has one constructor which takes a component object
    it has four attributes -- obj.start, obj.end, obj.summary, and obj.location
    the first two are python datetime objects, the latter are strings'''
    datekeys = ['DTSTART', 'DTEND'] #'DTSTAMP'
    stringkeys= ['SUMMARY', 'LOCATION'] #'DESCRIPTION'
    def __init__(self, component):
        for key in Event.datekeys:
            setattr(self, key.lower()[2:], (component.get(key).dt))
        for key in Event.stringkeys:
            setattr(self, key.lower(), str(component.get(key)))

class Schedule:
    '''a schedule object has one constructor which takes a filename
    it has one attribute -- a list of events, at obj.events'''
    def __init__(self,filename):
        self.events = []
        with open(filename, "rb") as inf:
            schedule = icalendar.Calendar.from_ical(inf.read())
        for component in schedule.walk():
            if component.name == "VEVENT":
                self.events.append(Event(component))


#test code
#q = Schedule('test_schedule.ics')
