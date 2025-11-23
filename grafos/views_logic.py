from .graph_data_structures.linked_list import LinkedList
from .graph_data_structures.category_tree import CategoryNode
from .graph_data_structures.store_graph import Graph

product_list = LinkedList()

def build_category_tree():
    root = CategoryNode("Root - Árbol de Categorías")

    lacteos = CategoryNode("Lácteos")
    queso = CategoryNode("Queso Alpina")
    queso.add_child(CategoryNode("Marca: Alpina"))
    queso.add_child(CategoryNode("Tipo: Fresco"))
    queso.add_child(CategoryNode("Presentación: 250g"))
    lacteos.add_child(queso)

    yogur = CategoryNode("Yogur Griego Colanta")
    yogur.add_child(CategoryNode("Marca: Colanta"))
    yogur.add_child(CategoryNode("Tipo: Griego"))
    yogur.add_child(CategoryNode("Presentación: 200g"))
    lacteos.add_child(yogur)

    leche = CategoryNode("Leche Alquería")
    leche.add_child(CategoryNode("Marca: Alquería"))
    leche.add_child(CategoryNode("Tipo: Entera"))
    leche.add_child(CategoryNode("Presentación: 1L"))
    lacteos.add_child(leche)

    root.add_child(lacteos)

    aseo = CategoryNode("Aseo")
    jabon = CategoryNode("Jabón Dove")
    jabon.add_child(CategoryNode("Marca: Dove"))
    jabon.add_child(CategoryNode("Tipo: Corporal"))
    jabon.add_child(CategoryNode("Presentación: Barra"))
    aseo.add_child(jabon)

    shampoo = CategoryNode("Shampoo Pantene")
    shampoo.add_child(CategoryNode("Marca: Pantene"))
    shampoo.add_child(CategoryNode("Tipo: Control Caída"))
    shampoo.add_child(CategoryNode("Presentación: 400ml"))
    aseo.add_child(shampoo)

    detergente = CategoryNode("Detergente Ariel")
    detergente.add_child(CategoryNode("Marca: Ariel"))
    detergente.add_child(CategoryNode("Tipo: Líquido"))
    detergente.add_child(CategoryNode("Presentación: 2L"))
    aseo.add_child(detergente)

    root.add_child(aseo)

    granos = CategoryNode("Granos")
    arroz = CategoryNode("Arroz Diana")
    arroz.add_child(CategoryNode("Marca: Diana"))
    arroz.add_child(CategoryNode("Tipo: Extra"))
    arroz.add_child(CategoryNode("Presentación: 1kg"))
    granos.add_child(arroz)

    frijol = CategoryNode("Frijol Rojo La Moderna")
    frijol.add_child(CategoryNode("Marca: La Moderna"))
    frijol.add_child(CategoryNode("Tipo: Rojo"))
    frijol.add_child(CategoryNode("Presentación: 500g"))
    granos.add_child(frijol)

    lentejas = CategoryNode("Lentejas Cosecha Roja")
    lentejas.add_child(CategoryNode("Marca: Cosecha Roja"))
    lentejas.add_child(CategoryNode("Tipo: Premium"))
    lentejas.add_child(CategoryNode("Presentación: 500g"))
    granos.add_child(lentejas)

    root.add_child(granos)

    ropa = CategoryNode("Ropa")
    camiseta = CategoryNode("Camiseta Adidas Hombre")
    camiseta.add_child(CategoryNode("Marca: Adidas"))
    camiseta.add_child(CategoryNode("Tipo: Hombre"))
    camiseta.add_child(CategoryNode("Talla: M"))
    ropa.add_child(camiseta)

    pantalon = CategoryNode("Pantalón Nike Dama")
    pantalon.add_child(CategoryNode("Marca: Nike"))
    pantalon.add_child(CategoryNode("Tipo: Dama"))
    pantalon.add_child(CategoryNode("Talla: S"))
    ropa.add_child(pantalon)

    zapatos = CategoryNode("Zapatos Puma Running")
    zapatos.add_child(CategoryNode("Marca: Puma"))
    zapatos.add_child(CategoryNode("Tipo: Running"))
    zapatos.add_child(CategoryNode("Talla: 40"))
    ropa.add_child(zapatos)

    root.add_child(ropa)

    electro = CategoryNode("Electrodomésticos")
    televisor = CategoryNode("Televisor Samsung 55p")
    televisor.add_child(CategoryNode("Marca: Samsung"))
    televisor.add_child(CategoryNode("Tipo: LED"))
    televisor.add_child(CategoryNode("Modelo: 55p"))
    electro.add_child(televisor)

    microondas = CategoryNode("Microondas Haceb 20L")
    microondas.add_child(CategoryNode("Marca: Haceb"))
    microondas.add_child(CategoryNode("Tipo: Digital"))
    microondas.add_child(CategoryNode("Capacidad: 20L"))
    electro.add_child(microondas)

    lavadora = CategoryNode("Lavadora LG 18kg")
    lavadora.add_child(CategoryNode("Marca: LG"))
    lavadora.add_child(CategoryNode("Tipo: Carga Superior"))
    lavadora.add_child(CategoryNode("Capacidad: 18kg"))
    electro.add_child(lavadora)

    root.add_child(electro)

    return root

store_graph = Graph()

def build_store_graph():
    aisles = ["Pasillo 1", "Pasillo 2", "Pasillo 3", "Pasillo 4", "Pasillo 5", "Pasillo 6"]
    for aisle in aisles:
        store_graph.add_node(aisle)
    store_graph.add_edge("Pasillo 1", "Pasillo 2")
    store_graph.add_edge("Pasillo 2", "Pasillo 3")
    store_graph.add_edge("Pasillo 3", "Pasillo 4")
    store_graph.add_edge("Pasillo 4", "Pasillo 5")
    store_graph.add_edge("Pasillo 5", "Pasillo 6")
    store_graph.add_edge("Pasillo 1", "Pasillo 3")
    store_graph.add_edge("Pasillo 2", "Pasillo 5")
    store_graph.add_edge("Pasillo 4", "Pasillo 6")
    store_graph.add_edge("Pasillo 3", "Pasillo 6")

def add_product_to_list(product_obj):
    product_list.add_product(product_obj)

def get_all_products():
    return product_list.traverse()

def find_category_node(category_name):
    root = build_category_tree()
    return root.find_category(category_name)

def calculate_route(start, end):
    build_store_graph()
    return store_graph.shortest_path(start, end)
