from django.views.generic.base import TemplateView
from django.shortcuts import render
import datetime
from .models import Period, Person, Course

def index(request, username=None):
    user = Person.objects.filter(username__exact=username).first()
    userPeriods = []
    periods = [datetime.time(h,m) for h in range(7,21) for m in [0,30]]
    days = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
    courseFriends = {}
    
    schedule = [[(startTime, False, None) for day in days] for startTime in periods]
    
    if user:
        courses = user.course_set.all()
        for course in courses:
            pers = Period.objects.filter(courses__name__contains=course.name)
            courseFriends[course.name] = list(course.people.exclude(username__exact=username))
            
            for per in pers:
                old = schedule[periods.index(per.startTime)][days.index(per.day)]
                schedule[periods.index(per.startTime)][days.index(per.day)] = (old[0], course, courseFriends[course.name])
                
            userPeriods.extend(list(Period.objects.filter(courses__name__contains=course.name)))
            
        context = {'days_of_week': days,
           'schedule': schedule,
           }
        
        return render(request, 'display_cal/index.html', context)
    else:
        context = None
        return render(request, 'display_cal/none.html', context)
    #TODO: render different courses with different colors
    
    
               
    