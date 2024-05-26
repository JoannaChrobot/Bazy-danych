from django import forms 
from .models import Pomieszczenie

class PomieszczenieForm(forms.ModelForm):
    class Meta:
        model = Pomieszczenie
        fields = ['Symbol', 'Zadanie']
