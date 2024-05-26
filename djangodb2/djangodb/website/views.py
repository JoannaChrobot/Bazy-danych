from django.http import HttpResponse
from django.shortcuts import render
from .models import Rezerwacja
from django.db import connection
from .models import Osoba
from .models import Pomieszczenie
from .models import Pracownik
from .models import Grafik

from .forms import PomieszczenieForm

def rezerwacje_query_view(request):
 
    # Use Manager.raw() to perform a raw SQL query and return model instances
    rezerwacja = Rezerwacja.objects.raw("SELECT * FROM website_Rezerwacja;")
 
    # Pass the queryset to the template
    return render(request, 'rezerwacje.html', {'Rezerwacje': rezerwacja})


def glowna_strona(request):
    return render(request, 'index.html')


def lista_pokoi(request):
    pokoje = Pomieszczenie.objects.raw("SELECT * FROM website_Pomieszczenie;")
    wybrany_pokoj = None
    
    pokoj_id = request.GET.get('pokoj_id')
    if pokoj_id:
        wybrany_pokoj = Pomieszczenie.objects.get(id=pokoj_id)
    
    return render(request, 'pokoje.html', {'Pomieszczenie': pokoje})#, 'wybrany_pokoj': wybrany_pokoj})

def home(request):
    return render(request, 'home.html', {})
    #return HttpResponse('Hello, World!')
    # Create your views here.

def lista_osob(request):
    # Pobierz wszystkie osoby z bazy danych
    osoby = Osoba.objects.raw("SELECT * FROM website_Osoba;")

    # wybrana_osoba = None
    
    # pesel = request.GET.get('Pesel')
    # if pesel:
    #     wybrana_osoba = Osoba.objects.get(id=pesel)

    return render(request, 'osoby.html', {'Osoba': osoby})# 'wybrana_osoba': wybrana_osoba})

def zadania(request):
    if request.method == "POST":
        form = PomieszczenieForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        zadania = Pomieszczenie.objects.raw("SELECT * FROM website_Pomieszczenie;")
        return render(request, 'zadania.html', {'Pomieszczenie': zadania})

def grafik(request):
    grafik = Grafik.objects.raw("SELECT * FROM website_Grafik;")
    return render(request, 'grafik.html', {'Grafik': grafik})
