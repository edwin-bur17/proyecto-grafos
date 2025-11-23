from django.shortcuts import render, redirect
from django.contrib import messages
from . import views_logic


def inicio(request):
    """
    Vista principal con inventario de productos y cálculo automático de ruta.
    """
    inventario = views_logic.obtener_inventario_productos()
    categorias = views_logic.obtener_categorias()
    
    # Filtrado por búsqueda o categoría
    termino_busqueda = request.GET.get('buscar', '')
    categoria_filtro = request.GET.get('categoria', '')
    
    if termino_busqueda:
        productos = views_logic.buscar_productos(termino_busqueda)
    elif categoria_filtro:
        productos = views_logic.obtener_productos_por_categoria(categoria_filtro)
    else:
        productos = inventario
    
    context = {
        'productos': productos,
        'categorias': categorias,
        'termino_busqueda': termino_busqueda,
        'categoria_filtro': categoria_filtro,
    }
    
    return render(request, 'inicio.html', context)


def calcular_ruta(request):
    """
    Calcula la ruta óptima automáticamente para los productos seleccionados.
    Siempre inicia en Entrada y termina en Caja.
    """
    if request.method == 'POST':
        # Obtener productos seleccionados (checkboxes)
        productos_seleccionados = request.POST.getlist('productos')
        # Obtener pasillo de inicio si está disponible (por ejemplo, de un campo en el formulario)
        pasillo_inicio = request.POST.get('pasillo_inicio', 'Entrada')
        
        if not productos_seleccionados:
            messages.warning(request, 'Por favor seleccione al menos un producto')
            return redirect('inicio')
        
        # Calcular ruta automáticamente pasando pasillo inicio
        resultado = views_logic.calcular_ruta_automatica(productos_seleccionados, pasillo_inicio=pasillo_inicio)
        
        # Preparar contexto para mostrar resultados
        inventario = views_logic.obtener_inventario_productos()
        categorias = views_logic.obtener_categorias()
        
        context = {
            'productos': inventario,
            'categorias': categorias,
            'ruta_resultado': resultado,
            'productos_seleccionados': productos_seleccionados,
            'pasillo_inicio': pasillo_inicio,
        }
        
        return render(request, 'inicio.html', context)
    
    return redirect('inicio')


def limpiar_seleccion(request):
    """Limpia la selección de productos y resultados."""
    views_logic.limpiar_lista_compras()
    messages.success(request, 'Selección limpiada')
    return redirect('inicio')


def informacion(request):
    """Vista de información sobre el proyecto."""
    return render(request, 'informacion.html')
