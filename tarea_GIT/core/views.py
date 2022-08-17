from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html')

def hijo(request):
    return render(request, 'hijo.html')

