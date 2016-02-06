import icalendar
import datetime
from schedule_object import Schedule, Event

def overlap(e1,e2):
    '''returns the overlap of event 1 and event2'''
    if e1.day != e2.day or e1.location != e2.location:
        return False
    t1, t2 = max(e1.start,e2.start),min(e1.end,e2.end)
    if t1 >= t2:
        return False
    else:
        e = Event()
        e.set(t1,t2),e1.day, e1.location)
        return e

def overlap_schedule(s1, s2):
    '''returns the overlap of two schedules'''
    #for each day of the week
    #for each e1 from s1 and e2 from s2
    #add their overlap to the schedule
    #return schedule
    pass

