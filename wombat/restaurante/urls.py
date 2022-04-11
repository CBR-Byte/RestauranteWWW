from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('alimentos',views.alimentos),
    path('platos',views.platos)
]
