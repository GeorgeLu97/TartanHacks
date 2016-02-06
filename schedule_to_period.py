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
        if 20 >= t0 >= 7:
            dts.append((get_dt(t0,d),get_dt(t0+.5,d)))
        t0 += .5
    return dts

@atomic
def event_to_periods(e, person):
    '''converts an event to periods'''
    ps = []
    for st, et, in splittime(e.time[0],e.time[1],e.day):
        p = Period.objects.filter(startTime=st).filter(day=e.day).first()
        if not p:
            p = Period(startTime = st, endTime = et, day = e.day)
            p.save()
            
        #fix this later
        tmpCodeNumber = e.summary.split(' :: ')[-1]
        c = Course.objects.filter(codeNumber=tmpCodeNumber).first()
        if not c:
            c = Course(codeNumber = tmpCodeNumber, 
                       name = e.location, 
                       building = e.location,
                       room = e.location)
            c.save()
            
        c.people.add(person)
        p.courses.add(c)
        ps.append(p)
    return ps

def schedule_to_p(s, name, username):
    '''converts from schedule to period obj'''
    periods = []
    #check that person isn't already in database
    student = Person.objects.filter(username=username)
    if not student:
        student = Person(name=name, username=username)
        student.save()
    for e in s.events:
        periods.extend(event_to_periods(e, student))
    return periods

#testcode
#p0 = schedule_to_p(q0, 'ricson9')
#p1 = schedule_to_p(q1, 'chong9')
#p2 = schedule_to_p(q2, 'overlap9')
"""
print(q1)
#testcode
#p0 = schedule_to_p(q0)
p1 = schedule_to_p(q1)
#print("hi")
#p2 = schedule_to_p(q2)
"""
