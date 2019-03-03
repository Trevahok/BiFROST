from django.contrib import admin

from .models import *
# Register your models here.

for i in [Product,Production,Batch,Diagnosis,Change,File]:
    admin.site.register(i)
