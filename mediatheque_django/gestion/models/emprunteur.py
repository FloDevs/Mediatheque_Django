from django.db import models
from django.core.exceptions import ValidationError



class Emprunteur(models.Model):
    name = models.CharField(max_length=200)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
