from dataclasses import fields
from tkinter.ttk import Style, Widget
from turtle import color
from .models import Alimentos, Platos
from django import forms
from django.forms import ModelForm


class AlimentoForm(ModelForm):
    class Meta:
        model = Alimentos
        fields = ['nombre','categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'center',
                'style' : 'color: black;'
            }),
            'categoria': forms.TextInput(attrs={
                'class': 'center',
                'style' : 'color: black;'
            })
        }

class PlatoForm(ModelForm):
    class Meta:
        model = Platos
        fields = '__all__'
        labels = {
            'alimentos': 'Ingredientes'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'center',
                'style' : 'color: black;margin-bottom: 20px'
            }),
            'tiempo_preparacion': forms.TimeInput(attrs={
                'class': 'center',
                'style' : 'color: black;margin-bottom: 20px'
            }),
            'categoria': forms.TextInput(attrs={
                'class': 'center',
                'style' : 'color: black;margin-bottom: 25px'
            }),
            'alimentos': forms.CheckboxSelectMultiple(attrs={
                'class': 'center,select',
                'style' : 'color: black;margin-bottom: 10px'
            })
        }
