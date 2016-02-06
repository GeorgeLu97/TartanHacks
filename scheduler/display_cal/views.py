from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.template import loader
from django.shortcuts import render

from .models import Period, Person, Course

def index(request, user=None):
    template = loader.get_template('display_cal/index.html')
    
    user = Person.objects.filter(username__exact=user).first()
    periods = []
    
    if user:
        courses = user.course_set.all()
        for course in courses:
            periods.extend(list(Period.objects.filter(courses__name__contains=course.name)))
    
    context = {'days_of_week': ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"],
               'periods': periods}
    return render(request, 'display_cal/index.html', context)