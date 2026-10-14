from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("visualizza/", views.visualizza, name="visualizza"),
    path("crea-tabella/", views.creaTabella, name="crea-tabella"),
    path("inserisci/", views.inserisciDati, name="inserisci"),
]