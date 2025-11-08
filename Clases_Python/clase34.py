#Kruskal

"""
    Kruskal es un algoritmo que sirve para contruir un Árbol Generador Mínimo (MST = Minimum Spanning Tree)
    Un subconjunto de aristas que conceta todos los nodos del grafo sin ciclos y con el menor costo posible

    ¿En que tipo de grafo puedo usar Kustkal?
        * Grafos ponderados
        * Grafos no dirigidos

    ¿Para qué sirve en la vida real?
        * Diseño de redes
        * Diseño de telefocinas
        * Diseño de carreteras
        * Optimización logística de costos cuando necesitas conectar todo pero gastando los menor posible

    Introducción simple
        1. Ordena Todas las coneciones por costo de menor a mayor
        2. Elegir las conexiones más baratas
        3. Agregar esa conexción "SOLO SI NO FORMA UN CICLO"
        4. Conectar todo

    ¿Cómo detecta ciclos?
    DSU (Union-Find)
    Union-Find sirve para saber si dos nodos "ya están conectados" en la red que se está formando

        * Si ya están conectados -> esa arista crearía un ciclo -> la rechazamos
        * Si no están conectados -> la aceptamos y unimos ambos conjutos

    O(E log E)


    ---------------------------------------------------------------------------------------------
    ordener todas las artias por peso ascendente

    para cada arista (u, v) en el orden:
        si u y v NO están conectados (DSU):
            agregar arista al MST
            unir u y v en DSU

    regresar MST final 
    ---------------------------------------------------------------------------------------------


    Resultado 
    Kruskal procede un conjuto de aristas que:
        * conecta todos los nodos
        * con suma total de pesos mínima
        * sin ciclos

    Ejemplo simple conceptual
    Imagina 5 cuidad con estos costos:

    conecixión                  peso
    A-B                          4
    A-C                          1
    C-B                          3
    B-D                          2
    C-D                          5

    Ordenar
    1 -> A-C(1)
    2 -> B-D(2)
    3 -> C-B(3)
    4 -> A-B(4)
    5 -> C-D(5)

    Construcción:
    * tomo A-C [x]
    * tomo B-D [x]
    * tomo C-B [x]
    * A-B -> rechazamos (porque ya conecta ciclo: A-C-B-A)
    * C-D -> rechazamos (por que ya conecta ciclo: C-B-D-C)

    MST final = {A-C, B-D, C-B}
    Costo total = 1 + 2 + 3 = 6
    
"""

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # comparación de caminos
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
        elif self.rank[b] < self.rank[a]:
            self.parent[b] = a
        else:
            self.parent[b] = a
            self.rank[a] += 1
        return True
    
def kruskal (n, edges):
    """
    n = número de nodos
    edges = lista de (peso, u, v)
    """
    dsu = DSU(n) # obj
    edges.sort() # ordenamos de peso ascedente
    mst_cost = 0
    mst = []

    for w, u, v in edges:
        if dsu.union(u, v): # si los une = NO había ciclo
            mst_cost += w
            mst.append((u, v, w))

    return mst_cost, mst

# Ejemplo de uso
edges = [
    (4, 0, 1),
    (1, 0, 2),
    (3, 2, 1),
    (2, 1, 3),
    (5, 2, 3),
]

mst_cost, mst = kruskal(4, edges)
print("Costo total del MST: ", mst_cost)
print("Aristas seleccionadas: ", mst)