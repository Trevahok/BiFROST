from django import forms
from .models import Parameter,Diagnosis,Production

class FileUploadForm(forms.Form):
    file = forms.FileField(max_length= 100, required=True)

class ParameterForm(forms.ModelForm):
    class Meta:
        model = Parameter
        fields = '__all__'

class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = '__all__'
    
class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = '__all__'