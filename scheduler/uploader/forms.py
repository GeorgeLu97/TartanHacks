from django import forms

class FileUploadForm(forms.Form):
    name = forms.CharField(max_length=40)
    username = forms.CharField(max_length=10, min_length=3)
    docfile = forms.FileField(label='Select a file')