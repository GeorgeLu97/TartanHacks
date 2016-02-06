from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.template import loader
from django.shortcuts import render

def index(request):
    template = loader.get_template('display_cal/index.html')
<<<<<<< HEAD
    context = {'days_of_week': ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]}
=======
    context = None
>>>>>>> 021fd84b07be709bdfaadaa09c4f095d89b20392
    return render(request, 'display_cal/index.html', context)