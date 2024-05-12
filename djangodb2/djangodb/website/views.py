from django.http import HttpResponse
from django.shortcuts import render
from .models import Rezerwacja
from django.db import connection

def rezerwacje_query_view(request):
 
    # Use Manager.raw() to perform a raw SQL query and return model instances
    rezerwacja = Rezerwacja.objects.raw("SELECT * FROM website_Rezerwacja;")
 
    # Pass the queryset to the template
    return render(request, 'rezerwacje.html', {'Rezerwacje': rezerwacja})

#def usun_rezerwacje(request, nr_rezerwacji_klienta):
    #usun = Rezerwacja.objects.raw("DELETE FROM website_Rezerwacja WHERE NrRezerwacji='1'")
    #return render(request, 'rezerwacje.html', {'Rezerwacje': usun})
   
   
   #query = "DELETE FROM website_Rezerwacja WHERE NrRezerwacji=1"
   #connection.cursor.execute(query)

def home(request):
    return render(request, 'home.html', {})
    #return HttpResponse('Hello, World!')
# Create your views here.
