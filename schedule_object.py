import icalendar
import datetime

def weektime(dtobj):
    '''converts a datetime object into a tuple which contains
    (weekday, starthour, endhour), with times rounded to the next
    10 minutes (for example, 12:20 is rounded to hour 12.5)'''
    daymap = {0:'M',1:'T',2:'W',3:'R',4:'F',5:'S',6:'U'}
    minmap = lambda x: x+10 if x in [20,50] else x
    return (daymap[dtobj.weekday()],dtobj.hour+minmap(dtobj.minute)/60.)

class Event:
    '''a event object has one constructor which takes a component object
    it has four attributes -- obj.start, obj.end, obj.summary, and obj.location
    the first two time tuples (weekday, hour), the latter are strings'''
    datekeys = ['DTSTART', 'DTEND'] #'DTSTAMP'
    stringkeys= ['SUMMARY', 'LOCATION'] #'DESCRIPTION'
    def __init__(self, component = None):
        if component is None:
            return
        for key in Event.datekeys:
            setattr(self, key.lower()[2:], weektime(component.get(key).dt))
        for key in Event.stringkeys:
            setattr(self, key.lower(), str(component.get(key)))
    def set(start, end, summary='', location=''):
        self.start = start
        self.end = end
        if summary:
            self.summary = summary
        if location:
            self.location = location

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
q = Schedule('test_schedule.ics')
for e in q.events:
    print e.start, e.end
