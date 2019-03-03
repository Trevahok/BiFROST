from django import forms
from .models import Parameter,Diagnosis,Production,Change, File, Batch, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = '__all__'

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'

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

class ChangeForm(forms.ModelForm):
    class Meta:
        model = Change
        fields = '__all__'