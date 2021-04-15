from django.db import models

# Create your models here.

class iatacodes(models.Model):
    iata= models.CharField(max_length=3)
    airlines= models.CharField(max_length=50)

    def __str__(self):
        return self.airlines