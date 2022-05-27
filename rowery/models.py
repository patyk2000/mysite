from django.db import models
from django.forms import CharField
from tkinter import CASCADE
from telnetlib import NOP

class types(models.Model):
    types_name=models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.types_name

class Producent(models.Model):
    producent_name=models.CharField(max_length=200, null=True)
   
    def __str__(self):
        return self.producent_name


class Parts(models.Model):
    parts_name=models.CharField(max_length=200, null=True)
   
    def __str__(self):
        return self.parts_name

class Bike(models.Model):
    name=models.CharField(max_length=200, null=True)
    type=models.ForeignKey(types, on_delete=models.CASCADE)
    Part=models.ManyToManyField(Parts)
    fork=models.CharField(max_length=200, null=True)
    producent=models.ForeignKey(Producent, on_delete=models.CASCADE)


    def __str__(self):
        return self.producent