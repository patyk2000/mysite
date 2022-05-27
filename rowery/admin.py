from itertools import product
from django.contrib import admin

from .models import types, Producent, Parts, Bike


# Register your models here.
admin.site.register(types)
admin.site.register(Producent)
admin.site.register(Parts)
admin.site.register(Bike)