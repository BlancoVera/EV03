from django.contrib import admin
from .models import Articulos, Categoria

class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')

admin.site.register(Articulos, ArticuloAdmin)
admin.site.register(Categoria, CategoriaAdmin)
