#Dijiktra

"""
    El algoritmo de Dijkstra sirve para encontrar el camino más corto desde un nodo origen hasta todos los demás nodos de un grado ponderado (con pesos positivos).

    Diklstra explora los caminos más baratos primero, actualizando las distancias mínimas conforme avanza.

    Pasos al algoritmo:
        1. Inicialización:
            * Marca la distancia del nodo origen como 0
            * Marca todos los demás nodos con una distancia infinita (∞)
        2. Visita el nodo más cercano (el que tenga la distancia miníma conocida).
        3. Actualiza las distancias de los vecinos del nodo actual.
            * Si la nueva distancia calculada es menor que la enterior, actualizada.
        4. Marcar el nodo como visitado (ya se conoce su distancia mínima).
        5. Repetir los pasos 2 a 4 hasta visitar todos los nodos o alcanzar el destino.

    Supón que estás en la cuidad A y quieres llegar a la cuidad D.

    Tienes este Mapa:
    Camino                  Distancia
    A -> B                     5 Km
    A -> C                     2 Km
    B -> D                     4 Km
    C -> D                     7 Km
    C -> B                     1 Km

    Dijktra irá encontrado el camino más corto:
        * De A a C cuesta 2Km
        * De C a B cuesta 1km (Total 3Km)
        * De B a D cuesta 4Km (Total 7km)
        Por lo tanto, el camino más corto es de A -> C -> B -> D = 7km

    FAQ
    ¿Puedo usar Dijkstra con peso negativos?
    No. Si hya pesos negativos, Dijkstra no garantiza el resultado correcto. En esos casos se usa el algoritmo Bellman-Ford

    ¿Dikstra encuentra solo el camino más corto a un nodo o a todos?
    Encuentra la distancia más corta desde el nodo origen hacia TODOS los demás nodos.

    ¿Se puede usar en grafos dirifidos?
    Sí, Dijktra funcia tanto como grafos dirigidos como no dirigidos (-> | ---)

    ¿Es eficiente?
    Sí, especialmente cuando se usa con una cola de prioridad (heap) su complejidad puede llagar aser O((V+E)log V), donde:
    V = número de vértices
    E = número de aristas
"""

#Usaremos una lista de adyacencia: un dict donde cada node tiene una lista de (vecinos, peso)

from heapq import heappush, heappop
from math import inf

def agregar_arista(grafo, u, v, peso, dirigido=False):
    """Agregar una arista (u -> v) con 'peso'
    Si el grado no es dirifido, también agrega (v -> u)."""
    if peso < 0:
        raise ValueError("Dijkstra no admite pesos negativos.")
    grafo.setdefault(u, []).append((v, peso))
    if not dirigido:
        grafo.setdefault(v, []).append((u, peso))
    else:
        grafo.setdefault(v, []) # asegurar de que el nodo exista aun que no tenga salientes

"""
    algoritmo de Dijkstra
    * Mantien dist[nodo] = mejor distancia conocida desde origen
    * Usar una cola de prioridad (min-heap) para siempre expandir el nodo con menor costo actual
    * previo[nodo] guarda el predecesor para reconstruir el camino óptimo
"""

def dijkstra(grafo, origen):
    """Calcula la distnai mímima desde 'origen' a todos los nodos usando dijstra
    
    Retorna:
    dist -> dict:nodo -> distancia mínima
    previo -> dict:nodo -> predecor en el camino
    """
    # 1) Inicialización
    dist = {n: inf for n in grafo}
    dist[origen] = 0
    previo = {n: None for n in grafo}

    # Min-heap de (distancia acumulado, nodo)
    heap = [(0, origen)]

    #2) Bucle principal
    while heap:
        d_actual, u = heappop(heap)

        #(Opcional/Optimización) Si el elemento del heap está desactualizado, lo saltamos
        if d_actual > dist[u]:
            continue

        # 3) Arista (u->v)
        for v, peso in grafo[u]:
            nueva = d_actual + peso
            if nueva < dist[v]:
                dist[v] = nueva
                previo[v] = u
                heappush(heap, (nueva, v))

    return dist, previo

def reconstruir_camino(previo, origen, destino):
    """Recostrue el camino optimo desde 'orifen' hasta 'destino' usando el dict 'previo'"""
    if destino not in previo:
        return None # destino desconocido
    
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        if actual == origen:
            break
        actual = previo[actual]
    camino.reverse()
    # si el origen no aparece, no hay ruta
    return camino if camino and camino[0] == origen else None

"""
Tienes este Mapa:
    Camino                  Distancia
    A -> B                     5 Km
    A -> C                     2 Km
    B -> D                     4 Km
    C -> D                     7 Km
    C -> B                     1 Km

    Dijktra irá encontrado el camino más corto:
        * De A a C cuesta 2Km
        * De C a B cuesta 1km (Total 3Km)
        * De B a D cuesta 4Km (Total 7km)
        Por lo tanto, el camino más corto es de A -> C -> B -> D = 7km
"""

grafo = {}
agregar_arista(grafo, "A", "B", 5, dirigido=False)
agregar_arista(grafo, "A", "C", 2, dirigido=False)
agregar_arista(grafo, "B", "D", 4, dirigido=False)
agregar_arista(grafo, "C", "D", 7, dirigido=False)
agregar_arista(grafo, "C", "B", 1, dirigido=False)

#Ejecutar Dijktra desde A
dist, previo = dijkstra(grafo, "A")

print("Distancia mínima desde A: ")
for nodo in sorted(dist):
    print(f" A -> {nodo}: {dist[nodo]}")

camino_AD = reconstruir_camino(previo,"A", "D")
print("\nCamino más corto de A a D:", " ->".join(camino_AD) if camino_AD else "No hay ruta")
print("Distancia total:", dist["D"])


print("---------------------------------------------------------------------------------")

class Grafo:
    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self.adj = {}

    def agrega(self, u, v, w):
        agregar_arista(self.adj, u, v, w, dirigido=self.dirigido)

    def dijkstra(self, origen):
        return dijkstra(self.adj, origen)

    def camino(self, origen, destino):
        _, previo = self.dijkstra(origen)
        return reconstruir_camino(previo, origen, destino)
