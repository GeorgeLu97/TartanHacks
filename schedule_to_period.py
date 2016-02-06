import icalendar
import sys
import os
import django
from django.db.transaction import atomic

from schedule_object import *
from overlap import *

sys.path.append('./scheduler/')
os.environ["DJANGO_SETTINGS_MODULE"] = "scheduler.settings"
django.setup()

from display_cal.models import *

#from django.conf import settings
#settings.configure()

def ics_to_p(filename):
    '''converts ics to period object'''
    pass

def splittime(t0,t1,d):
    '''returns datetime objects'''
    dts = []
    while t0 < t1:
        dts.append((get_dt(t0,d),get_dt(t0+.5,d)))
        t0 += .5
    return filter(lambda x: x[0] >= 7 and x[1] <= 8.5, dts)

@atomic
def event_to_periods(e, person):
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
        c.people.add(person)
        p.save()
        p.courses.add(c)
        ps.append(p)
        print(st)
    return ps

def schedule_to_p(s):
    '''converts from schedule to period obj'''
    periods = []
    rando = Person(name="ABDC", username="abcdefgh")
    rando.save()
    for e in s.events:
        periods.extend(event_to_periods(e, rando))
    return periods

#testcode
p0 = schedule_to_p(q0)
#p1 = schedule_to_p(q1)
#print("hi")
#p2 = schedule_to_p(q2)
