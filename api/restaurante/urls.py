from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.apiOverview,name="api-overview"),
    path('alimentos/',views.alimentos,name='al'),
    path('crearA/',views.crearA,name="ca"),
    path('editA/<str:id>',views.editA,name="ea"),
    path('deleteA/<str:id>',views.deleteA,name="da"),
    path('platos/',views.platos,name='pl'),
    path('crearP/',views.crearP,name="cp"),
    path('editP/<str:id>',views.editP,name="ep"),
    path('deleteP/<str:id>',views.deleteP,name="dp")
]