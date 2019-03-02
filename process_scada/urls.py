from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('file/upload/', views.FileUploadView.as_view() ,name = 'file_upload'),
    path('file/upload/success/', TemplateView.as_view(template_name='file_upload_success.html'), name='success'),

    path("parameter/", views.ParameterListView.as_view(), name="view_parameter"),
    path("parameter/add/", views.ParameterCreationView.as_view(), name="add_parameter"),
    path("parameter/<pk>/update/", views.ParameterUpdationView.as_view(), name="update_parameter"),
    path("parameter/<pk>/delete/", views.ParameterDeleteView.as_view(), name="delete_parameter"),

    path("diagnosis/", views.DiagnosisListView.as_view(), name="view_diagnosis"),
    path("diagnosis/add/", views.DiagnosisCreationView.as_view(), name="add_diagnosis"),
    path("diagnosis/<pk>/update/", views.DiagnosisUpdationView.as_view(), name="update_diagnosis"),
    path("diagnosis/<pk>/delete/", views.DiagnosisDeleteView.as_view(), name="delete_diagnosis"),

    path("production/", views.ProductionListView.as_view(), name="view_production"),
    path("production/add/", views.ProductionCreationView.as_view(), name="add_production"),
    path("production/<pk>/update/", views.ProductionUpdationView.as_view(), name="update_production"),
    path("production/<pk>/delete/", views.ProductionDeleteView.as_view(), name="delete_production"),
]
