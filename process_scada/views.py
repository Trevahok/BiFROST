from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import forms
from . import models
from time import sleep
from .utils.pdf_extractor import read_report
from json import dumps,loads
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from pprint import pprint

# Create your views here.
class FileUploadView(LoginRequiredMixin , generic.FormView):
    template_name = 'generic_form.html'
    form_class = forms.FileUploadForm
    success_url = 'success'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        print('form received')
        if form.is_valid():
            print('form valid ')
            pdf_file = self.request.FILES['file']
            print('its a change form')
            data_to_db = read_report(pdf_file)
            batch = data_to_db['batch']
            product = data_to_db['product']
            print(product)
            product_model, created = models.Product.objects.get_or_create(name=product)
            batch_model, created = models.Batch.objects.get_or_create(product=product_model, batch_no=batch)
            product_form = forms.ProductForm(data={'name':product}) 
            for row in data_to_db['change']:
                final_data = {
                    'time': row[0],
                    'operation' : row[1],
                    'description' : row[2],
                    'batch': batch_model.pk,
                }
                print(final_data)
                print()
                change_form = forms.ChangeForm(data=final_data) 
                if change_form.is_valid():
                    print('change form is valid ')
                    change_form.save()
                else:
                    print('change form is invalid ')

            print('diagnosis is doing ')
            for row in data_to_db['diagnosis']:
                final_data = {
                    'timestamp': row[0],
                    'diagnosis_filter' : row[1],
                    'error_code' : row[2],
                    'details': row[3],
                    'batch': batch_model.pk,
                }
                diagnosis_form = forms.DiagnosisForm(data=final_data) 
                if diagnosis_form.is_valid():
                    print('diagnosis form is valid ')
                    diagnosis_form.save()
                else:
                    print('diagnosis form is invalid ')
            print('production started')
            for row in data_to_db['production']:
                final_data = {
                    'time': row[0],
                    'types': row[1],
                    'quantity': row[2],
                    'comp_mmv': row[3],
                    'comp_srel': row[4],
                    'comp_pmv': row[5],
                    'batch': batch_model.pk,
                }
                production_form = forms.ProductionForm(data=final_data) 
                if production_form.is_valid():
                    print('production form is valid ')
                    production_form.save()
                else:
                    print('production form is invalid ')


            
            return self.form_valid(form, **kwargs)
        else:
            print('form invalid')
            return self.form_invalid(form, **kwargs)

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    # def form_valid(self, form, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return self.render_to_response(context)


class ParameterListView(LoginRequiredMixin, generic.ListView):
    model = models.Parameter
    template_name = 'parameter_list.html'

class ParameterCreationView(LoginRequiredMixin, generic.CreateView):
    form_class =  forms.ParameterForm
    template_name = 'generic_form.html'

class ParameterUpdationView(LoginRequiredMixin, generic.UpdateView):
    model = models.Parameter
    form_class = forms.ParameterForm
    template_name = 'generic_form.html'

class ParameterDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Parameter
    template_name = 'delete_confirm.html'
    success_url =reverse_lazy( 'view_parameter')


class DiagnosisListView(LoginRequiredMixin, generic.ListView):
    model = models.Diagnosis
    template_name = 'diagnosis_list.html'

class DiagnosisCreationView(LoginRequiredMixin, generic.CreateView):
    form_class =  forms.DiagnosisForm
    template_name = 'generic_form.html'

class DiagnosisUpdationView(LoginRequiredMixin, generic.UpdateView):
    model = models.Diagnosis
    form_class = forms.DiagnosisForm
    template_name = 'generic_form.html'

class DiagnosisDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Diagnosis
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('view_diagnosis')


class ProductionListView(LoginRequiredMixin, generic.ListView):
    model = models.Production
    template_name = 'production_list.html'

class ProductionCreationView(LoginRequiredMixin,generic.CreateView):
    form_class = forms.ProductionForm
    template_name = 'generic_form.html'

class ProductionUpdationView(LoginRequiredMixin,generic.UpdateView):
    model = models.Production
    form_class = forms.ProductionForm
    template_name = 'generic_form.html'

class ProductionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Production
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('view_production')


class ChangeListView(LoginRequiredMixin, generic.ListView):
    model = models.Change
    template_name = 'change_list.html'

class ChangeCreationView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.ChangeForm
    template_name = 'generic_form.html'

class ChangeUpdationView(LoginRequiredMixin, generic.UpdateView):
    model = models.Change
    form_class = forms.ChangeForm
    template_name = 'generic_form.html'

class ChangeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Change
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('view_change')

class ApiEndpoint(generic.View):
    def get(self,request):
        return HttpResponse('fuck u ')
    def post(self,request,*args, **kwargs):
        data = loads(self.request.body)
        change_data = data['change']
        diagnosis_data = data['diagnosis']
        batch = data['batch']
        product = data['product']
        print(product)
        product_model, created = models.Product.objects.get_or_create(name=product)
        batch_model, created = models.Batch.objects.get_or_create(product=product_model, batch_no=batch)
        product_form = forms.ProductForm(data={'name':product})
        print(product_form.__dict__)
        print('going to start ')
        for row in change_data:
            final_data = {
                'batch':batch_model.pk,
                'time': row[0],
                'operation' : row[1],
                'description' : row[2],
            }
            change_form = forms.ChangeForm(data=final_data) 
            if change_form.is_valid():
                print('change form is valid ')
                change_form.save()
            else:
                print('change form is invalid ')

        for row in diagnosis_data:
            print(row)
            final_data = {
                'batch':batch_model.pk,
                'timestamp': row[0],
                'diagnosis_filter' : row[1],
                'error_code' : row[2],
                'details': row[3],
            }
            diagnosis_form = forms.DiagnosisForm(data=final_data) 
            if diagnosis_form.is_valid():
                print('diagnosis form is valid ')
                diagnosis_form.save()
            else:
                print('diagnosis form is invalid ')
                return HttpResponse('Failed, Diagnosis form has redundancy or error')

        
        return HttpResponse('success')

class BatchListView(LoginRequiredMixin, generic.ListView):
    model = models.Batch
    template_name = 'batch_list.html'

class BatchCreationView(LoginRequiredMixin, generic.CreateView):
    form_class =  forms.BatchForm
    template_name = 'generic_form.html'

class BatchUpadteView(LoginRequiredMixin, generic.UpdateView):
    model = models.Batch
    form_class = forms.BatchForm
    template_name = 'generic_form.html'

class BatchDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Batch
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('view_batch')

class BatchDetailView(LoginRequiredMixin,generic.DetailView):
    model = models.Batch
    template_name = 'batch_detail.html'





class ProductListView(LoginRequiredMixin, generic.ListView):
    model = models.Product
    template_name = 'product_list.html'

class ProductCreationView(LoginRequiredMixin, generic.CreateView):
    form_class =  forms.ProductForm
    template_name = 'generic_form.html'

class ProductUpadteView(LoginRequiredMixin, generic.UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    template_name = 'generic_form.html'

class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Product
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('view_product')

class ProductDetailView(LoginRequiredMixin,generic.DetailView):
    model = models.Product
    template_name = 'product_detail.html'
    