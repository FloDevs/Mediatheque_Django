from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .emprunteur import Emprunteur
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from datetime import timedelta

class Emprunt(models.Model):
    emprunteur = models.ForeignKey(Emprunteur, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    media = GenericForeignKey('content_type', 'object_id')
    
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour = models.DateField(blank=True, null=True)

    def clean(self):
        
        # **Vérification du nombre d'emprunts en cours**
        nb_emprunts_en_cours = Emprunt.objects.filter(
            emprunteur=self.emprunteur, 
            date_retour__isnull=True  
        ).count()

        if nb_emprunts_en_cours >= 3:
            raise ValidationError(f"L'emprunteur {self.emprunteur} a déjà 3 emprunts en cours.")
        
        # **Vérification des retards de l'emprunteur**
        emprunts_en_retard = Emprunt.objects.filter(
            emprunteur=self.emprunteur,
            date_retour__isnull=True,
            date_emprunt__lt=now().date() - timedelta(days=7)  # Si la date d'emprunt dépasse 7 jours
        )
        
        if emprunts_en_retard.exists():
            raise ValidationError(f"L'emprunteur {self.emprunteur} a un emprunt en retard et ne peut pas emprunter de nouveau.")

        # **Vérification que le média n'est pas un jeu de plateau**
        if self.content_type.model == 'jeudeplateau':
            raise ValidationError("Les jeux de plateau ne peuvent pas être empruntés.")

    def save(self, *args, **kwargs):
        
        self.clean() 
        super().save(*args, **kwargs)  # Sauvegarde l'emprunt

    def __str__(self):
        return f'{self.media} emprunté par {self.emprunteur}'
