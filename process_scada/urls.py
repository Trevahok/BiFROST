from django.urls import path
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
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

    path("change/", views.ChangeListView.as_view(), name="view_change"),
    path("change/add/", views.ChangeCreationView.as_view(), name="add_change"),
    path("change/<pk>/update/", views.ChangeUpdationView.as_view(), name="update_change"),
    path("change/<pk>/delete/", views.ChangeDeleteView.as_view(), name="delete_change"),

    path('api/', csrf_exempt(views.ApiEndpoint.as_view()),name='api'),

    path("batch/", views.BatchListView.as_view(), name="view_batch"),
    path("batch/add/", views.BatchCreationView.as_view(), name="add_batch"),
    path("batch/<pk>/update/", views.BatchUpadteView.as_view(), name="update_batch"),
    path("batch/<pk>/delete/", views.BatchDeleteView.as_view(), name="delete_batch"),
    path("batch/<pk>/", views.BatchDetailView.as_view(), name='detail_batch'),

    path("product/", views.ProductListView.as_view(), name="view_product"),
    path("product/add/", views.ProductCreationView.as_view(), name="add_product"),
    path("product/<pk>/update/", views.ProductUpadteView.as_view(), name="update_product"),
    path("product/<pk>/delete/", views.ProductDeleteView.as_view(), name="delete_product"),
    path("product/<pk>/", views.ProductDetailView.as_view(), name="detail_product")
]
