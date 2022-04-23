from rest_framework import serializers
from .models import Alimentos, Platos


class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentos
        fields = ['id','nombre','categoria']


class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platos
        fields = ['id','nombre','tiempo_preparacion','categoria','alimentos']