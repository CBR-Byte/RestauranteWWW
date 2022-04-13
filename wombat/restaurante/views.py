from django.shortcuts import render
from .models import Platos, Alimentos

# Create your views here.


def menu(request):
    return render(request,'menup.html')

def alimentos(request):
    alimento = Alimentos.objects.all()
    return render(request,'alimentos.html',{'al' : alimento})

def platos(request):
    plato = Platos.objects.all()
    print(plato)
    return render(request,'platos.html',{'pl' : plato})