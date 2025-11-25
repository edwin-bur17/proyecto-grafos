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
    
    # Verificar si estamos en modo "agregar productos"
    modo_agregar = request.session.pop('modo_agregar', False)
    
    context = {
        'productos': productos,
        'categorias': categorias,
        'termino_busqueda': termino_busqueda,
        'categoria_filtro': categoria_filtro,
        'productos_seleccionados': productos_seleccionados,
        'modo_agregar': modo_agregar,
        'num_productos_en_ruta': len(productos_seleccionados) if modo_agregar else 0,
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


def agregar_productos_a_ruta(request):
    """
    Permite agregar más productos a una ruta ya calculada.
    Mantiene los productos actuales y permite seleccionar adicionales.
    """
    # Marcar que estamos en modo "agregar"
    request.session['modo_agregar'] = True
    return redirect('inicio')


def eliminar_producto_de_ruta(request, producto_nombre):
    """
    Elimina un producto específico de la ruta y recalcula.
    Maneja correctamente la sincronización con sessionStorage del frontend.
    """
    productos_seleccionados = request.session.get('productos_seleccionados', [])
    
    if producto_nombre in productos_seleccionados:
        # Eliminar el producto
        productos_seleccionados.remove(producto_nombre)
        request.session['productos_seleccionados'] = productos_seleccionados
        request.session.modified = True  # Forzar guardado de sesión
        
        # Recalcular ruta si quedan productos
        if productos_seleccionados:
            try:
                resultado = views_logic.calcular_ruta_automatica(productos_seleccionados)
                request.session['ruta_resultado'] = resultado
                request.session.modified = True
                messages.success(
                    request, 
                    f'✅ Producto "{producto_nombre}" eliminado. Ruta recalculada con {len(productos_seleccionados)} producto(s).'
                )
            except Exception as e:
                messages.error(request, f'❌ Error al recalcular la ruta: {str(e)}')
                return redirect('inicio')
        else:
            # Si no quedan productos, limpiar todo
            request.session.pop('ruta_resultado', None)
            views_logic.limpiar_lista_compras()
            messages.info(request, '📝 Todos los productos eliminados. Puedes iniciar una nueva compra.')
            return redirect('inicio')
    else:
        messages.warning(request, f'⚠️ El producto "{producto_nombre}" no se encuentra en tu lista.')
    
    return redirect('ruta_resultado')


def informacion(request):
    """Vista de información sobre el proyecto."""
    return render(request, 'informacion.html')
