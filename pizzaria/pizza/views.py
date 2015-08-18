from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

def menu(request):
    #import ipdb: ipdb.set_trace()
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizza/menu.html', context)
