from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('calcular-ruta/', views.calcular_ruta, name='calcular_ruta'),
    path('ruta-resultado/', views.ver_ruta_resultado, name='ruta_resultado'),
    path('limpiar-seleccion/', views.limpiar_seleccion, name='limpiar_seleccion'),
    path('agregar-productos/', views.agregar_productos_a_ruta, name='agregar_productos'),
    path('eliminar-producto/<str:producto_nombre>/', views.eliminar_producto_de_ruta, name='eliminar_producto'),
    path('informacion/', views.informacion, name='informacion'),
]
