from django.shortcuts import render
from django.http import HttpResponse
from .models import CardTitle, CardContent, CardType

def hello_world(request):
    return HttpResponse("Hello World")

def home(request):
    context = {'cards': CardTitle.objects.all()}
    return render(request, 'card/home.html', context)