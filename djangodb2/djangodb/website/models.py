from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Osoba(models.Model):
    Pesel = models.IntegerField(
        validators=[
            MaxValueValidator(99999999999),  # 11 cyfr
            MinValueValidator(10000000000),  # 11 cyfr
        ]) 
    Imie = models.CharField(max_length=30)
    Nazwisko = models.CharField(max_length=30)
    Telefon = models.IntegerField(
        validators=[
            MaxValueValidator(999999999),  # 9 cyfr
            MinValueValidator(100000000),  # 9 cyfr
        ]) 
    Miejsce_zamieszkania = models.CharField(max_length=100)
    Mail = models.EmailField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.Imie + ' ' + self.Nazwisko

class Pomieszczenie(models.Model):
    Symbol = models.CharField(max_length=5)
    Rodzaj = models.CharField(max_length=30)
    Maks_osob = models.IntegerField(null=True, blank=True)
    Usterki = models.CharField(max_length=200, null=True, blank=True)
    Opis = models.CharField(max_length=500, null=True, blank=True)
    Stan_czystości = models.BooleanField()
    Zadanie = models.CharField(max_length=100)

    def __str__(self):
        return self.Symbol + ' ' + self.Rodzaj

class Rezerwacja(models.Model):
    NrRezerwacji = models.IntegerField()
    Pesel = models.ForeignKey(Osoba, on_delete=models.CASCADE) 
    Pokoj = models.ForeignKey(Pomieszczenie, on_delete=models.CASCADE) 
    Termin_rezerwacji = models.DateField()
    Data_zlozenia = models.DateField(null=True, blank=True)
    Cena = models.IntegerField()
    
    def __str__(self):
        return 'Rezerwacja ' + str(self.NrRezerwacji)
   
class Pracownik(models.Model):
    ID_Pracownika = models.OneToOneField(Osoba, on_delete=models.CASCADE)
    Stanowisko = models.CharField(max_length=30)
    Zadanie = models.CharField(max_length=100)
    Haslo = models.CharField(max_length=100)

    def __str__(self):
        return 'Pracownik '+ self.ID_Pracownika.Imie + ' '+ self.ID_Pracownika.Nazwisko
    
class Grafik(models.Model):
    ID_grafik = models.IntegerField()
    ID_Pracownika = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    Miesiac = models.CharField(max_length=20)
    Zmiana = models.IntegerField()

    def __str__(self):
        return 'Grafik' + ' ' + str(self.ID_grafik)

# Create your models here.
