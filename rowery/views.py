from django.shortcuts import render
from .models import types, Producent, Parts, Bike

def Bikes(request):
    return render(request, 'Bikes/index.html')

def types(request):
    return render(request, 'types/index.html')


def Producent(request):
    return render(request, 'Producent/index.html')

def Parts(request):
    return render(request, 'Parts/index.html')

