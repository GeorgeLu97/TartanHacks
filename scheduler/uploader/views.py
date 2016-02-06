from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from .models import FileUpload
from .forms import FileUploadForm

import sys
sys.path.append('../')
from schedule_object import Schedule
from schedule_to_period import schedule_to_p

# Create your views here.
def upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            tmp = Schedule(data=request.FILES['docfile'].read())
            tmp2 = schedule_to_p(tmp, name, username)
            
            #newfile = FileUpload(upload=request.FILES['docfile'])
            #newfile.save()
            
            return HttpResponseRedirect("../index/" + username)
    else:
        form = FileUploadForm()
        
    return render_to_response('uploader/upload.html', {'form': form},
                              context_instance=RequestContext(request))