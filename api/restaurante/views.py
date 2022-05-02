from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Alimentos, Platos
from .serializers import PlatoSerializer, AlimentoSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'integrantes': 'Julián Leal-1860143, Cristhian Botero-1860054',
        'Lista de alimentos': '/alimentos/',
        'Crear Alimentos': '/crearA/',
        'Editar alimento': '/editA/<str:id>',
        'Eliminar': '/deleteA/<str:id>',
        'Lista de platos': '/platos/',
        'Crear Plato': '/crearP/',
        'Editar plato': '/editP/<str:id>',
        'Eliminar plato': '/deleteP/<str:id>',
    }

    return Response(api_urls)

@api_view(['GET'])
def alimentos(request):
    a = Alimentos.objects.all()
    serializer = AlimentoSerializer(a,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def crearA(request):
    serializer = AlimentoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def editA(request,id):
    a = Alimentos.objects.get(id=id)
    serializer = AlimentoSerializer(instance=a,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteA(request,id):
    a = Alimentos.objects.get(id=id)
    a.delete()
    return Response("Deleteado")

@api_view(['GET'])
def platos(request):
    a = Platos.objects.all()
    serializer = PlatoSerializer(a,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crearP(request):
    serializer = PlatoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def editP(request,id):
    a = Platos.objects.get(id=id)
    serializer = PlatoSerializer(instance=a,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteP(request,id):
    a = Platos.objects.get(id=id)
    a.delete()
    return Response("Deleteado")