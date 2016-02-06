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
        e.set((t1,t2),e1.day, e1.location)
        return e

def overlap_schedule(s1, s2):
    '''returns the overlap of two schedules'''
    #for each day of the week
    #for each e1 from s1 and e2 from s2
    #add their overlap to the schedule
    #return schedule
    #Don't Mention Time Complexity
    ret = Schedule()
    for component1 in s1.events():
        for component2 in s2.events():
            e = overlap(component1, component2)
            if e:
                e.summary = "Shared With " + s2.Owner
                ret.events.append(e)

    return ret

def overlap_s_schedule(sh1,s1,s2):
    #returns shared schedule based on s1, with sh1 being already shared
    r1 = overlap_schedule(s1,s2)
    for e1 in r1.events():
        paired = False
        e = Event()
        for e2 in sh1.events():
            if overlap(e1,e2):
                paired = True
                e = overlap(e1,e2)
                break
        if paired:
            e.summary = e.summary + " " + s2.Owner
        else:
            sh1.append(e1)
    return sh1

#testcode
q2 = overlap_schedule(q0,q1)
q3 = overlap_s_schedule(q0,q1)
