from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import CardTitle, CardContent, CardType

def hello_world(request):
    return HttpResponse("Hello World")

def detail(request, card_id):
    try:
        context = {'card':CardTitle.objects.get(pk=card_id)}
    except:
        raise Http404("Card not found -____-")
    return render(request, 'card/detail.html', context)

def home(request):
    try:
        context = {'cards': CardTitle.objects.all()}
    except:
        raise Http404("Page not found -____-")
    return render(request, 'card/home.html', context)