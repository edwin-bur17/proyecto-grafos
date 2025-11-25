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
    
    # 1. Obtener inventario base
    productos = inventario
    
    # 2. Filtrar por categoría si existe
    if categoria_filtro:
        productos = [p for p in productos if p['categoria'] == categoria_filtro]
        
    # 3. Filtrar por búsqueda si existe
    if termino_busqueda:
        termino = termino_busqueda.lower()
        productos = [
            p for p in productos
            if termino in p['nombre'].lower()
            or termino in p['marca'].lower()
            or termino in p['categoria'].lower()
        ]
    
    # Obtener productos seleccionados desde la sesión
    productos_seleccionados = request.session.get('productos_seleccionados', [])
    
    context = {
        'productos': productos,
        'categorias': categorias,
        'termino_busqueda': termino_busqueda,
        'categoria_filtro': categoria_filtro,
        'productos_seleccionados': productos_seleccionados,
    }
    
    return render(request, 'inicio.html', context)


def calcular_ruta(request):
    """
    Calcula la ruta óptima automáticamente para los productos seleccionados.
    Guarda los resultados en sesión y redirige a la página de resultados.
    """
    if request.method == 'POST':
        # Obtener productos seleccionados (checkboxes)
        productos_seleccionados = request.POST.getlist('productos')
        
        if not productos_seleccionados:
            messages.warning(request, 'Por favor seleccione al menos un producto')
            return redirect('inicio')
        
        # Calcular ruta automáticamente
        resultado = views_logic.calcular_ruta_automatica(productos_seleccionados)
        
        # Guardar resultados en sesión
        request.session['ruta_resultado'] = resultado
        request.session['productos_seleccionados'] = productos_seleccionados
        
        # Redirigir a página de resultados
        return redirect('ruta_resultado')
    
    return redirect('inicio')


def ver_ruta_resultado(request):
    """
    Muestra la página de resultados con la ruta calculada.
    """
    ruta_resultado = request.session.get('ruta_resultado')
    productos_seleccionados = request.session.get('productos_seleccionados', [])
    
    context = {
        'ruta_resultado': ruta_resultado,
        'productos_seleccionados': productos_seleccionados,
    }
    
    return render(request, 'ruta_resultado.html', context)


def limpiar_seleccion(request):
    """Limpia la selección de productos y resultados."""
    views_logic.limpiar_lista_compras()
    # Limpiar datos de sesión
    request.session.pop('productos_seleccionados', None)
    request.session.pop('ruta_resultado', None)
    messages.success(request, 'Selección limpiada')
    return redirect('inicio')


def informacion(request):
    """Vista de información sobre el proyecto."""
    return render(request, 'informacion.html')
