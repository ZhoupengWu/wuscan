from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home_test/index.html")

def visualizza(request):
    return HttpResponse("ciaoooo")