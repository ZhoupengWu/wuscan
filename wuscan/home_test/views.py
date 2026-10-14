from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from .services.db import crea_tabella, aggiungi_nota, leggi_note
from django.views.decorators.http import require_POST

def home(request: HttpRequest):
    return render(request, "home_test/index.html")

def visualizza(request: HttpRequest):
    rows = leggi_note()
    data = [{"id": r[0], "text": r[1], "colpo": r[2]} for r in rows]

    return JsonResponse({"scanner": data})

def creaTabella(request: HttpRequest):
    crea_tabella()

    return HttpResponse("Table created", status=201)

@require_POST
def inserisciDati(request: HttpRequest):
    text = request.POST.get("text", "").strip().lower()
    colpo = request.POST.get("colpo", "").strip().lower()

    if not text or not colpo:
        return HttpResponse("Obbligo compilazione dati", status=400)

    aggiungi_nota(text, colpo)

    return HttpResponse("Dati inseriti", status=201)
