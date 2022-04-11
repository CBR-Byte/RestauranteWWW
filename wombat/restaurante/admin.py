from django.contrib import admin
from .models import Alimentos,Platos

# Register your models here.


class alimentosAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','categoria')
    fields = ('nombre','categoria')

class platosAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','tiempo_preparacion','categoria')

admin.site.register(Alimentos,alimentosAdmin)
admin.site.register(Platos,platosAdmin)