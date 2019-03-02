from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
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
            print('form valid checking')
            return self.form_valid(form, **kwargs)
        else:
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
    success_url = 'view_parameter'


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
    success_url = 'view_diagnosis'


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
    success_url = 'view_production'
