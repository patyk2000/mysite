from django.urls import path, include
from .import views
from django.contrib import admin

app_name = "rowery"
urlpatterns = [
    path('admin', admin.site.urls),

]