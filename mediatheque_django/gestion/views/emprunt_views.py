from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from ..models.emprunteur import Emprunteur
from ..models.emprunt import Emprunt
from ..models.books import Livre
from ..models.cds import Cd
from ..models.dvds import Dvd

def creer_emprunt(request):
    
    if request.method == 'POST':
        emprunteur_id = request.POST.get('emprunteur')
        media_type = request.POST.get('media_type')
        media_id = request.POST.get('media_id')
        
        emprunteur = Emprunteur.objects.get(id=emprunteur_id)
        if media_type == 'Livre':
            media = Livre.objects.get(id=media_id)
        elif media_type == 'CD':
            media = Cd.objects.get(id=media_id)
        elif media_type == 'DVD':
            media = Dvd.objects.get(id=media_id)
        
        Emprunt.objects.create(emprunteur=emprunteur, media=media)
        return redirect('liste_emprunteurs')
    
    emprunteurs = Emprunteur.objects.all()
    livres = Livre.objects.filter(disponible=True)
    cds = Cd.objects.filter(disponible=True)
    dvds = Dvd.objects.filter(disponible=True)
    return render(request, 'gestion/creer_emprunt.html', {'emprunteurs': emprunteurs, 'livres': livres, 'cds': cds, 'dvds': dvds})


def rentrer_emprunt(request, emprunt_id):
    
    emprunt = get_object_or_404(Emprunt, id=emprunt_id)
    emprunt.date_retour = now()
    emprunt.save()
    return redirect('liste_emprunteurs')
