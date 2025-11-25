from .data_estructura.linked_list import ListaEnlazada
from .data_estructura.category_tree import NodoCategoria
from .data_estructura.store_graph import Grafo


# Instancias globales de las estructuras de datos
lista_compras = ListaEnlazada()
grafo_tienda = Grafo()


# ==================== INVENTARIO DE PRODUCTOS ====================

def obtener_inventario_productos():
    """
    Retorna el inventario completo de productos disponibles en la tienda.
    Cada producto incluye: nombre, marca, tipo, presentación, categoría, pasillo.
    """
    return [
        # Pasillo 1 - Lácteos
        {'nombre': 'Leche Alquería', 'marca': 'Alquería', 'tipo': 'Entera', 'presentacion': '1L', 'categoria': 'Lácteos', 'pasillo': 'Pasillo 1'},
        {'nombre': 'Queso Alpina', 'marca': 'Alpina', 'tipo': 'Fresco', 'presentacion': '250g', 'categoria': 'Lácteos', 'pasillo': 'Pasillo 1'},
        {'nombre': 'Yogur Colanta', 'marca': 'Colanta', 'tipo': 'Griego', 'presentacion': '200g', 'categoria': 'Lácteos', 'pasillo': 'Pasillo 1'},
        {'nombre': 'Mantequilla Alpina', 'marca': 'Alpina', 'tipo': 'Con Sal', 'presentacion': '250g', 'categoria': 'Lácteos', 'pasillo': 'Pasillo 1'},
        
        # Pasillo 2 - Aseo
        {'nombre': 'Jabón Dove', 'marca': 'Dove', 'tipo': 'Corporal', 'presentacion': '90g', 'categoria': 'Aseo', 'pasillo': 'Pasillo 2'},
        {'nombre': 'Shampoo Pantene', 'marca': 'Pantene', 'tipo': 'Control Caída', 'presentacion': '400ml', 'categoria': 'Aseo', 'pasillo': 'Pasillo 2'},
        {'nombre': 'Detergente Ariel', 'marca': 'Ariel', 'tipo': 'Líquido', 'presentacion': '2L', 'categoria': 'Aseo', 'pasillo': 'Pasillo 2'},
        {'nombre': 'Crema Dental Colgate', 'marca': 'Colgate', 'tipo': 'Triple Acción', 'presentacion': '100ml', 'categoria': 'Aseo', 'pasillo': 'Pasillo 2'},
        
        # Pasillo 3 - Granos
        {'nombre': 'Arroz Diana', 'marca': 'Diana', 'tipo': 'Extra', 'presentacion': '1kg', 'categoria': 'Granos', 'pasillo': 'Pasillo 3'},
        {'nombre': 'Frijol Rojo', 'marca': 'La Moderna', 'tipo': 'Rojo', 'presentacion': '500g', 'categoria': 'Granos', 'pasillo': 'Pasillo 3'},
        {'nombre': 'Lentejas', 'marca': 'Cosecha Roja', 'tipo': 'Premium', 'presentacion': '500g', 'categoria': 'Granos', 'pasillo': 'Pasillo 3'},
        {'nombre': 'Pasta Doria', 'marca': 'Doria', 'tipo': 'Espagueti', 'presentacion': '500g', 'categoria': 'Granos', 'pasillo': 'Pasillo 3'},
        
        # Pasillo 4 - Bebidas
        {'nombre': 'Coca Cola', 'marca': 'Coca Cola', 'tipo': 'Original', 'presentacion': '2L', 'categoria': 'Bebidas', 'pasillo': 'Pasillo 4'},
        {'nombre': 'Jugo Hit', 'marca': 'Hit', 'tipo': 'Mora', 'presentacion': '1L', 'categoria': 'Bebidas', 'pasillo': 'Pasillo 4'},
        {'nombre': 'Agua Cristal', 'marca': 'Cristal', 'tipo': 'Natural', 'presentacion': '600ml', 'categoria': 'Bebidas', 'pasillo': 'Pasillo 4'},
        {'nombre': 'Té Hatsu', 'marca': 'Hatsu', 'tipo': 'Verde', 'presentacion': '500ml', 'categoria': 'Bebidas', 'pasillo': 'Pasillo 4'},
        
        # Pasillo 5 - Snacks
        {'nombre': 'Papas Margarita', 'marca': 'Margarita', 'tipo': 'Natural', 'presentacion': '150g', 'categoria': 'Snacks', 'pasillo': 'Pasillo 5'},
        {'nombre': 'Chocolate Jet', 'marca': 'Jet', 'tipo': 'Leche', 'presentacion': '35g', 'categoria': 'Snacks', 'pasillo': 'Pasillo 5'},
        {'nombre': 'Galletas Festival', 'marca': 'Festival', 'tipo': 'Chocolate', 'presentacion': '200g', 'categoria': 'Snacks', 'pasillo': 'Pasillo 5'},
        {'nombre': 'Maní Toddy', 'marca': 'Toddy', 'tipo': 'Salado', 'presentacion': '100g', 'categoria': 'Snacks', 'pasillo': 'Pasillo 5'},
        
        # Pasillo 6 - Panadería
        {'nombre': 'Pan Bimbo', 'marca': 'Bimbo', 'tipo': 'Integral', 'presentacion': '450g', 'categoria': 'Panadería', 'pasillo': 'Pasillo 6'},
        {'nombre': 'Pan Integral', 'marca': 'Super Ricas', 'tipo': 'Integral', 'presentacion': '500g', 'categoria': 'Panadería', 'pasillo': 'Pasillo 6'},
        {'nombre': 'Tostadas Doria', 'marca': 'Doria', 'tipo': 'Tradicional', 'presentacion': '300g', 'categoria': 'Panadería', 'pasillo': 'Pasillo 6'},

        # Pasillo 7 - Ropa
        {'nombre': 'Camiseta Adidas Hombre', 'marca': 'Adidas', 'tipo': 'Hombre', 'presentacion': 'M', 'categoria': 'Ropa', 'pasillo': 'Pasillo 7'},
        {'nombre': 'Pantalón Nike Dama', 'marca': 'Nike', 'tipo': 'Dama', 'presentacion': 'S', 'categoria': 'Ropa', 'pasillo': 'Pasillo 7'},
        {'nombre': 'Zapatos Puma Running', 'marca': 'Puma', 'tipo': 'Running', 'presentacion': '40', 'categoria': 'Ropa', 'pasillo': 'Pasillo 7'},

        # Pasillo 8 - Electrodomésticos
        {'nombre': 'Televisor Samsung 55p', 'marca': 'Samsung', 'tipo': 'LED', 'presentacion': '55p', 'categoria': 'Electrodomésticos', 'pasillo': 'Pasillo 8'},
        {'nombre': 'Microondas Haceb 20L', 'marca': 'Haceb', 'tipo': 'Digital', 'presentacion': '20L', 'categoria': 'Electrodomésticos', 'pasillo': 'Pasillo 8'},
        {'nombre': 'Lavadora LG 18kg', 'marca': 'LG', 'tipo': 'Carga Superior', 'presentacion': '18kg', 'categoria': 'Electrodomésticos', 'pasillo': 'Pasillo 8'},
    ]


def construir_arbol_categorias():
    """
    Construye y retorna el árbol de categorías basado en el inventario.
    """
    raiz = NodoCategoria("Tienda")
    inventario = obtener_inventario_productos()
    
    # Agrupar por categoría
    categorias = {}
    for producto in inventario:
        cat = producto['categoria']
        if cat not in categorias:
            categorias[cat] = []
        categorias[cat].append(producto)
    
    # Construir árbol
    for categoria, productos in categorias.items():
        pasillo = productos[0]['pasillo']
        nodo_categoria = NodoCategoria(categoria, pasillo=pasillo)
        
        for prod in productos:
            nodo_producto = NodoCategoria(
                prod['nombre'],
                pasillo=prod['pasillo'],
                es_producto=True
            )
            nodo_categoria.agregar_hijo(nodo_producto)
        
        raiz.agregar_hijo(nodo_categoria)
    
    return raiz


def construir_grafo_tienda():
    """
    Construye y configura el grafo de la tienda con pasillos y conexiones.
    Ahora incluye 4 cajas estratégicamente ubicadas.
    """
    global grafo_tienda
    grafo_tienda = Grafo()
    
    pasillos = {
        "Entrada": 0.3,
        "Pasillo 1": 0.2,
        "Pasillo 2": 0.4,
        "Pasillo 3": 0.1,
        "Pasillo 4": 0.3,
        "Pasillo 5": 0.5,
        "Pasillo 6": 0.2,
        "Pasillo 7": 0.4,
        "Pasillo 8": 0.5,
        "Caja 1": 0.6,  # Cerca de Pasillo 3 y 7
        "Caja 2": 0.6,  # Cerca de Pasillo 6
        "Caja 3": 0.6,  # Cerca de Pasillo 4
        "Caja 4": 0.6,  # Cerca de Pasillo 8
    }
    
    for pasillo, congestion in pasillos.items():
        grafo_tienda.agregar_nodo(pasillo, congestion)
    
    conexiones = [
        # Conexiones de Entrada
        ("Entrada", "Pasillo 1", 1),
        ("Entrada", "Pasillo 4", 2),
        
        # Conexiones entre pasillos - lado izquierdo
        ("Pasillo 1", "Pasillo 2", 1),
        ("Pasillo 2", "Pasillo 3", 1),
        ("Pasillo 3", "Pasillo 7", 1),
        
        # Conexiones entre pasillos - lado derecho
        ("Pasillo 4", "Pasillo 5", 1),
        ("Pasillo 5", "Pasillo 6", 1),
        ("Pasillo 6", "Pasillo 8", 1),
        
        # Conexiones horizontales
        ("Pasillo 1", "Pasillo 4", 2),
        ("Pasillo 2", "Pasillo 5", 2),
        ("Pasillo 3", "Pasillo 6", 2),
        ("Pasillo 7", "Pasillo 8", 2),
        
        # Conexiones a las cajas
        ("Pasillo 3", "Caja 1", 1),
        ("Pasillo 7", "Caja 1", 1),
        ("Pasillo 6", "Caja 2", 1),
        ("Pasillo 4", "Caja 3", 2),
        ("Pasillo 8", "Caja 4", 1),
        
        # Conexiones entre cajas para permitir rutas alternativas
        ("Caja 1", "Caja 2", 2),
        ("Caja 2", "Caja 4", 2),
        ("Caja 3", "Caja 4", 2),
    ]
    
    for desde, hacia, peso in conexiones:
        grafo_tienda.agregar_arista(desde, hacia, peso)


# ==================== OPERACIONES DE LISTA ====================

def agregar_productos_a_lista(nombres_productos):
    """
    Agrega múltiples productos a la lista de compras desde el inventario.
    
    Args:
        nombres_productos: Lista de nombres de productos a agregar
    """
    inventario = obtener_inventario_productos()
    lista_compras.limpiar()  # Limpiar lista anterior
    
    for nombre in nombres_productos:
        # Buscar producto en inventario
        producto = next((p for p in inventario if p['nombre'] == nombre), None)
        if producto:
            lista_compras.agregar_producto(producto)


def limpiar_lista_compras():
    """Elimina todos los productos de la lista."""
    lista_compras.limpiar()


def obtener_productos_seleccionados():
    """Retorna los productos actualmente en la lista de compras."""
    return lista_compras.recorrer()


# ==================== INTEGRACIÓN SIMPLIFICADA ====================

def calcular_ruta_automatica(nombres_productos, pasillo_inicio="Entrada"):
    """
    Calcula automáticamente la ruta óptima para los productos seleccionados.
    **SIEMPRE** inicia en "Entrada" y termina en la caja más cercana al último producto.
    
    Args:
        nombres_productos: Lista de nombres de productos seleccionados
        pasillo_inicio: Ignorado, siempre se usa "Entrada"
    
    Returns:
        dict: Resultado con ruta, productos por pasillo, y costo
    """
    # Agregar productos a la lista
    agregar_productos_a_lista(nombres_productos)
    
    # Construir estructuras de datos
    construir_grafo_tienda()
    arbol = construir_arbol_categorias()
    productos = obtener_productos_seleccionados()
    
    # SIEMPRE iniciar en "Entrada"
    pasillo_inicio = "Entrada"
    
    if not productos:
        return {
            'productos': [],
            'pasillos_necesarios': [],
            'ruta_optima': [],
            'costo_total': 0,
            'productos_por_pasillo': {},
            'mensaje': 'No hay productos seleccionados'
        }
    
    # Mapear productos a pasillos usando el árbol
    pasillos_necesarios = []
    productos_por_pasillo = {}
    
    for producto in productos:
        nombre = producto.get('nombre', '')
        nodo = arbol.buscar_categoria(nombre)
        
        if nodo and nodo.pasillo:
            pasillo = nodo.pasillo
            if pasillo not in pasillos_necesarios:
                pasillos_necesarios.append(pasillo)
            
            if pasillo not in productos_por_pasillo:
                productos_por_pasillo[pasillo] = []
            productos_por_pasillo[pasillo].append(producto)
    
    # Lista de cajas disponibles
    cajas_disponibles = ["Caja 1", "Caja 2", "Caja 3", "Caja 4"]
    
    # Calcular top rutas (usando pasillo_inicio="Entrada")
    if pasillos_necesarios:
        top_rutas = grafo_tienda.calcular_top_rutas(
            pasillos_necesarios,
            inicio=pasillo_inicio,
            top_k=3
        )
        
        rutas_procesadas = []
        for i, (ruta, costo) in enumerate(top_rutas):
            ruta_final = list(ruta)
            costo_final = costo
            
            # Asegurar que SIEMPRE inicie en "Entrada"
            if not ruta_final or ruta_final[0] != "Entrada":
                # Si no inicia en Entrada, calcular ruta desde Entrada al primer punto
                if ruta_final:
                    ruta_desde_entrada, costo_entrada = grafo_tienda.ruta_mas_corta("Entrada", ruta_final[0])
                    if ruta_desde_entrada:
                        ruta_final = ruta_desde_entrada[:-1] + ruta_final
                        costo_final += costo_entrada
                else:
                    ruta_final = ["Entrada"]
            
            # Encontrar la caja más cercana al último pasillo con productos
            if ruta_final and ruta_final[-1] not in cajas_disponibles:
                ultimo_pasillo = ruta_final[-1]
                
                # Buscar la caja más cercana
                mejor_caja = None
                menor_costo_caja = float('inf')
                mejor_ruta_caja = None
                
                for caja in cajas_disponibles:
                    ruta_a_caja, costo_caja = grafo_tienda.ruta_mas_corta(ultimo_pasillo, caja)
                    if ruta_a_caja and costo_caja < menor_costo_caja:
                        menor_costo_caja = costo_caja
                        mejor_caja = caja
                        mejor_ruta_caja = ruta_a_caja
                
                # Agregar ruta a la caja más cercana
                if mejor_ruta_caja:
                    ruta_final.extend(mejor_ruta_caja[1:])  # Evitar duplicar el último pasillo
                    costo_final += menor_costo_caja
            
            rutas_procesadas.append({
                'id': i,
                'nombre': 'Ruta Óptima' if i == 0 else f'Alternativa {i}',
                'ruta': ruta_final,
                'costo': round(costo_final, 2),
                'es_optima': i == 0
            })
            
    else:
        # Caso sin productos: ir de Entrada a la caja más cercana
        mejor_caja = "Caja 1"  # Usar Caja 1 como default
        menor_costo = float('inf')
        mejor_ruta = None
        
        for caja in cajas_disponibles:
            ruta_directa, costo = grafo_tienda.ruta_mas_corta("Entrada", caja)
            if ruta_directa and costo < menor_costo:
                menor_costo = costo
                mejor_caja = caja
                mejor_ruta = ruta_directa
        
        rutas_procesadas = [{
            'id': 0,
            'nombre': 'Ruta Directa',
            'ruta': mejor_ruta if mejor_ruta else ["Entrada", "Caja 1"],
            'costo': round(menor_costo, 2) if mejor_ruta else 0,
            'es_optima': True
        }]
    
    # Seleccionar la primera como activa por defecto
    ruta_activa = rutas_procesadas[0] if rutas_procesadas else None

    return {
        'productos': productos,
        'pasillos_necesarios': pasillos_necesarios,
        'rutas': rutas_procesadas, # Lista de todas las opciones
        'ruta_activa': ruta_activa, # La ruta seleccionada actualmente (para compatibilidad)
        'productos_por_pasillo': productos_por_pasillo,
    }


# ==================== BÚSQUEDA Y FILTRADO ====================

def buscar_productos(termino):
    """
    Busca productos en el inventario que coincidan con el término.
    
    Args:
        termino: Texto a buscar (busca en nombre, marca, categoría)
    
    Returns:
        list: Productos que coinciden con la búsqueda
    """
    if not termino:
        return obtener_inventario_productos()
    
    termino = termino.lower()
    inventario = obtener_inventario_productos()
    
    return [
        p for p in inventario
        if termino in p['nombre'].lower()
        or termino in p['marca'].lower()
        or termino in p['categoria'].lower()
    ]


def obtener_productos_por_categoria(categoria):
    """Retorna todos los productos de una categoría específica."""
    inventario = obtener_inventario_productos()
    return [p for p in inventario if p['categoria'] == categoria]


def obtener_categorias():
    """Retorna lista de todas las categorías disponibles."""
    inventario = obtener_inventario_productos()
    return list(set(p['categoria'] for p in inventario))
