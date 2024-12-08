from django.urls import path
from .views import menus_views , emprunteur_views, media_views, emprunt_views  

urlpatterns = [
    path('menu/', menus_views.menu, name='menu'),
    path('emprunteurs/', emprunteur_views.liste_emprunteurs, name='liste_emprunteurs'),
    path('emprunteurs/ajouter/', emprunteur_views.ajouter_emprunteur, name='ajouter_emprunteur'),

    # Médias
    path('medias/', media_views.liste_medias, name='liste_medias'),
    path('medias/ajouter/', media_views.ajouter_media, name='ajouter_media'),

    # Emprunts
    path('emprunts/creer/', emprunt_views.creer_emprunt, name='creer_emprunt'),
    path('emprunts/rentrer/<int:emprunt_id>/', emprunt_views.rentrer_emprunt, name='rentrer_emprunt'),
    
    
]