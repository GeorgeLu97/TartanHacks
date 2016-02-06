from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from .models import FileUpload
from .forms import FileUploadForm

# Create your views here.
def upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            #handle ics
            newfile = FileUpload(upload=request.FILES['docfile'])
            newfile.save()
            
            username = form.cleaned_data['username']
            return HttpResponseRedirect("../index/" + username)
    else:
        form = FileUploadForm()
        
    return render_to_response('uploader/upload.html', {'form': form},
                              context_instance=RequestContext(request))