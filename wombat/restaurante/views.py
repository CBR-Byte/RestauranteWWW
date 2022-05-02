from email import message
from multiprocessing import context
from tkinter import N
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Platos, Alimentos
from .forms import AlimentoForm, PlatoForm
from django.contrib import messages

# Create your views here.

def menu(request):
    return render(request,'menup.html')

def alimentos(request):
    alimento = Alimentos.objects.all()
    context = {
        'al': alimento
    }
    return render(request,"alimentos.html",context)

def platos(request):
    plato = Platos.objects.all()
    context = {
        'pl': plato
    }
    return render(request,'platos.html',context)

def Editar(request,id):

    if Alimentos.objects.filter(id=id).exists():
        alimento = Alimentos.objects.get(pk=id)
        form = AlimentoForm(instance=alimento)

        if request.method == 'POST':
            form = AlimentoForm(request.POST, instance=alimento)
            if form.is_valid():
                form.save()
                messages.info(request, 'Se ha editado el alimento correctamente!')
                return redirect('al')
        context = {
            'form': form
        }  
        return render(request, "editar.html",context)

def EditarP(request,id):

    if Platos.objects.filter(id=id).exists():
        pl = Platos.objects.get(pk=id)
        form = PlatoForm(instance=pl)

        if request.method == 'POST':
            form = PlatoForm(request.POST, instance=pl)
            if form.is_valid():
                form.save()
                messages.info(request, 'Se ha editado el plato correctamente!')
                return redirect('pl')
        context = {
            'form': form
        }  
        return render(request, "editP.html",context)

def CrearP(request):
    form = PlatoForm()
    if request.method=='POST':
        form = PlatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha creado el plato correctamente!')
            return redirect('pl')
    context = {
        'form' : form,
    }   
    return render(request, "CrearP.html",context)

def Crear(request):

    form = AlimentoForm()
    if request.method=='POST':
        form = AlimentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha creado el alimento correctamente!')
            return redirect('al')
    context = {
        'form' : form,
    }   
    
    return render(request, "Crear.html",context)

def Delete(request,id):
    alimento = Alimentos.objects.get(id=id)

    if request.method == 'POST':
        alimento.delete()
        messages.error(request, 'Se ha eliminado el alimento correctamente!')
        return redirect('al')

    context = {
        'al': alimento
    }

    return render(request, "Eliminar.html",context)

def DeleteP(request,id):
    pl = Platos.objects.get(id=id)

    if request.method == 'POST':
        pl.delete()
        messages.error(request, 'Se ha eliminado el plato correctamente!')
        return HttpResponseRedirect(reverse_lazy('pl'))

    context = {
        'pl': pl
    }

    return render(request, "DeleteP.html",context)
    