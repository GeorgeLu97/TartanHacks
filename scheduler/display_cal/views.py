from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.template import loader
from django.shortcuts import render

def index(request):
    template = loader.get_template('display_cal/index.html')
    context = {'days_of_week': ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]}
    return render(request, 'display_cal/index.html', context)