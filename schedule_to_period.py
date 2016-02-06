import icalendar
import sys
sys.path.append('./scheduler/display_cal/')
from models import *
from schedule_object import *
from overlap import *

#from django.conf import settings
#settings.configure()

def ics_to_p(filename):
    '''converts ics to period object'''
    pass

def splittime(t0,t1,d):
    '''returns datetime objects'''
    dts = []
    while t0 < t1:
        dts.append((get_dt(t0,day),get_dt(t0+.5,day)))
        t0 += .5
    return dts    

def event_to_periods(event):
    '''converts an event to periods'''
    ps = []
    for st, et, in splittime(e.time[0],e.time[1],e.day):
        p = Period(startTime = st, endTime = et, day = e.day)
        #fix this later
        c = Course(codeNumber = e.location, 
                   name = e.location, 
                   building = e.location,
                   room = e.location)
        c.save()
        p.save()
        p.courses.add(c)
        p.save()
        ps.append(p)
    return ps

def schedule_to_p(s):
    '''converts from schedule to period obj'''
    periods = []
    for e in s.events:
        periods.extend(event_to_periods(e))
    return periods

#testcode
p0 = schedule_to_p(q0)
p1 = schedule_to_p(q1)
p2 = schedule_to_p(q2)
