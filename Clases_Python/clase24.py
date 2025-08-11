# Árboles Espejo
"""
Árbol Original
     1
    / \
   2   3
  / \
 4   5

Árbol Espejo (Respuesta Esperada)
     1
    / \
   3   2
       / \
      5   4

    Un árbol espero es aquel donde se interbian los hijos izquierdos y derechos de todos los nodos del árbol

    DFS recursivo
    1. Si el nodo esta vacío -> no hacer nada
    2. Intercambiar los hijos izquierda con derecha
    3. Aplicar la misma función recursivamente al hijo izqeuirdo y derecho
"""

# Solución Tarea
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def invertir_arbol(nodo):
    if nodo is None:
        return
    # Intercambiar los hijos izquierdo y derecho
    nodo.izquierda, nodo.derecha = nodo.derecha, nodo.izquierda
    # Aplicar recursivamente a los hijos
    invertir_arbol(nodo.izquierda)
    invertir_arbol(nodo.derecha)

def preorden(nodo):
    if nodo is None:
        return
    print(nodo.valor, end=' ')
    preorden(nodo.izquierda)
    preorden(nodo.derecha)

# Ejemplo de uso
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)

print("Árbol original: ")
preorden(raiz)  # Resultado esperado: 1 2 4 5 3

# Invertir el árbol
print("\nInvirtiendo el árbol...")
invertir_arbol(raiz)

print("Árbol invertido en preorden:")
preorden(raiz)  # Resultado esperado: 1 3 2 5 4