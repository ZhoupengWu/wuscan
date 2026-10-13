from django.shortcuts import render
from django.http import HttpResponse
from .services.db import crea_tabella, aggiungi_nota, leggi_note

def home(request):
    return render(request, "home_test/index.html")

def visualizza(request):
    return HttpResponse("ciaoooo")

def creaTabella(request):
    crea_tabella()

    return HttpResponse(201)

def inserisciDati(request):
    aggiungi_nota()