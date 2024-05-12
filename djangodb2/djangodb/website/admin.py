from django.contrib import admin
from .models import Osoba
from .models import Pomieszczenie
from .models import Rezerwacja
from .models import Pracownik
from .models import Grafik

admin.site.register(Osoba)
admin.site.register(Pomieszczenie)
admin.site.register(Rezerwacja)
admin.site.register(Pracownik)
admin.site.register(Grafik)

# Register your models here.
