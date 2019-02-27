from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField(max_length= 100, required=False)
