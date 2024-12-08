from django.shortcuts import render

def menu(request):
    return render(request, 'gestion/menu.html')

def menu_membre (request) : 
    return render (request, 'gestion/menu_membre.html')

def menu_bibliothecaire (request) : 
    return render (request, 'gestion/menu_bibliothecaire.html')