from django.shortcuts import render, redirect
from ..models.emprunteur import Emprunteur

def ajouter_emprunteur(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        emprunteur = Emprunteur.objects.create(name=name)
        return redirect('liste_emprunteurs')
    return render(request, 'gestion/ajouter_emprunteur.html')


def liste_emprunteurs(request):
    
    emprunteurs = Emprunteur.objects.all()
    return render(request, 'gestion/liste_emprunteurs.html', {'emprunteurs': emprunteurs})