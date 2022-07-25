from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "AppFinal/index.html", {})

def nosotros(request):
    return render(request, "AppFinal/nosotros.html", {})

def reseñas(request):
    return render(request, "AppFinal/reseñas.html", {})



