from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>I am from firt app of index!</h1>")

def contact(request):
    diction = {'text_1':'I am a text sent from views.py'}
    return render(request, 'first_app/index.html', context=diction)
