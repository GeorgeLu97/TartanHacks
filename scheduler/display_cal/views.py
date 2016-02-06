from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.template import loader
from django.shortcuts import render
import datetime
from .models import Period, Person, Course

def index(request, user=None):
    template = loader.get_template('display_cal/index.html')
    
    user = Person.objects.filter(username__exact=user).first()
    userPeriods = []
    periods = [datetime.time(h,m) for h in range(7,21) for m in [0,30]]
    days = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
    
    schedule = [[(startTime, False) for day in days] for startTime in periods]
    
    if user:
        courses = user.course_set.all()
        for course in courses:
            userPeriods.extend(list(Period.objects.filter(courses__name__contains=course.name)))
    
        for period in userPeriods:
            old = schedule[periods.index(period.startTime)][days.index(period.day)]
            schedule[periods.index(period.startTime)][days.index(period.day)] = (old[0], True)
    
    context = {'days_of_week': days,
               'user_periods': userPeriods,
               'periods': periods,
               'schedule': schedule}
    return render(request, 'display_cal/index.html', context)