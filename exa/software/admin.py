from django.contrib import admin

# Register your models here.
from .models import Trabajo, CategoriaTrabajo

admin.site.register(Trabajo)
admin.site.register(CategoriaTrabajo)