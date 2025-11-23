class NodoCategoria:
    """
    Nodo del árbol de categorías que representa la estructura jerárquica de la tienda.
    Cada nodo puede ser una categoría principal, subcategoría o producto.
    """
    def __init__(self, nombre, atributos=None, pasillo=None, es_producto=False):
        self.nombre = nombre
        self.atributos = atributos if atributos else {}
        self.hijos = []
        self.pasillo = pasillo  # Pasillo donde se encuentra esta categoría/producto
        self.es_producto = es_producto  # Indica si este nodo es un producto final
        self.padre = None  # Referencia al nodo padre

    def agregar_hijo(self, nodo_hijo):
        """Agrega un nodo hijo a este nodo."""
        self.hijos.append(nodo_hijo)
        nodo_hijo.padre = self  # Establecer referencia al padre

    def buscar_categoria(self, nombre):
        """
        Búsqueda recursiva para encontrar un nodo de categoría por nombre.
        Retorna el nodo si se encuentra, None en caso contrario.
        """
        if self.nombre == nombre:
            return self
        for hijo in self.hijos:
            resultado = hijo.buscar_categoria(nombre)
            if resultado:
                return resultado
        return None

    def obtener_productos(self):
        """
        Obtiene todos los productos (nodos hoja) dentro de esta categoría.
        Retorna una lista de nodos que son productos.
        """
        productos = []
        if self.es_producto:
            productos.append(self)
        for hijo in self.hijos:
            productos.extend(hijo.obtener_productos())
        return productos

    def obtener_ruta_completa(self):
        """
        Obtiene la ruta completa desde la raíz hasta este nodo.
        Retorna una lista de nombres de nodos.
        """
        ruta = [self.nombre]
        nodo_actual = self.padre
        while nodo_actual:
            ruta.insert(0, nodo_actual.nombre)
            nodo_actual = nodo_actual.padre
        return ruta

    def obtener_nivel(self):
        """Retorna el nivel de profundidad de este nodo (0 para la raíz)."""
        nivel = 0
        nodo_actual = self.padre
        while nodo_actual:
            nivel += 1
            nodo_actual = nodo_actual.padre
        return nivel

    def recorrer(self, profundidad=0):
        """Recorre el árbol de categorías e imprime los nodos con indentación."""
        print('  ' * profundidad + self.nombre)
        for hijo in self.hijos:
            hijo.recorrer(profundidad + 1)

    def recorrer_lista(self, profundidad=0):
        """
        Recorre el árbol y retorna una lista de diccionarios con información de cada nodo.
        Útil para serializar el árbol y enviarlo al frontend.
        """
        resultado = [{
            'nombre': self.nombre,
            'profundidad': profundidad,
            'pasillo': self.pasillo,
            'es_producto': self.es_producto,
            'atributos': self.atributos
        }]
        for hijo in self.hijos:
            resultado.extend(hijo.recorrer_lista(profundidad + 1))
        return resultado
