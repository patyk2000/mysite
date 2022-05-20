from operator import truediv
from turtle import ondrag
from django.db import models
from datetime import datetime
from django.forms import CharField
from tkinter import CASCADE
from telnetlib import NOP

class types(models.Model):
    name=models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name

class Producent(models.Model):
    producent=models.CharField(max_length=200, null=True)
   
    def __str__(self):
        return self.producent

class Wheel(models.Model):
    Wheel=models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return self.Wheel

class Rower(models.Model):
    frame=models.CharField(max_length=200, null=True)
    types=models.ForeignKey(types, on_delete=models.CASCADE)
    Wheel=models.ForeignKey(Wheel, on_delete=models.CASCADE)
    forks=models.CharField(max_length=200, null=True)
    Producent=models.ForeignKey(Producent, on_delete=models.CASCADE)
    Rower=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.Rower