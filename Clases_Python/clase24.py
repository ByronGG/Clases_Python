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
