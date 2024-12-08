from django.db import models

class Livre(models.Model):
    name = models.CharField(max_length=200)
    auteur = models.CharField(max_length=200)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    

    def __str__(self):
        return self.name