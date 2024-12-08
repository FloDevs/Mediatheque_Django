from django.shortcuts import render, redirect
from ..models.books import Livre
from ..models.cds import Cd
from ..models.dvds import Dvd

def liste_medias(request):
    
    livres = Livre.objects.all()
    cds = Cd.objects.all()
    dvds = Dvd.objects.all()
    return render(request, 'gestion/liste_medias.html', {'livres': livres, 'cds': cds, 'dvds': dvds})


def ajouter_media(request):
    
    if request.method == 'POST':
        media_type = request.POST.get('media_type')
        name = request.POST.get('name')
        if media_type == 'Livre':
            Livre.objects.create(name=name)
        elif media_type == 'CD':
            Cd.objects.create(name=name)
        elif media_type == 'DVD':
            Dvd.objects.create(name=name)
        return redirect('liste_medias')
    return render(request, 'gestion/ajouter_media.html')
