"""
    El reoccirdo inorden visita los nodos en el siguiente orden:
        1. Reccore el subárbol izquierdo en inorden
        2. Visita la raiz
        3. Recorre el subárbol derecho en inorden

        Izquierda -> Raiz -> Derecha

     A
    / \
   B   C
  / \
 D   E

1. Comienza en A, va a la izquierda -> B
2. En B, ve a la izquierda -> D (no tiene hijos) y visita -> D
3. Regresamos a B -> Visita B
4. Ve a la deracha de B -> E (no tiene hijos) y visita -> E
5. Regremos a A -> visitamos A
6. Ve a la derecha -> C visitamos C
Resultado Final : D, B, E, A, C
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def inorden(nodo):
    if nodo:
        inorden(nodo.izquierda) 
        print(nodo.valor, end=' ')
        inorden(nodo.derecha)

raiz = Nodo('A')
raiz.izquierda = Nodo('B')
raiz.derecha = Nodo('C')
raiz.izquierda.izquierda = Nodo('D')
raiz.izquierda.derecha = Nodo('E')

print("Recorrido inorden: ")
inorden(raiz)


"""
    El recorrido postorden visita los nodos en este orden:
        1. Recorre el subarbol izquierdo en postorden
        2. Recorre el subarbol derecho en postorden
        3. Visita la raiz (nodo actual)

        Izquierda -> Derecha -> Raiz

     A
    / \
   B   C
  / \
 D   E

1. Comienza en A, ve a izquierda -> B
2. En B, ve a la izquierda -> D (no tiene hijos) -> visita D
3. Regreso a B, ve a la derecha -> E (no tiene hijos) -> visita E
4. Regresamos a B -> visitamos B
5. Regresa A, ve a la derecha -> C (no tiene hijos) -> visita C
6. Regresa a A -> visita A
Resultado Final: D, E, B, C, A
"""

class Nodo_Postorden:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def postorden(nodo):
    if nodo:
        postorden(nodo.izquierda) 
        postorden(nodo.derecha)
        print(nodo.valor, end=' ')

raiz = Nodo_Postorden('A')
raiz.izquierda = Nodo_Postorden('B')
raiz.derecha = Nodo_Postorden('C')
raiz.izquierda.izquierda = Nodo_Postorden('D')
raiz.izquierda.derecha = Nodo_Postorden('E')

print("\nRecorrido postorden: ")
postorden(raiz)

"""
      M
     / \
    L   Q
   /   / \
  A   N   R

Preorden: M->L->A->Q->N->R
Inorden: A->L->M->N->Q->R
Postorden: A->L->N->R->Q->M
"""
"""
       F
      / \
     B   G
    / \   \
   A   D   I
      / \  /
     C  E H

Inorden: A->B->C->D->E->F->G->H->I
Postorden: A->C->E->D->B->H->I->G->F
Preorden: F->B->A->D->C->E->G->I->H
"""

"""
TAREA PARA MAÑANA

Preorden: E, B, A, D, C, F, G
Inorden: A, B, C, D, E, F, G
"""