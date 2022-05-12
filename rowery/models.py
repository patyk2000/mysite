
from django.db import models

class types(models.Model):
    name=models.CharField(max_length=200, null=True)
    
def __str__(self):
     return self.name

class Producent(models.Model):
    producent=models.CharField(max_length=200)
    model=models.ForeignKey(types, on_delete=models.CASCADE, null=True)

def __str__(self):
     return self.producent


class Osprzęt(models.Model):
    frame=models.CharField(max_length=200, null=True)
    wheel=models.CharField(max_length=200, null=True)
    forks=models.CharField(max_length=200, null=True)
        
def __str__(self):
     return self.frame
