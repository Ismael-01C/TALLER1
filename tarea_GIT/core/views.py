from django.shortcuts import render
from .models import *
# Create your views here.

def base(request):
    return render(request, 'base.html')

def hijo(request):
    ports = Persona.objects.all()
    return render(request, 'herencias/hijo.html', context= {'Ports': ports})
