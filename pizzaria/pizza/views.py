from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

def menu(request):
    pizzas = Pizza.object.all()
    result = ''
    for pizza in pizzas:
        result += pizza.name
        result += '<br>'
    return HttpResponse(result)
