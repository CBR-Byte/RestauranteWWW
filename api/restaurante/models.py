from django.db import models

# Create your models here.

class Alimentos(models.Model):
    nombre=models.CharField(max_length=20)
    categoria=models.CharField(max_length=20)
    def __str__(self):
        return self.nombre
 
class Platos(models.Model):
    nombre=models.CharField(max_length=20)
    tiempo_preparacion=models.DurationField(default='00:30:00')
    categoria=models.CharField(max_length=20)
    alimentos = models.ManyToManyField(Alimentos,blank=True)
    def __str__(self):
        return self.nombre
    