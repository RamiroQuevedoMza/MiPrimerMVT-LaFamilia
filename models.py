from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length= 8)
    segundo_nombre = models.CharField (max_length= 8)
    documento = models.IntegerField ()
    edad = models.IntegerField ()
    nacimiento = models.DateField (null= True)