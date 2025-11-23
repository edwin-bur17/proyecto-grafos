import heapq
from itertools import permutations


class Grafo:
    """
    Grafo que representa las rutas dentro de la tienda.
    Cada nodo es un pasillo y las aristas representan conexiones entre pasillos.
    Incluye soporte para niveles de congestión que afectan el peso de las rutas.
    """
    def __init__(self):
        self.nodos = set()
        self.aristas = {}  # lista de adyacencia: nodo -> lista de (vecino, peso_base)
        self.congestion = {}  # nodo -> nivel de congestión (0.0 a 1.0)

    def agregar_nodo(self, nodo, nivel_congestion=0.0):
        """Agrega un nodo (pasillo) al grafo con un nivel inicial de congestión."""
        self.nodos.add(nodo)
        if nodo not in self.aristas:
            self.aristas[nodo] = []
        if nodo not in self.congestion:
            self.congestion[nodo] = nivel_congestion

    def agregar_arista(self, desde_nodo, hacia_nodo, peso=1):
        """
        Agrega una arista bidireccional entre dos nodos.
        El peso representa la distancia base entre pasillos.
        """
        self.agregar_nodo(desde_nodo)
        self.agregar_nodo(hacia_nodo)
        self.aristas[desde_nodo].append((hacia_nodo, peso))
        self.aristas[hacia_nodo].append((desde_nodo, peso))  # grafo no dirigido

    def actualizar_congestion(self, pasillo, nivel):
        """
        Actualiza el nivel de congestión de un pasillo.
        nivel debe estar entre 0.0 (vacío) y 1.0 (muy congestionado).
        """
        if pasillo in self.nodos:
            self.congestion[pasillo] = max(0.0, min(1.0, nivel))

    def obtener_peso_real(self, nodo, peso_base):
        """
        Calcula el peso real considerando la congestión.
        A mayor congestión, mayor el peso (menos deseable la ruta).
        """
        factor_congestion = 1 + (self.congestion.get(nodo, 0.0) * 2)  # Multiplica hasta 3x
        return peso_base * factor_congestion

    def ruta_mas_corta(self, inicio, fin, considerar_congestion=True):
        """
        Retorna la ruta más corta desde inicio hasta fin usando el algoritmo de Dijkstra.
        Si considerar_congestion es True, incluye los niveles de congestión en el cálculo.
        Retorna una tupla (ruta, costo_total) o (None, None) si no hay ruta.
        """
        if inicio not in self.nodos or fin not in self.nodos:
            return None, None

        cola = [(0, inicio, [])]
        visitados = set()
        
        while cola:
            (costo, actual, ruta) = heapq.heappop(cola)
            
            if actual in visitados:
                continue
            
            ruta = ruta + [actual]
            
            if actual == fin:
                return ruta, costo
            
            visitados.add(actual)
            
            for (vecino, peso_base) in self.aristas.get(actual, []):
                if vecino not in visitados:
                    if considerar_congestion:
                        peso = self.obtener_peso_real(vecino, peso_base)
                    else:
                        peso = peso_base
                    heapq.heappush(cola, (costo + peso, vecino, ruta))
        
        return None, None  # no se encontró ruta

    def calcular_ruta_optima(self, lista_pasillos, inicio=None, considerar_congestion=True):
        """
        Calcula la ruta óptima para visitar múltiples pasillos.
        Usa un enfoque de fuerza bruta para listas pequeñas (<8 pasillos).
        
        Args:
            lista_pasillos: Lista de pasillos a visitar
            inicio: Pasillo de inicio (opcional, si None usa el primero de la lista)
            considerar_congestion: Si debe considerar niveles de congestión
            
        Returns:
            Tupla (ruta_completa, costo_total) con la mejor ruta encontrada
        """
        if not lista_pasillos:
            return [], 0
        
        # Eliminar duplicados manteniendo el orden
        pasillos_unicos = []
        vistos = set()
        for p in lista_pasillos:
            if p not in vistos:
                pasillos_unicos.append(p)
                vistos.add(p)
        
        if len(pasillos_unicos) == 1:
            return pasillos_unicos, 0
        
        # Si hay un inicio específico, lo usamos
        if inicio and inicio in pasillos_unicos:
            pasillos_unicos.remove(inicio)
            pasillos_a_permutar = pasillos_unicos
            punto_inicio = inicio
        else:
            punto_inicio = pasillos_unicos[0]
            pasillos_a_permutar = pasillos_unicos[1:]
        
        mejor_ruta = None
        mejor_costo = float('inf')
        
        # Probar todas las permutaciones posibles
        for permutacion in permutations(pasillos_a_permutar):
            orden = [punto_inicio] + list(permutacion)
            ruta_completa = []
            costo_total = 0
            valida = True
            
            for i in range(len(orden) - 1):
                ruta_segmento, costo_segmento = self.ruta_mas_corta(
                    orden[i], orden[i + 1], considerar_congestion
                )
                
                if ruta_segmento is None:
                    valida = False
                    break
                
                # Agregar segmento evitando duplicar nodos
                if i == 0:
                    ruta_completa.extend(ruta_segmento)
                else:
                    ruta_completa.extend(ruta_segmento[1:])
                
                costo_total += costo_segmento
            
            if valida and costo_total < mejor_costo:
                mejor_costo = costo_total
                mejor_ruta = ruta_completa
        
        return mejor_ruta if mejor_ruta else [], mejor_costo

    def obtener_info_nodo(self, nodo):
        """Retorna información detallada sobre un nodo."""
        if nodo not in self.nodos:
            return None
        
        vecinos = [v[0] for v in self.aristas.get(nodo, [])]
        return {
            'nombre': nodo,
            'congestion': self.congestion.get(nodo, 0.0),
            'vecinos': vecinos,
            'num_conexiones': len(vecinos)
        }

    def obtener_todos_nodos(self):
        """Retorna información de todos los nodos del grafo."""
        return [self.obtener_info_nodo(nodo) for nodo in sorted(self.nodos)]
