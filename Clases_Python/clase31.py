# Bellaman-Ford
"""
El algoritmo de Bellman-Ford se ultiza para encontrar el camino más corto desde un nodo origen a todos los demás en un grafgo ponderado (ya sea dirigido o no dirigido).

Esto lo hace ideal para situaciones desde los "costos" pueden representar pérdidas, descuentos o penalizaciones, no solo distancias positivas.

Bellman-Ford sigue un enfoque de relajación repetida:
    1. Inicializa las distancias:
        * dist[origen] = 0
        * dist[otros] = ∞
    2. Repite (V - 1) veces (v es el número de vértices):
        * Para cada arista (u -> v) con peso w:
            * Si dist[u] + w < dist[v], entonces acutliza:
                dist[v] = dist[u] + w
    3. Al final, haz un iteración extra:
        * Si alguna distancia puede seguir reduciéndose, significa que existe un ciclo negativo (un bucle que reduce idefinidamente el costo total)

    ¿Qué es un ciclo negativo?
    Un ciclo negativo es un camino cerrado donde la suma de los pesos es menor que 0. Esto implica que podrías "dar vueltas infititas" reduciendo el costo sin límite.

    Ejemplo IRL:
    Imagina un moneda que puedes cambiar de una divisa a otra:

        * 1 USD -> 0.9 EUR
        * 1 EUR -> 120 JPY
        * 120 JPY -> 0.7 USD

    Si vuelves al inidio terminas con menos dinero del que tenías, hay un ciclo negativo

    Camino              Peso
    A -> B               4
    A -> C               2
    C -> B              -2
    B -> D               2
    C -> D               3

    1. Inicialización
    dist[A] = 0
    dist[B] = ∞
    dist[C] = ∞
    dist[D] = ∞

    2. Iteración
    A -> B: dist[B] = 4
    A -> C: dist[C] = 2
    C -> B: dist[B] = 0 (2+(-2))
    B -> D: dist[D] = 2 (0 + 2)
    C -> D: dist[D] = min(2, 2 + 3) = 2

    ¿dist[C] + 3 < dist[D]?
    -> ¿2 + 3 < 2? -> ¿5 < 2? NO
    No actualizamos NADA

    Resultado
    A: 0, B:0, C:2, D:2

    Complejidad
    Tipo          Complejidad
    Tiempo        O(V x E)(más lento que Dijkstra)
    Espacio       O(V)
    Por eso se usa Bellman-Ford solo cuando hay posibilidad de peso negativos.
"""

from math import inf

def bellman_ford(grafo, origen):
    """
    Calcula las distancias mínimas desde 'origen a todos los nodos. 'grafo dede ser una lista de aristas [(u, v, peso)...]
    """
    # Extraer todos los vértices
    vertices = set()
    for u, v, _ in grafo:
        vertices.add(u)
        vertices.add(v)
    
    # Inicialicación
    dist = {v: inf for v in vertices}
    dist[origen] = 0
    previo = {v: None for v in vertices}

    # Relajación reptida (V - 1 vences)
    for _ in range(len(vertices) - 1):
        actulizado = False
        for u, v, w in grafo:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                previo[v] = u
                actulizado = True
        if not actulizado:
            break # optimización
    
    #Comprobacion de ciclo negativos
    for u, v, w in grafo:
        if dist[u] + w < dist[v]:
            raise ValueError("El grafo contiene un ciclo negativo.")
        
    return dist, previo


# Ejemplo de uso

grafo = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("C", "B", -2),
    ("B", "D", 2),
    ("C", "D", 3)
]

dist, previo = bellman_ford(grafo, "A")

print("Distancias mínimas desde A: ")
for nodo in dist:
    print(f"A -> {nodo}: {dist[nodo]}")

