from django.contrib import admin

from .models import Producent, Typ, Osprzęt


# Register your models here.
admin.site.register(Producent)
admin.site.register(Typ)
admin.site.register(Osprzęt)