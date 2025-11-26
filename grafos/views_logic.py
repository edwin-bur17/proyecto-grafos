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
    Cada producto incluye: nombre, marca, tipo, presentación, categoría, pasillo (estante).
    
    IMPORTANTE: Los 'pasillos' ahora representan ESTANTES donde se almacenan los productos,
    no los caminos de tránsito. Los caminos son nodos separados en el grafo.
    """
    return [
        # Estante Lácteos
        {'nombre': 'Leche Alquería', 'marca': 'Alquería', 'tipo': 'Entera', 'presentacion': '1L', 'categoria': 'Lácteos', 'pasillo': 'Estante Lácteos'},
        {'nombre': 'Queso Alpina', 'marca': 'Alpina', 'tipo': 'Fresco', 'presentacion': '250g', 'categoria': 'Lácteos', 'pasillo': 'Estante Lácteos'},
        {'nombre': 'Yogur Colanta', 'marca': 'Colanta', 'tipo': 'Griego', 'presentacion': '200g', 'categoria': 'Lácteos', 'pasillo': 'Estante Lácteos'},
        {'nombre': 'Mantequilla Alpina', 'marca': 'Alpina', 'tipo': 'Con Sal', 'presentacion': '250g', 'categoria': 'Lácteos', 'pasillo': 'Estante Lácteos'},
        {'nombre': 'Crema de Leche', 'marca': 'Colanta', 'tipo': 'Original', 'presentacion': '200ml', 'categoria': 'Lácteos', 'pasillo': 'Estante Lácteos'},
        
        # Estante Frutas y Verduras
        {'nombre': 'Manzana Roja', 'marca': 'Fresco', 'tipo': 'Nacional', 'presentacion': '1kg', 'categoria': 'Frutas', 'pasillo': 'Estante Frutas'},
        {'nombre': 'Banano', 'marca': 'Fresco', 'tipo': 'Orgánico', 'presentacion': '1kg', 'categoria': 'Frutas', 'pasillo': 'Estante Frutas'},
        {'nombre': 'Naranja', 'marca': 'Fresco', 'tipo': 'Valencia', 'presentacion': '1kg', 'categoria': 'Frutas', 'pasillo': 'Estante Frutas'},
        {'nombre': 'Lechuga', 'marca': 'Fresco', 'tipo': 'Crespa', 'presentacion': '1un', 'categoria': 'Verduras', 'pasillo': 'Estante Verduras'},
        {'nombre': 'Tomate', 'marca': 'Fresco', 'tipo': 'Chonto', 'presentacion': '500g', 'categoria': 'Verduras', 'pasillo': 'Estante Verduras'},
        {'nombre': 'Zanahoria', 'marca': 'Fresco', 'tipo': 'Nacional', 'presentacion': '500g', 'categoria': 'Verduras', 'pasillo': 'Estante Verduras'},
        {'nombre': 'Cebolla', 'marca': 'Fresco', 'tipo': 'Cabezona', 'presentacion': '500g', 'categoria': 'Verduras', 'pasillo': 'Estante Verduras'},
        
        # Estante Aseo Personal
        {'nombre': 'Jabón Dove', 'marca': 'Dove', 'tipo': 'Corporal', 'presentacion': '90g', 'categoria': 'Aseo Personal', 'pasillo': 'Estante Aseo'},
        {'nombre': 'Shampoo Pantene', 'marca': 'Pantene', 'tipo': 'Control Caída', 'presentacion': '400ml', 'categoria': 'Aseo Personal', 'pasillo': 'Estante Aseo'},
        {'nombre': 'Crema Dental Colgate', 'marca': 'Colgate', 'tipo': 'Triple Acción', 'presentacion': '100ml', 'categoria': 'Aseo Personal', 'pasillo': 'Estante Aseo'},
        {'nombre': 'Desodorante Rexona', 'marca': 'Rexona', 'tipo': 'Clinical', 'presentacion': '50ml', 'categoria': 'Aseo Personal', 'pasillo': 'Estante Aseo'},
        {'nombre': 'Acondicionador Sedal', 'marca': 'Sedal', 'tipo': 'Brillo', 'presentacion': '350ml', 'categoria': 'Aseo Personal', 'pasillo': 'Estante Aseo'},
        
        # Estante Limpieza
        {'nombre': 'Detergente Ariel', 'marca': 'Ariel', 'tipo': 'Líquido', 'presentacion': '2L', 'categoria': 'Limpieza', 'pasillo': 'Estante Limpieza'},
        {'nombre': 'Suavizante Suavitel', 'marca': 'Suavitel', 'tipo': 'Durazzno', 'presentacion': '1L', 'categoria': 'Limpieza', 'pasillo': 'Estante Limpieza'},
        {'nombre': 'Limpiapisos Fabuloso', 'marca': 'Fabuloso', 'tipo': 'Lavanda', 'presentacion': '1L', 'categoria': 'Limpieza', 'pasillo': 'Estante Limpieza'},
        {'nombre': 'Cloro Clorox', 'marca': 'Clorox', 'tipo': 'Original', 'presentacion': '1L', 'categoria': 'Limpieza', 'pasillo': 'Estante Limpieza'},
        {'nombre': 'Lavavajillas Axión', 'marca': 'Axión', 'tipo': 'Limón', 'presentacion': '500ml', 'categoria': 'Limpieza', 'pasillo': 'Estante Limpieza'},
        
        # Estante Granos y Cereales
        {'nombre': 'Arroz Diana', 'marca': 'Diana', 'tipo': 'Extra', 'presentacion': '1kg', 'categoria': 'Granos', 'pasillo': 'Estante Granos'},
        {'nombre': 'Frijol Rojo', 'marca': 'La Moderna', 'tipo': 'Rojo', 'presentacion': '500g', 'categoria': 'Granos', 'pasillo': 'Estante Granos'},
        {'nombre': 'Lentejas', 'marca': 'Cosecha Roja', 'tipo': 'Premium', 'presentacion': '500g', 'categoria': 'Granos', 'pasillo': 'Estante Granos'},
        {'nombre': 'Avena Quaker', 'marca': 'Quaker', 'tipo': 'Hojuelas', 'presentacion': '500g', 'categoria': 'Cereales', 'pasillo': 'Estante Granos'},
        {'nombre': 'Cereal Zucaritas', 'marca': 'Kelloggs', 'tipo': 'Original', 'presentacion': '400g', 'categoria': 'Cereales', 'pasillo': 'Estante Granos'},
        
        # Estante Pastas y Harinas
        {'nombre': 'Pasta Doria', 'marca': 'Doria', 'tipo': 'Espagueti', 'presentacion': '500g', 'categoria': 'Pastas', 'pasillo': 'Estante Pastas'},
        {'nombre': 'Pasta Lasagna', 'marca': 'Doria', 'tipo': 'Lasagna', 'presentacion': '500g', 'categoria': 'Pastas', 'pasillo': 'Estante Pastas'},
        {'nombre': 'Harina PAN', 'marca': 'PAN', 'tipo': 'Blanca', 'presentacion': '1kg', 'categoria': 'Harinas', 'pasillo': 'Estante Pastas'},
        {'nombre': 'Harina de Trigo', 'marca': 'Haz de Oros', 'tipo': 'Todo uso', 'presentacion': '1kg', 'categoria': 'Harinas', 'pasillo': 'Estante Pastas'},
        
        # Estante Bebidas
        {'nombre': 'Coca Cola', 'marca': 'Coca Cola', 'tipo': 'Original', 'presentacion': '2L', 'categoria': 'Bebidas', 'pasillo': 'Estante Bebidas'},
        {'nombre': 'Jugo Hit', 'marca': 'Hit', 'tipo': 'Mora', 'presentacion': '1L', 'categoria': 'Bebidas', 'pasillo': 'Estante Bebidas'},
        {'nombre': 'Agua Cristal', 'marca': 'Cristal', 'tipo': 'Natural', 'presentacion': '600ml', 'categoria': 'Bebidas', 'pasillo': 'Estante Bebidas'},
        {'nombre': 'Té Hatsu', 'marca': 'Hatsu', 'tipo': 'Verde', 'presentacion': '500ml', 'categoria': 'Bebidas', 'pasillo': 'Estante Bebidas'},
        {'nombre': 'Gaseosa Colombiana', 'marca': 'Postobón', 'tipo': 'Original', 'presentacion': '1.5L', 'categoria': 'Bebidas', 'pasillo': 'Estante Bebidas'},
        
        # Estante Snacks y Dulces
        {'nombre': 'Papas Margarita', 'marca': 'Margarita', 'tipo': 'Natural', 'presentacion': '150g', 'categoria': 'Snacks', 'pasillo': 'Estante Snacks'},
        {'nombre': 'Chocolate Jet', 'marca': 'Jet', 'tipo': 'Leche', 'presentacion': '35g', 'categoria': 'Dulces', 'pasillo': 'Estante Snacks'},
        {'nombre': 'Galletas Festival', 'marca': 'Festival', 'tipo': 'Chocolate', 'presentacion': '200g', 'categoria': 'Snacks', 'pasillo': 'Estante Snacks'},
        {'nombre': 'Maní Toddy', 'marca': 'Toddy', 'tipo': 'Salado', 'presentacion': '100g', 'categoria': 'Snacks', 'pasillo': 'Estante Snacks'},
        {'nombre': 'Chicles Trident', 'marca': 'Trident', 'tipo': 'Menta', 'presentacion': '12un', 'categoria': 'Dulces', 'pasillo': 'Estante Snacks'},
        {'nombre': 'Gomitas Bon Bon Bum', 'marca': 'Colombina', 'tipo': 'Surtidas', 'presentacion': '100g', 'categoria': 'Dulces', 'pasillo': 'Estante Snacks'},
        
        # Estante Panadería
        {'nombre': 'Pan Bimbo', 'marca': 'Bimbo', 'tipo': 'Integral', 'presentacion': '450g', 'categoria': 'Panadería', 'pasillo': 'Estante Panadería'},
        {'nombre': 'Pan Integral', 'marca': 'Super Ricas', 'tipo': 'Integral', 'presentacion': '500g', 'categoria': 'Panadería', 'pasillo': 'Estante Panadería'},
        {'nombre': 'Tostadas Doria', 'marca': 'Doria', 'tipo': 'Tradicional', 'presentacion': '300g', 'categoria': 'Panadería', 'pasillo': 'Estante Panadería'},
        {'nombre': 'Pandebono', 'marca': 'La Especial', 'tipo': 'Congelado', 'presentacion': '500g', 'categoria': 'Panadería', 'pasillo': 'Estante Panadería'},

        # Estante Carnes y Embutidos
        {'nombre': 'Salchicha Zenú', 'marca': 'Zenú', 'tipo': 'Suiza', 'presentacion': '500g', 'categoria': 'Embutidos', 'pasillo': 'Estante Carnes'},
        {'nombre': 'Jamón de Pierna', 'marca': 'Pietran', 'tipo': 'Ahumado', 'presentacion': '250g', 'categoria': 'Embutidos', 'pasillo': 'Estante Carnes'},
        {'nombre': 'Pollo Entero', 'marca': 'Piko', 'tipo': 'Fresco', 'presentacion': '1.5kg', 'categoria': 'Carnes', 'pasillo': 'Estante Carnes'},
        {'nombre': 'Carne Molida', 'marca': 'Guadalupe', 'tipo': 'Res', 'presentacion': '500g', 'categoria': 'Carnes', 'pasillo': 'Estante Carnes'},
        
        # Estante Congelados
        {'nombre': 'Pizza Congelada', 'marca': 'Mr. Pizza', 'tipo': 'Hawaiana', 'presentacion': '400g', 'categoria': 'Congelados', 'pasillo': 'Estante Congelados'},
        {'nombre': 'Helado Crem Helado', 'marca': 'Crem Helado', 'tipo': 'Vainilla', 'presentacion': '1L', 'categoria': 'Congelados', 'pasillo': 'Estante Congelados'},
        {'nombre': 'Verduras Mixtas', 'marca': 'La Huerta', 'tipo': 'Congeladas', 'presentacion': '500g', 'categoria': 'Congelados', 'pasillo': 'Estante Congelados'},
        
        # Estante Mascotas
        {'nombre': 'Alimento Perros Pedigree', 'marca': 'Pedigree', 'tipo': 'Adultos', 'presentacion': '2kg', 'categoria': 'Mascotas', 'pasillo': 'Estante Mascotas'},
        {'nombre': 'Alimento Gatos Whiskas', 'marca': 'Whiskas', 'tipo': 'Adultos', 'presentacion': '1kg', 'categoria': 'Mascotas', 'pasillo': 'Estante Mascotas'},
        {'nombre': 'Arena para Gatos', 'marca': 'Catsan', 'tipo': 'Aglutinante', 'presentacion': '4kg', 'categoria': 'Mascotas', 'pasillo': 'Estante Mascotas'},
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
    Construye y configura el grafo de la tienda usando analogía de Google Maps.
    
    LAYOUT: Cuadrícula de pasillos paralelos (similar a supermercado real)
    - Pasillos = 3 columnas verticales paralelas
    - Estantes = Rectángulos a los lados de cada pasillo
    - Entrada conecta directamente a los pasillos
    """
    global grafo_tienda
    grafo_tienda = Grafo()
    
    # Definir RUTAS DE NAVEGACIÓN (pasillos en cuadrícula)
    pasillos = {
        "Entrada": 0.2,
        
        # Pasillo 1 (Izquierda) - 3 segmentos verticales
        "Pasillo 1 Norte": 0.2,
        "Pasillo 1 Centro": 0.2,
        "Pasillo 1 Sur": 0.2,
        
        # Pasillo 2 (Centro) - 3 segmentos verticales
        "Pasillo 2 Norte": 0.2,
        "Pasillo 2 Centro": 0.2,
        "Pasillo 2 Sur": 0.2,
        
        # Pasillo 3 (Derecha) - 3 segmentos verticales
        "Pasillo 3 Norte": 0.2,
        "Pasillo 3 Centro": 0.2,
        "Pasillo 3 Sur": 0.2,
        
        # Cajas (4 en total)
        "Caja 1": 0.6,
        "Caja 2": 0.6,
        "Caja 3": 0.6,
        "Caja 4": 0.6,
    }
    
    # Definir BLOQUES DE DESTINO (estantes)
    estantes = {
        "Estante Lácteos": 0.3,
        "Estante Frutas": 0.2,
        "Estante Verduras": 0.2,
        "Estante Aseo": 0.3,
        "Estante Limpieza": 0.3,
        "Estante Granos": 0.2,
        "Estante Pastas": 0.2,
        "Estante Bebidas": 0.4,
        "Estante Snacks": 0.3,
        "Estante Panadería": 0.3,
        "Estante Carnes": 0.4,
        "Estante Congelados": 0.4,
        "Estante Mascotas": 0.2,
    }
    
    # Agregar todos los nodos
    for nodo, congestion in {**pasillos, **estantes}.items():
        grafo_tienda.agregar_nodo(nodo, congestion)
    
    # CONEXIONES (mantener todas para cálculo de rutas)
    conexiones = [
        # Entrada conecta directamente a los 3 pasillos Norte
        ("Entrada", "Pasillo 1 Norte", 1),
        ("Entrada", "Pasillo 2 Norte", 1),
        ("Entrada", "Pasillo 3 Norte", 1),
        
        # PASILLO 1 (flujo vertical)
        ("Pasillo 1 Norte", "Pasillo 1 Centro", 1),
        ("Pasillo 1 Centro", "Pasillo 1 Sur", 1),
        
        # PASILLO 2 (flujo vertical)
        ("Pasillo 2 Norte", "Pasillo 2 Centro", 1),
        ("Pasillo 2 Centro", "Pasillo 2 Sur", 1),
        
        # PASILLO 3 (flujo vertical)
        ("Pasillo 3 Norte", "Pasillo 3 Centro", 1),
        ("Pasillo 3 Centro", "Pasillo 3 Sur", 1),
        
        # Conexiones horizontales entre pasillos (para rutas alternativas)
        ("Pasillo 1 Norte", "Pasillo 2 Norte", 2),
        ("Pasillo 2 Norte", "Pasillo 3 Norte", 2),
        ("Pasillo 1 Centro", "Pasillo 2 Centro", 2),
        ("Pasillo 2 Centro", "Pasillo 3 Centro", 2),
        ("Pasillo 1 Sur", "Pasillo 2 Sur", 2),
        ("Pasillo 2 Sur", "Pasillo 3 Sur", 2),
        
        # ESTANTES conectados a pasillos
        ("Pasillo 1 Norte", "Estante Lácteos", 0.5),
        ("Pasillo 1 Norte", "Estante Aseo", 0.5),
        ("Pasillo 1 Centro", "Estante Frutas", 0.5),
        ("Pasillo 1 Centro", "Estante Limpieza", 0.5),
        ("Pasillo 1 Sur", "Estante Verduras", 0.5),
        ("Pasillo 1 Sur", "Estante Granos", 0.5),
        
        ("Pasillo 2 Norte", "Estante Pastas", 0.5),
        ("Pasillo 2 Centro", "Estante Panadería", 0.5),
        ("Pasillo 2 Sur", "Estante Bebidas", 0.5),
        
        ("Pasillo 3 Norte", "Estante Snacks", 0.5),
        ("Pasillo 3 Centro", "Estante Carnes", 0.5),
        ("Pasillo 3 Sur", "Estante Congelados", 0.5),
        ("Pasillo 3 Sur", "Estante Mascotas", 0.5),
        
        # Pasillos a Cajas (4 cajas)
        ("Pasillo 1 Sur", "Caja 1", 1),
        ("Pasillo 2 Sur", "Caja 2", 1),
        ("Pasillo 2 Sur", "Caja 3", 1),
        ("Pasillo 3 Sur", "Caja 4", 1),
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
    
    # Lista de cajas disponibles (ahora 4)
    cajas_disponibles = ["Caja 1", "Caja 2", "Caja 3", "Caja 4"]
    
    # Agrupar estantes por pasillo de tránsito más cercano
    if pasillos_necesarios:
        pasillos_transito = {}  # {pasillo_nodo: [estantes]}
        
        for estante in pasillos_necesarios:
            pasillo_cercano = None
            min_distancia = float('inf')
            
            # Buscar el nodo de pasillo más cercano
            for nodo in grafo_tienda.nodos:
                if "Pasillo" in nodo and nodo != "Entrada":
                    ruta, costo = grafo_tienda.ruta_mas_corta(nodo, estante)
                    if ruta and costo < min_distancia:
                        min_distancia = costo
                        pasillo_cercano = nodo
            
            if pasillo_cercano:
                if pasillo_cercano not in pasillos_transito:
                    pasillos_transito[pasillo_cercano] = []
                pasillos_transito[pasillo_cercano].append(estante)
        
        # CRÍTICO: Obtener lista ÚNICA de pasillos (sin duplicados)
        pasillos_a_visitar = list(pasillos_transito.keys())
        
        if pasillos_a_visitar:
            # Calcular las mejores rutas entre pasillos
            top_rutas_pasillos = grafo_tienda.calcular_top_rutas(
                pasillos_a_visitar,
                inicio=None,  # Sin inicio forzado
                top_k=3
            )
            
            rutas_procesadas = []
            for i, (orden_pasillos, costo_entre_pasillos) in enumerate(top_rutas_pasillos):
                # FILTRAR: Remover "Entrada" y duplicados de la lista de pasillos
                orden_pasillos_limpio = []
                vistos = set()
                for p in orden_pasillos:
                    if p != "Entrada" and p not in vistos:
                        orden_pasillos_limpio.append(p)
                        vistos.add(p)
                
                # Construir ruta completa
                ruta_completa = ["Entrada"]
                costo_total = 0
                
                # Para cada pasillo en el orden LIMPIO (sin duplicados ni Entrada)
                for idx_pasillo, pasillo in enumerate(orden_pasillos_limpio):
                    # Calcular ruta desde el punto actual al pasillo
                    punto_actual = ruta_completa[-1]
                    
                    if punto_actual != pasillo:
                        ruta_al_pasillo, costo_al_pasillo = grafo_tienda.ruta_mas_corta(punto_actual, pasillo)
                        if ruta_al_pasillo:
                            # CRÍTICO: Filtrar "Entrada" de rutas intermedias
                            if "Entrada" in ruta_al_pasillo[1:]:
                                # La ruta pasa por Entrada - buscar alternativa
                                # Intentar ruta horizontal a través de Pasillo 2
                                ruta_alternativa = None
                                
                                # Extraer el número de pasillo (1, 2, 3) y nivel (Norte, Centro, Sur)
                                def extraer_info_pasillo(nombre):
                                    partes = nombre.split()
                                    if len(partes) >= 3 and partes[0] == "Pasillo":
                                        try:
                                            numero = int(partes[1])
                                            nivel = partes[2] if len(partes) > 2 else ""
                                            return numero, nivel
                                        except:
                                            pass
                                    return None, None
                                
                                num_actual, nivel_actual = extraer_info_pasillo(punto_actual)
                                num_destino, nivel_destino = extraer_info_pasillo(pasillo)
                                
                                # Si ambos son pasillos con info válida
                                if num_actual and num_destino and nivel_actual:
                                    # Construir ruta horizontal
                                    ruta_horizontal = []
                                    
                                    if num_actual < num_destino:
                                        # Ir de izquierda a derecha
                                        for n in range(num_actual, num_destino + 1):
                                            nodo = f"Pasillo {n} {nivel_actual}"
                                            if nodo in grafo_tienda.nodos:
                                                ruta_horizontal.append(nodo)
                                    else:
                                        # Ir de derecha a izquierda
                                        for n in range(num_actual, num_destino - 1, -1):
                                            nodo = f"Pasillo {n} {nivel_actual}"
                                            if nodo in grafo_tienda.nodos:
                                                ruta_horizontal.append(nodo)
                                    
                                    # Si el nivel cambia, agregar movimiento vertical
                                    if nivel_destino != nivel_actual and num_destino in [1, 2, 3]:
                                        nodo_destino_final = f"Pasillo {num_destino} {nivel_destino}"
                                        if nodo_destino_final in grafo_tienda.nodos:
                                            if nodo_destino_final not in ruta_horizontal:
                                                ruta_horizontal.append(nodo_destino_final)
                                    
                                    if ruta_horizontal and len(ruta_horizontal) > 1:
                                        # Usar ruta horizontal construida
                                        ruta_completa.extend(ruta_horizontal[1:])  # Sin duplicar punto actual
                                        # Costo aproximado
                                        costo_total += len(ruta_horizontal) - 1
                                    else:
                                        # Fallback: agregar solo el destino
                                        ruta_completa.append(pasillo)
                                else:
                                    # No se pudo construir ruta horizontal - agregar destino directamente
                                    ruta_completa.append(pasillo)
                                    print(f"⚠️ Advertencia: Salto directo de {punto_actual} a {pasillo}")
                            else:
                                # Ruta válida sin Entrada
                                ruta_completa.extend(ruta_al_pasillo[1:])
                                costo_total += costo_al_pasillo
                    
                    # Visitar estantes en este pasillo
                    estantes = pasillos_transito.get(pasillo, [])
                    for estante in estantes:
                        # Ir al estante
                        if estante not in ruta_completa:
                            ruta_al_estante, costo_estante = grafo_tienda.ruta_mas_corta(pasillo, estante)
                            if ruta_al_estante and len(ruta_al_estante) > 1:
                                ruta_completa.append(estante)
                                costo_total += costo_estante
                                # Volver al pasillo
                                ruta_completa.append(pasillo)
                                costo_total += costo_estante
                
                # Ir a la caja más cercana
                ultimo_punto = ruta_completa[-1]
                if ultimo_punto not in cajas_disponibles:
                    mejor_caja = None
                    menor_costo_caja = float('inf')
                    
                    for caja in cajas_disponibles:
                        ruta_a_caja, costo_caja = grafo_tienda.ruta_mas_corta(ultimo_punto, caja)
                        if ruta_a_caja and costo_caja < menor_costo_caja:
                            mejor_caja = ruta_a_caja
                            menor_costo_caja = costo_caja
                    
                    if mejor_caja:
                        ruta_completa.extend(mejor_caja[1:])
                        costo_total += menor_costo_caja
                
                # DEBUG: Imprimir la ruta para diagnóstico
                print(f"\n{'='*60}")
                print(f"DEBUG - RUTA {i+1} ({'ÓPTIMA' if i == 0 else 'ALTERNATIVA'})")
                print(f"{'='*60}")
                print(f"Pasillos originales: {orden_pasillos}")
                print(f"Pasillos limpios: {orden_pasillos_limpio}")
                print(f"Ruta completa generada:")
                for idx, nodo in enumerate(ruta_completa):
                    print(f"  {idx}: {nodo}")
                print(f"Costo total: {costo_total}")
                
                # Verificar si Entrada aparece más de una vez
                entrada_count = ruta_completa.count("Entrada")
                if entrada_count > 1:
                    print(f"❌ ERROR: 'Entrada' aparece {entrada_count} veces!")
                else:
                    print(f"✅ OK: 'Entrada' aparece solo 1 vez")
                print(f"{'='*60}\n")
                
                rutas_procesadas.append({
                    'id': i,
                    'nombre': 'Ruta Óptima' if i == 0 else f'Alternativa {i}',
                    'ruta': ruta_completa,
                    'costo': round(costo_total, 2),
                    'es_optima': i == 0
                })
        else:
            rutas_procesadas = []
    else:
        # Caso sin productos: calcular distancias a todas las cajas desde Entrada
        distancias_cajas = []
        for caja in cajas_disponibles:
            ruta_directa, costo = grafo_tienda.ruta_mas_corta("Entrada", caja)
            if ruta_directa:
                distancias_cajas.append({
                    'caja': caja,
                    'ruta': ruta_directa,
                    'costo': costo
                })
        
        # Ordenar por costo y seleccionar la más cercana
        if distancias_cajas:
            distancias_cajas.sort(key=lambda x: x['costo'])
            mejor_opcion = distancias_cajas[0]
            
            rutas_procesadas = [{
                'id': 0,
                'nombre': 'Ruta Directa',
                'ruta': mejor_opcion['ruta'],
                'costo': round(mejor_opcion['costo'], 2),
                'es_optima': True
            }]
        else:
            # Fallback extremo si no hay rutas válidas
            rutas_procesadas = [{
                'id': 0,
                'nombre': 'Ruta Directa',
                'ruta': ["Entrada", "Caja 1"],
                'costo': 0,
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
        'graph_structure': {
            'nodes': [
                # ENTRADA (arriba centro)
                {'id': 'Entrada', 'label': '🚪', 'type': 'start', 'icon': '🚪', 'position': {'x': 0, 'y': -650}},
                
                # PASILLO 1 (columna izquierda) - 3 segmentos verticales
                {'id': 'Pasillo 1 Norte', 'label': '', 'type': 'aisle', 'icon': '', 'position': {'x': -400, 'y': -350}},
                {'id': 'Pasillo 1 Centro', 'label': '', 'type': 'aisle', 'icon': '', 'position': {'x': -400, 'y': 0}},
                {'id': 'Pasillo 1 Sur', 'label': '', 'type': 'aisle', 'icon': '', 'position': {'x': -400, 'y': 350}},
                
                # PASILLO 2 (columna centro) - 3 segmentos verticales
                {'id': 'Pasillo 2 Norte', 'label': '', 'type': 'aisle', 'icon': '', 'position': {'x': 0, 'y': -350}},
                {'id': 'Pasillo 2 Centro', 'label': '', 'type': 'aisle', 'icon': '', 'position': {'x': 0, 'y': 0}},
                {'id': 'Pasillo 2 Sur', 'label': '', 'type': 'aisle', 'icon': '', 'position': {'x': 0, 'y': 350}},
                
                # PASILLO 3 (columna derecha) - 3 segmentos verticales
                {'id': 'Pasillo 3 Norte', 'label': '', 'type': 'aisle', 'icon': '', 'position': {'x': 400, 'y': -350}},
                {'id': 'Pasillo 3 Centro', 'label': '', 'type': 'aisle', 'icon': '', 'position': {'x': 400, 'y': 0}},
                {'id': 'Pasillo 3 Sur', 'label': '', 'type': 'aisle', 'icon': '', 'position': {'x': 400, 'y': 350}},
                
                # ESTANTES - PASILLO 1 OESTE (lado izquierdo)
                {'id': 'Estante Lácteos', 'label': 'Lácteos', 'type': 'shelf', 'icon': '🥛', 'position': {'x': -550, 'y': -350}},
                {'id': 'Estante Frutas', 'label': 'Frutas', 'type': 'shelf', 'icon': '🍎', 'position': {'x': -550, 'y': 0}},
                {'id': 'Estante Verduras', 'label': 'Verduras', 'type': 'shelf', 'icon': '🥬', 'position': {'x': -550, 'y': 350}},
                
                # ESTANTES - PASILLO 1 ESTE (lado derecho)
                {'id': 'Estante Aseo', 'label': 'Aseo', 'type': 'shelf', 'icon': '🧼', 'position': {'x': -250, 'y': -350}},
                {'id': 'Estante Limpieza', 'label': 'Limpieza', 'type': 'shelf', 'icon': '🧹', 'position': {'x': -250, 'y': 0}},
                {'id': 'Estante Granos', 'label': 'Granos', 'type': 'shelf', 'icon': '🌾', 'position': {'x': -250, 'y': 350}},
                
                # ESTANTES - PASILLO 2 OESTE
                {'id': 'Estante Pastas', 'label': 'Pastas', 'type': 'shelf', 'icon': '🍝', 'position': {'x': -150, 'y': -350}},
                {'id': 'Estante Panadería', 'label': 'Panadería', 'type': 'shelf', 'icon': '🍞', 'position': {'x': -150, 'y': 0}},
                {'id': 'Estante Bebidas', 'label': 'Bebidas', 'type': 'shelf', 'icon': '🥤', 'position': {'x': -150, 'y': 350}},
                
                # ESTANTES - PASILLO 3 OESTE
                {'id': 'Estante Snacks', 'label': 'Snacks', 'type': 'shelf', 'icon': '🍿', 'position': {'x': 250, 'y': -350}},
                {'id': 'Estante Carnes', 'label': 'Carnes', 'type': 'shelf', 'icon': '🥩', 'position': {'x': 250, 'y': 0}},
                {'id': 'Estante Congelados', 'label': 'Congelados', 'type': 'shelf', 'icon': '🧊', 'position': {'x': 250, 'y': 350}},
                
                # ESTANTES - PASILLO 3 ESTE
                {'id': 'Estante Mascotas', 'label': 'Mascotas', 'type': 'shelf', 'icon': '🐕', 'position': {'x': 550, 'y': 350}},
                
                # CAJAS (4 al final, alineadas horizontalmente)
                {'id': 'Caja 1', 'label': '💳', 'type': 'end', 'icon': '💳', 'position': {'x': -300, 'y': 550}},
                {'id': 'Caja 2', 'label': '💳', 'type': 'end', 'icon': '💳', 'position': {'x': -100, 'y': 550}},
                {'id': 'Caja 3', 'label': '💳', 'type': 'end', 'icon': '💳', 'position': {'x': 100, 'y': 550}},
                {'id': 'Caja 4', 'label': '💳', 'type': 'end', 'icon': '💳', 'position': {'x': 300, 'y': 550}}
            ],
            'edges': [
                # Entrada a pasillos Norte (conexiones directas)
                {'from': 'Entrada', 'to': 'Pasillo 1 Norte', 'weight': 1},
                {'from': 'Entrada', 'to': 'Pasillo 2 Norte', 'weight': 1},
                {'from': 'Entrada', 'to': 'Pasillo 3 Norte', 'weight': 1},
                
                # PASILLO 1 (flujo vertical)
                {'from': 'Pasillo 1 Norte', 'to': 'Pasillo 1 Centro', 'weight': 1},
                {'from': 'Pasillo 1 Centro', 'to': 'Pasillo 1 Sur', 'weight': 1},
                
                # PASILLO 2 (flujo vertical)
                {'from': 'Pasillo 2 Norte', 'to': 'Pasillo 2 Centro', 'weight': 1},
                {'from': 'Pasillo 2 Centro', 'to': 'Pasillo 2 Sur', 'weight': 1},
                
                # PASILLO 3 (flujo vertical)
                {'from': 'Pasillo 3 Norte', 'to': 'Pasillo 3 Centro', 'weight': 1},
                {'from': 'Pasillo 3 Centro', 'to': 'Pasillo 3 Sur', 'weight': 1},
                
                # Conexiones horizontales entre pasillos
                {'from': 'Pasillo 1 Norte', 'to': 'Pasillo 2 Norte', 'weight': 2},
                {'from': 'Pasillo 2 Norte', 'to': 'Pasillo 3 Norte', 'weight': 2},
                {'from': 'Pasillo 1 Centro', 'to': 'Pasillo 2 Centro', 'weight': 2},
                {'from': 'Pasillo 2 Centro', 'to': 'Pasillo 3 Centro', 'weight': 2},
                {'from': 'Pasillo 1 Sur', 'to': 'Pasillo 2 Sur', 'weight': 2},
                {'from': 'Pasillo 2 Sur', 'to': 'Pasillo 3 Sur', 'weight': 2},
                
                # ESTANTES en PASILLO 1
                {'from': 'Pasillo 1 Norte', 'to': 'Estante Lácteos', 'weight': 0.5},
                {'from': 'Pasillo 1 Norte', 'to': 'Estante Aseo', 'weight': 0.5},
                {'from': 'Pasillo 1 Centro', 'to': 'Estante Frutas', 'weight': 0.5},
                {'from': 'Pasillo 1 Centro', 'to': 'Estante Limpieza', 'weight': 0.5},
                {'from': 'Pasillo 1 Sur', 'to': 'Estante Verduras', 'weight': 0.5},
                {'from': 'Pasillo 1 Sur', 'to': 'Estante Granos', 'weight': 0.5},
                
                # ESTANTES en PASILLO 2
                {'from': 'Pasillo 2 Norte', 'to': 'Estante Pastas', 'weight': 0.5},
                {'from': 'Pasillo 2 Centro', 'to': 'Estante Panadería', 'weight': 0.5},
                {'from': 'Pasillo 2 Sur', 'to': 'Estante Bebidas', 'weight': 0.5},
                
                # ESTANTES en PASILLO 3
                {'from': 'Pasillo 3 Norte', 'to': 'Estante Snacks', 'weight': 0.5},
                {'from': 'Pasillo 3 Centro', 'to': 'Estante Carnes', 'weight': 0.5},
                {'from': 'Pasillo 3 Sur', 'to': 'Estante Congelados', 'weight': 0.5},
                {'from': 'Pasillo 3 Sur', 'to': 'Estante Mascotas', 'weight': 0.5},
                
                # Pasillos a Cajas (4 cajas)
                {'from': 'Pasillo 1 Sur', 'to': 'Caja 1', 'weight': 1},
                {'from': 'Pasillo 2 Sur', 'to': 'Caja 2', 'weight': 1},
                {'from': 'Pasillo 2 Sur', 'to': 'Caja 3', 'weight': 1},
                {'from': 'Pasillo 3 Sur', 'to': 'Caja 4', 'weight': 1}
            ]
        }
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
