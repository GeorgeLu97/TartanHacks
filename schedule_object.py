from collections import defaultdict
import icalendar
import datetime
import copy
from date_conversion import get_dt

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
    def get_start_dt(self):
        return get_dt(self.time[0],self.day)
    def get_end_dt(self):
        return get_dt(self.time[1],self.day)
    def __str__(self):
        return ("%s from %.1f to %.1f on %s" %
                (self.location, self.time[0], self.time[1], self.day))
            
class Schedule:
    '''a schedule object has one constructor which takes a filename
    it has one attribute -- a list of events, at obj.events'''
    Owner=''
    def __init__(self,filename = None,Owner='', complete = False, data=None):
        events = []
        self.events = []
        self.Owner = Owner
        if not filename and not data:
            return
        if filename:    
            with open(filename, "rb") as inf:
                schedule = icalendar.Calendar.from_ical(inf.read())
        elif data:
            schedule = icalendar.Calendar.from_ical(data)
        for component in schedule.walk():
            if component.name == "VEVENT":
                events.append(Event(component))
        for event in events:
            self.events.extend(eventsplit(event))
        if complete:
            self.complete()
    def complete(self):
        '''adds break times'''
        day_dict = defaultdict(list)
        for event in self.events:
            day_dict[event.day].append(event)
        for day in day_dict:
            day_dict[day].sort(key = lambda x: x.time[0])
        gap_events = []
        for day, es in day_dict.items():
            start = 0
            for e in es:
                if e.time[0]-.00001 > start:
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
"""
print 'schedule 0'
>>>>>>> 38b16c43a0c96f359e2380a8098bcb77779c337e
q0 = Schedule('test_schedule.ics')
q1 = Schedule('S16_schedule.ics')
<<<<<<< HEAD
=======
for e in q1.events:
    print e.time, e.day
print("hi1")
"""
