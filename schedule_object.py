from collections import defaultdict
import icalendar
import datetime
import copy

def eventsplit(e):
    '''splits an event into a separate event for each day'''
    es = [copy.deepcopy(e) for date in e.days]
    for i, e in enumerate(es):
        e.day = e.days[i]
        del e.days
    return es

class Event:
    '''a event object has one constructor which takes a component object'''
    ''' there are four attributes:
    summary -- a string
    location -- a string
    time -- a (hour, hour) tuple
    
    only one of the following attributes may be in use at a time
    days -- a list of strings for days of the week
    day -- a single string for the day of the week this event happens on'''
    def __init__(self, component = None):
        if component is None:
            return
        self.component = component
        minmap = lambda x: x+10 if x in [20,50] else x
        gethour = lambda x: x.hour+minmap(x.minute)/60.
        startt,endt = component['DTSTART'].dt,component['DTEND'].dt
        starthour, endhour = gethour(startt), gethour(endt)
        self.time = (starthour,endhour)
        self.day = ''
        self.days = [str(val) for val in component['RRULE']['BYDAY']]
        self.summary = str(component['SUMMARY'])
        self.location = str(component['LOCATION'])
    def set(self,time, day, summary='', location=''):
        self.time = time
        self.day = day
        if summary:
            self.summary = summary
        if location:
            self.location = location
    def __str__(self):
        return ("%s from %.1f to %.1f on %s" %
                (self.location, self.time[0], self.time[1], self.day))
            
class Schedule:
    '''a schedule object has one constructor which takes a filename
    it has one attribute -- a list of events, at obj.events'''
    Owner=''
    def __init__(self,filename = None,Owner='',splitevents = True):
        events = []
        self.events = []
        self.Owner = Owner
        if not filename:
            return
        with open(filename, "rb") as inf:
            schedule = icalendar.Calendar.from_ical(inf.read())
        for component in schedule.walk():
            if component.name == "VEVENT":
                events.append(Event(component))
        if splitevents:
            for event in events:
                self.events.extend(eventsplit(event))
        else:
            self.events = events
    def complete(self):
        '''unions a schedule with its complement'''
        day_dict = defaultdict(list)
        for event in self.events:
            day_dict[event.day].append(event)
        for day in day_dict:
            day_dict[day].sort()
        gap_events = []
        for day, es in day_dict.items():
            start = 0
            for e in es:
                if e.time[0] > start:
                    gap_events.append((start, e.time[0],day))
                    start = e.time[1]
            if start < 24:
                gap_events.append((start,24,day))
        for s,t,d in gap_events:
            E = Event()
            E.set((s,t),d,'free','free')
            self.events.append(E)
    def __str__(self):
        return ("%s has %d events\n" % (self.Owner, len(self.events))+
                '\n'.join([str(e) for e in self.events]))
            

#test code
print 'schedule 0'
q0 = Schedule('test_schedule.ics')
for e in q0.events:
    print e.time, e.day
print 'schedule 1'
q1 = Schedule('S16_schedule.ics')
for e in q1.events:
    print e.time, e.day
