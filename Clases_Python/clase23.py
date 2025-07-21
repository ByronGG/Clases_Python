# Árboles Binario valor Máximo y Mínimo
"""
      8
     / \
    3   10
   / \    \
  1   6    14
     / \   /
    4   7 13

    * Si el nodo es None, devuelve un inf para mínimo y -inf para máximo
    * Recorrer el subárbol izquiero y derecho
    * Comparar todos los valores y devolver el máximo o mínimo
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def encontrar_maximo(nodo):
    if nodo is None:
        return float('-inf')
    max_izq = encontrar_maximo(nodo.izquierda)
    max_der = encontrar_maximo(nodo.derecha)
    return max(nodo.valor, max_izq, max_der)

def encontrar_minimo(nodo):
    if nodo is None:
        return float('inf')
    max_izq = encontrar_minimo(nodo.izquierda)
    max_der = encontrar_minimo(nodo.derecha)
    return min(nodo.valor, max_izq, max_der)

def encontrar_maximo_BST(nodo):
    actual = nodo
    while actual.derecha:
        actual = actual.derecha
    return actual.valor

def encontrar_minimo_BST(nodo):
    actual = nodo
    while actual.izquierda:
        actual = actual.izquierda
    return actual.valor


# Árbol de ejemplo
raiz = Nodo(8)
raiz.izquierda = Nodo(3)
raiz.derecha = Nodo(10)
raiz.izquierda.izquierda = Nodo(1)
raiz.izquierda.derecha = Nodo(6)
raiz.izquierda.derecha.izquierda = Nodo(6)
raiz.izquierda.derecha.derecha = Nodo(6)
raiz.derecha.derecha = Nodo(14)
raiz.derecha.derecha.izquierda = Nodo(13)

print("Valor máximo: ", encontrar_maximo(raiz)) # Resultado => 14
print("Valor mínimo: ", encontrar_minimo(raiz)) # Resultado => 1

print("----------------------------------------------------------------------------------------")

# Encontrar el nivel más produnfo (o la altura) de un árbol binario
"""
    Dado un árbol binario, implementa una función que deveulva su profundidad máxima, es decir el número de niveles desde la raiz hasta la hoja más lejana
       1
      / \
     2   3
    /
   4
    * El nivel más profundo es 3 (camino: 1 -> 2 -> 4)

    1. Si el nodo es None, devuelve 0 (caso base)
    2. Calcula la profundidad máxima del subárbol izquiero
    3. Calcula la profundidad máxima del subárbol derecho
    4. Devuelve el mayor de los dos + 1 (por el nodo actual)
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def profundidad_maxima(nodo):
    if nodo is None:
        return 0
    profundidad_izq = profundidad_maxima(nodo.izquierda)
    profundidad_der = profundidad_maxima(nodo.derecha)
    return max(profundidad_izq, profundidad_der) + 1

raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)

print("Nivel más produndo: ",profundidad_maxima(raiz)) # Resultado => 3

print("----------------------------------------------------------------------------------------")

# Sumar los nodos del nivel más produnfo de un árbol binario
"""
    Dado un árbol binario, escribe una función que sume todos los nodos que están en el nivel más produndo del árbol

        1
       / \
      2   3
     /     \
    4       5
           / \
          6   7
    
    * El nivem más profundo es el nivel 7 (nodos 6 y 7)
    Resultado esperado: 6 + 7 = 13 

    Usamos el recorrido por niveles (BFS) con una cola:
    1. Recorrermos el árbol nivel por nivel
    2. En cada nivel, almacenamos temporalmente los valores de los nodos.
    3. Al final, los útlimos valores almacenados son del nivel más profundo.
    4. Sumamos esos valores y los devolvemos.
"""
from collections import deque

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def suma_nivel_mas_profundo(raiz):
    if not raiz:
        return 0
    
    cola = deque([raiz])
    suma = 0

    while cola:
        nivel_size = len(cola)
        suma = 0 # Resetear suma en cada nivel

        for _ in range(nivel_size):
            nodo = cola.popleft()
            suma += nodo.valor
            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)

    return suma # Suma del último nivel procesado

# Árbol
"""
        1
       / \
      2   3
     /     \
    4       5
           / \
          6   7

"""
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.derecho.derecho = Nodo(5)
raiz.derecho.derecho.izquierdo = Nodo(6)
raiz.derecho.derecho.derecho = Nodo(7)

print("Suma del nivel más profundo: ", suma_nivel_mas_profundo(raiz))