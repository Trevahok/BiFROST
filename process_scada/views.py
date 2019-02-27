from django.views.generic import FormView
from .forms import FileUploadForm

# Create your views here.
class FileUploadView(FormView):
    template_name = 'generic_form.html'
    form_class = FileUploadForm
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

