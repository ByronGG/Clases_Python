# Árbol binario
"""
    Un árbol binario es una estrucutra de datos jerárquica compuesta por nodos, donde:
        * Cada nodo tiene como máximo dos hijos: uno a la izquirda (hijo izq) y otro a la derecha (hijo der)
        * se utilizan mucho en programación por su eficiencia de búsqueda, ordenamiento y represnatción de datos jerárquicos.

     Raiz: Es el primer nodo del árbol, desde donde comienza toda la estructura. 10
     Nodo: Cada elemento del árbol es un nodo: Tiene * Valor o dato * Un puntero/referencia a su hijo izq / der
     Hijo (child): Son nodos que deciendess de otro nodo [5, 10]
     Padre: Es el nodo que tiene uno o más hijos [10] es padre de [5, 10]
     Hoja (leaf):  Son los nodos que no tiene hijos, es decir, están al final de la rama [12]

     ¿Para qué se usan los árboles binarios?
        * Estrucutras jerárquicas, como carpetas y archivos
        * Árboles de búsqueda binaria (BTS), donde los valores menores están a la izquierda y mayores a la derecha, para búsqueda y ordenamiento eficientes
        * Expresiones matemáticas (árboles de expresión) para calcular resultados.
        * Implementación de algoritmos como árboles de decisión en IA
        * Compiladores, para analizar y traducir código fuente

    8
   / \
  3   10
 / \    \
1   6    14
   / \   /
  4   7 13

"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.insertar_recursivo(self.raiz, valor)

    def insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self.insertar_recursivo(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self.insertar_recursivo(nodo_actual.derecha, valor)
        else:
            print("El valor ya existe en el árbol")

    def buscar(self, valor):
        return self.buscar_recursivo(self.raiz, valor)

    def buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self.buscar_recursivo(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            return self.buscar_recursivo(nodo_actual.derecha, valor)
        
# Ejemplo de uso:
arbol = ArbolBinarioBusqueda()
arbol.insertar(8)
arbol.insertar(3)
arbol.insertar(10)
arbol.insertar(1)
arbol.insertar(6)
arbol.insertar(14)
arbol.insertar(4)
arbol.insertar(7)
arbol.insertar(13)

print(arbol.buscar(13))


"""
    8
   / \
  3   10
 / \    \
1   6    14
   / \   /
  4   7 13
"""

"""
    Qué es un recorrido en preorden?
    El recorrido en preorden (Preorden Traversal) visita los nodos en el siguiente orden:
        1. Visita la raiz (nodo_actual)
        2. Recorre el subárbol izquirda en preorden
        3. Recorre el subparbol derecha en preorden

        Raíz -> Izquierda -> Derecha

     A
    / \
   B   C
  / \
 D   E

 Resultado final: A, B, D, E, C
"""

class Nodo_Preorden:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def preorden(nodo):
    if nodo:
        print(nodo.valor, end=' ')  #1. Visita raíz
        preorden(nodo.izquierda)    #2. Recorre Izq
        preorden(nodo.derecha)      #3. Recorre Der

#Ejemplo de uso:
raiz = Nodo_Preorden('A')
raiz.izquierda = Nodo_Preorden('B')
raiz.derecha = Nodo_Preorden('C')
raiz.izquierda.izquierda = Nodo_Preorden('D')
raiz.izquierda.derecha = Nodo_Preorden('E')

print("Recorrido preorden")
preorden(raiz) 