from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("calcular-ruta/", views.calcular_ruta, name="calcular_ruta"),
    path("limpiar/", views.limpiar_seleccion, name="limpiar_seleccion"),
    path("informacion/", views.informacion, name="informacion"),
]
