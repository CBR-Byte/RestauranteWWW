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
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>',
        'Detale': '/task-delate/<str:pk>',
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