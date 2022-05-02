from rest_framework import serializers
from .models import Alimentos, Platos


class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentos
        fields = ['id','nombre','categoria']


class PlatoSerializer(serializers.ModelSerializer):
    #alimentos = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Platos
        fields = ['id','nombre','tiempo_preparacion','categoria','alimentos']