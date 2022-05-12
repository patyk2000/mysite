from django.db import models

class Producent(models.Model):
    producent=models.CharField(max_length=200)
    model=models.ForeignKey(Typ, on_delete=models.CASCADE, null=True)

def __str__(self):
     return self.producent

class Typ(models.Model):
    model_nazwa=models.CharField(max_length=200, null=True)
    
def __str__(self):
     return self.model_nazwa


class Osprzęt(models.Model):
    frame=models.CharField(max_length=200, null=True)
    wheel=models.CharField(max_length=200, null=True)
    forks=models.CharField(max_length=200, null=True)
        
def __str__(self):
     return self.frame
