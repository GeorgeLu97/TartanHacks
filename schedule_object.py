import icalendar
import datetime

class Event:
    '''a event object has one constructor which takes a component object'''

    def __init__(self, component = None):
        if component is None:
            return
        self.component = component
        minmap = lambda x: x+10 if x in [20,50] else x
        gethour = lambda x: x.hour+minmap(x.minute)/60.
        startt,endt = component['DTSTART'].dt,component['DTEND'].dt
        starthour, endhour = gethour(startt), gethour(endt)
        self.time = (starthour,endhour)
        self.days = [str(val) for val in component['RRULE']['BYDAY']]
        self.summary = str(component['SUMMARY'])
        self.location = str(component['LOCATION'])
    def set(time, days, summary='', location=''):
        self.time = time
        self.days = days
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
print 'schedule 0'
q0 = Schedule('test_schedule.ics')
for e in q0.events:
    print e.time, e.days
print 'schedule 1'
q1 = Schedule('S16_schedule.ics')
for e in q1.events:
    print e.time, e.days
