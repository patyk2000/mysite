from django.contrib import admin

from .models import Producent, types, Rower, Wheel


# Register your models here.
admin.site.register(Producent)
admin.site.register(types)
admin.site.register(Rower)
admin.site.register(Wheel)