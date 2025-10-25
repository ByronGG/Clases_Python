# Floy-Warshall
"""
    El algoritmo de Floyd-Warshall sirve para encontrar el camino más corto entre todos los pares de vértices de un grafo ponderador (con o sin dirección).

    Dijktra -> desde un nodo origen
    Bellman-Ford -> desde un nodo origen (pero con pesos negativos)
    Floyd-Warshall -> de todo a todos.

    Imagina que tienes una tabla con las distancais directas entre todas las ciudades. Floy-Warshall initenta mejorar esas distancais preguntándoce constantemente:

    ¿Hay una ruta más corta de 'i' a 'j' pasando por algún nodo 'k' intermedio?
    Si sí -> actualiza la distancia

    Es un enfoque de programación dinamica, donde cada celda dist[i][j] se va refinando conforme probamos TODOS LOS POSIBLES NODOS INTERMEDIOS

    3 Ciudades A, B y C

    Origen          Destino         Distancia
    A -> B             4
    A -> C             11
    B -> C             2

    El objetivo: "saber la distancia más corta entre todas las combianaciones posibles"
    De entra:
        * A->B=4
        * A->C=11
        * B->C=2
        * Pero...¿Y si A->C puede ser más corta pasando por B?

        A->B->C = 4 + 2 = 6, que es mejor que 11
        Entonces, actualizamos A->C = 6

        Eso es excatamente lo que hace Floyd-Warshall automáticamente, pero para todos los pares de nodos y todos los posibles intermediarios.

    Concepto matemático
    Usamos una matriz dist de tamño n x n, donde dist[i][j] guarda la distancia más corta conocida de 'i' a 'j'

    Inicializamos:
        * Si existe arista i->j con peso w, entonces dist[i][j] = w
        * dist[i][i] = 0
        * Si no hay coneción directa, dist[i][j] = ∞

        Fórmula de actualización (CLAVE!!!!)
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            Es decir, "Si pasar por 'k' mejora el camino de 'i' a 'j', actualiza!
        Y se repite para todos los posibles 'k' (nodo intermedios)

    Pasos del algoritmo
        1. Inicializar la amtriz de distancias.
        2. Para cada nodo 'k' (intermedio posible)
        3. Para cada nodo 'i' (origen)
        4. Para cada nodo 'j' (destino)
            * Ver si pasar por 'k' mejora dist[i][j]
                5. Al final, dist[i][j] contiene la disntacia mínima entre 'i' y 'j'

    De      A       B       C
    A       0       4       11
    B       ∞       0       2
    C       ∞       ∞       0

    Iteramos k = A, B, C:
        * k = A: nada mejora (A no ayuda como intermedio todavía)
        * k = B:
            * A -> C mejora: dist[A][B] + dist[B][C] = 4 + 2 = 6 < 11 -> OK
            * Actualizamo A->C = 6
        * k = C: no mejora nada más

    De      A       B       C
    A       0       4       6
    B       ∞       0       2
    C       ∞       ∞       0 
"""

from math import inf

def floyd_warshall(grafo):
    """
    grafo: diccionario de diccionarios
    grafo[u][v] = peso de la arista u->v
    """
    # Paso 1: crear la lista de nodos
    nodos = list(grafo.keys())

    #Paso 2: Inicializar matriz de disntacias
    dist = {i: {j: inf for j in nodos} for i in nodos}
    for i in nodos:
        dist[i][i] = 0
        for j in grafo[i]:
            dist[i][j] = grafo[i][j]

    #Paso 3: algoritmo príncipal
    for k in nodos:                 # nodo interno
        for i in nodos:             # nodo origen
            for j in nodos:         # nodo destino
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

grafo = {
    "A": {"B": 3, "C": 8, "E": -4},
    "B": {"D": 1, "E": 7},
    "C": {"B":4},
    "D": {"A": 2, "C": -5},
    "E": {"D": 6}
}

dist = floyd_warshall(grafo)

print("Matriz de disntacias mínimas: ")
for i in dist:
    for j in dist[i]:
        print(f"{i} -> {j}: {dist[i][j]}")



"""
Tabla 1

De      A       B       C       D       E
A       0       3       8       ∞       -4
B       ∞       0       ∞       1       7
C       ∞       4       0       ∞       ∞       
D       2       ∞       -5      0       ∞
E       ∞       ∞       ∞       6       0

Tabla 2 k = B

De      A       B       C       D       E
A       0       3       8       4       -4
B       ∞       0       ∞       1       7
C       ∞       4       0       5       11       
D       2       ∞       -5      0       ∞
E       ∞       ∞       ∞       6       0
A -> D mejora : 4
A -> B -> D = 3 + 1 = 4 < ∞
C -> D
C -> B -> E = 4 + 7 = 11 < ∞

Tabla 3 k = C

De      A       B       C       D       E
A       0       3       8       4       -4
B       ∞       0       ∞       1       7
C       ∞       4       0       5       11       
D       2       ∞       -5      0       6   
E       ∞       ∞       ∞       6       0
D->C->B->E = (-5) + 4 + 7 = 6 < ∞
""" 