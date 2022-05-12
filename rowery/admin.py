from django.contrib import admin

from .models import Producent, types, Osprzęt


# Register your models here.
admin.site.register(Producent)
admin.site.register(types)
admin.site.register(Osprzęt)