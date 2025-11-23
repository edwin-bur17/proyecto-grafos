class Nodo:
    """Nodo de la lista enlazada que contiene un producto."""
    def __init__(self, producto):
        self.producto = producto  # producto es un diccionario con detalles del producto
        self.siguiente = None


class ListaEnlazada:
    """
    Lista enlazada para gestionar la lista de compras.
    Cada nodo contiene un producto que el usuario desea adquirir.
    """
    def __init__(self):
        self.cabeza = None

    def agregar_producto(self, producto):
        """Agrega un producto al final de la lista enlazada."""
        nuevo_nodo = Nodo(producto)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_producto(self, nombre_producto):
        """
        Elimina un producto de la lista por su nombre.
        Retorna True si se eliminó, False si no se encontró.
        """
        if self.cabeza is None:
            return False

        # Si el producto a eliminar está en la cabeza
        if self.cabeza.producto.get('name') == nombre_producto:
            self.cabeza = self.cabeza.siguiente
            return True

        # Buscar en el resto de la lista
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.producto.get('name') == nombre_producto:
                actual.siguiente = actual.siguiente.siguiente
                return True
            actual = actual.siguiente
        
        return False

    def buscar_producto(self, nombre_producto):
        """
        Busca un producto en la lista por su nombre.
        Retorna el producto si se encuentra, None en caso contrario.
        """
        actual = self.cabeza
        while actual:
            if actual.producto.get('name') == nombre_producto:
                return actual.producto
            actual = actual.siguiente
        return None

    def obtener_cantidad(self):
        """Retorna la cantidad de productos en la lista."""
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def esta_vacia(self):
        """Retorna True si la lista está vacía, False en caso contrario."""
        return self.cabeza is None

    def recorrer(self):
        """Recorre la lista enlazada y retorna una lista con los detalles de todos los productos."""
        productos = []
        actual = self.cabeza
        while actual:
            productos.append(actual.producto)
            actual = actual.siguiente
        return productos

    def limpiar(self):
        """Elimina todos los productos de la lista."""
        self.cabeza = None
