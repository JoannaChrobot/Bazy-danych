from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name="home"),
    path('rezerwacje', views.rezerwacje_query_view, name='rezerwacje_query_view'),
    path('zadania', views.zadania, name='zadania'),
    path('index', views.glowna_strona, name='index'),
    path('osoby', views.lista_osob, name="osoby"),
    path('pokoje', views.lista_pokoi, name="pokoje"),
    path('grafik', views.grafik, name='grafik'),

]
