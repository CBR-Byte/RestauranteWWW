from django.urls import path
from .views import menu,alimentos,platos

urlpatterns = [
    path('menu', menu, name="menup"),
    path('alimentos',alimentos),
    path('platos',platos)
]
