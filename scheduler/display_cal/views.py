from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.template import loader
from django.shortcuts import render

def index(request):
    template = loader.get_template('display_cal/index.html')
    context = None
    return render(request, 'display_cal/index.html', context)