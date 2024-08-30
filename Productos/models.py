from django.db import models

# Create your models here.

class Vestido (models.Model):
    nombre= models.CharField(max_length=100)
    estilo= models.CharField(max_length=100)
    color= models.CharField(max_length=100)
    talla= models.IntegerField()

    def __srt__(self):
        return self.nombre