# Grafos

"""
    Un grafo es una estrcutrua de datos que sirve para representar relaciones entre objetos.

    Vértices (o nodos): los elementos u objetos.
    Aristas (o edges): las conexiones o relaciones entre los vértices

    (A) ---- (B)
    |        |
    |        |
   (C) ---- (D)

   Los vértices son: A, B, C, D
   Las artias son: (A-C), (B-D), (A-B), (C-D)

   Tipos de grafos:

   1. Dirigidos y No dirigidos
        * No dirigidos: las relación es mutua. Ejemplo "contactos en tu red social" ( ------ )
        * Dirigidos: las artias tiene dirección. Ejemplo "seguir en Twitter/Instagram" ( ------>, <------)
   2. Ponderados y No Ponderados
        * No ponderado: todas las aristas pesan lo mismo
        * Ponderados: cada artisa tiene un valor (peso, costo, distancia). Ejemplo: mapas que muestran kilómetros
   3. Grados cíclicos y Acíclicos
        * Cícilos: tiene ciclos (pueden empezar en un nodo y regrar al mismo)
        * Acíclicos: No hay ciclos (ejemplo: aun árbol es un grado acíclico)

    Los grafos se pueden represntar de varias formas en estructuras de datos:
    1. Matriz de adyacencia
        * Un tabla de n x n
        * 1 o peso si hay conecion, 0 si no hay.

        Ejemplo para el grafo A-B-C-D
    
        A   B   C   D
    A   0   1   1   0
    B   1   0   0   1
    C   1   0   0   1
    D   0   1   1   0

    Lista de adyacencia
        * Un diccionario o lista donde cada nodeo guardo sus vecinos

        grafo = {
            "A": ["B", "C"],
            "B": ["A", "D"],
            "C": ["A", "D"],
            "D": ["B", "C"]        
        }
"""

class Grafo:
    def __init__(self):
        self.grafo = {} # Dict

    def agregar_vertices(self, v):
        if v not in self.grafo:
            self.grafo[v] = []

    def agregar_artias(self, v1, v2):
        self.grafo[v1].append(v2)
        self.grafo[v2].append(v1) # Grafo no dirigido

    def mostrar_grafo(self):
        for vertice in self.grafo:
            print(vertice, "-", self.grafo[vertice])

# Caso de uso
g = Grafo()
g.agregar_vertices("A")
g.agregar_vertices("B")
g.agregar_vertices("C")
g.agregar_vertices("D")

g.agregar_artias("A", "B")
g.agregar_artias("A", "C")
g.agregar_artias("B", "D")
g.agregar_artias("C", "D")

g.mostrar_grafo()