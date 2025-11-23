from django.contrib import admin
from .models import Pasillo, Categoria, Producto


@admin.register(Pasillo)
class PasilloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel_congestion', 'descripcion')
    list_editable = ('nivel_congestion',)
    search_fields = ('nombre',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'padre', 'pasillo')
    list_filter = ('pasillo',)
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'tipo_producto', 'categoria', 'precio', 'stock')
    list_filter = ('categoria', 'marca')
    search_fields = ('nombre', 'marca')
    list_editable = ('precio', 'stock')

