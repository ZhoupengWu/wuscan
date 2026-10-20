from django.shortcuts import render
from django.http import HttpRequest

def landingPage(request: HttpRequest):
    return render(request, "landing/index.html")
