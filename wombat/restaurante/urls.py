from django.urls import path
from .views import Editar, menu,alimentos,platos,Editar,Crear, Delete,CrearP,EditarP, DeleteP

urlpatterns = [
    path('menu/', menu, name="menup"),
    path('alimentos/',alimentos, name="al"),
    path('platos/',platos, name='pl'),
    path('edit/<int:id>/',Editar, name="edit"),
    path('create/',Crear, name="crear"),
    path('createP/',CrearP, name="crearP"),
    path('editP/<int:id>/',EditarP, name="EditarP"),
    path('DeleteP/<int:id>/',DeleteP, name="EliminarP"),
    path('Eliminar/<int:id>/', Delete, name='delete')
]
