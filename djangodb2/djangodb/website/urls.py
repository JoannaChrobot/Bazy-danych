from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('rezerwacje', views.rezerwacje_query_view, name='rezerwacje_query_view'),
    #path('index', views.usun_rezerwacje, name='usun_rezerwacje'),

]
