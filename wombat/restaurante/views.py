from django.shortcuts import render
from .models import Platos, Alimentos

# Create your views here.

def index(request):

    return render(request,'index.html')

def alimentos(request):
    alimento = Alimentos.objects.all()
    return render(request,'alimentos.html',{'al' : alimento})

def platos(request):
    plato = Platos.objects.all()
    print(plato)
    return render(request,'platos.html',{'pl' : plato})