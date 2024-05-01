from django.contrib import admin

# Register your models here.
from .models import model1, Model2

admin.site.register(model1)
admin.site.register(Model2)
