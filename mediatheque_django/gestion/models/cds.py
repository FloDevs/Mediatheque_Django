from django.db import models

class Cd(models.Model):
    name = models.CharField(max_length=200)
    artiste = models.CharField(max_length=200)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    

    def __str__(self):
        return self.name
