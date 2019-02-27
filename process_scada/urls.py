from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('file/upload/', views.FileUploadView.as_view() ,name = 'file_upload'),
    path('file/upload/success/', TemplateView.as_view(template_name='file_upload_success.html'), name='success'),
]
