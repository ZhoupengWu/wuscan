from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .services.client import isAvaibleBot, sendMessage

def test(request: HttpRequest):
    if not isAvaibleBot():
        return JsonResponse({"err": "Bot non configurato"}, status=503)

    response = sendMessage("Test da Wuscan ✅")

    return JsonResponse(response, status=400 if "err" in response else 200)
