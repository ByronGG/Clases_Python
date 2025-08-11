# Árboles Balanceados
"""
    Un árbol binario balanceado es aquel en el que la altura de los subárboles izquierdo y derecho de cualquier nodo difiere como máximo en uno.
    Para cada nodo del árbol:
        * absoluta(altura(subárbol izquierdo) - altura(subárbol derecho)) <= 1

    ¿Para qué sirve balancear un árbol?
    * Mejora la eficiencia de las operaciones de búsqueda, inserción y eliminación.
    * Evita que el árbol se convierta en una lista enlazada, lo que degradaría el rendimiento de las operaciones.
    * Si no está balanceado, las operaciones pueden tener un tiempo de ejecución O(n) en el peor caso, mientras que en un árbol balanceado, el tiempo de ejecución es O(log n).

    Ejemplo de árbol balanceado:
    4
   / \
  2   6
 / \ / \
1  3 5  7

    * Altura de subárboles = igual o con diferencia de 1
    
    Ejemplo de árbol no balanceado:
    1
     \
      2
       \
        3
         \
          4
    
    * Todos los nodos están solo a la derecha -> es una lista -> muy lento para buscar, insertar o eliminar
    * Altura de subárboles = diferencia mayor a 1

    ¿Cómo saber si un árbol está balanceado?
    Recursivamente:
    1. Recorres todo el árbol
    2. Calculas la altura de cada subárbol
    3. Verificas si la diferencia de alturas es mayor a 1 en algún nodo
    4. Si es así, el árbol no está balanceado; si no, sí lo está.

    -------------------------------------------------------------------------------------------------------------------------------------------------------
    Conclusión:
    * Ventaja de balancear un árbol: Operaciones rápidas y eficientes O(log n). Menor uso de memoria que estructuras como listas enlazadas. Ideal para busquedas, inserciones y eliminaciones frecuentes.
    * Desventaja de no balancear un árbol: Operaciones lentas O(n) en el peor caso. Puede convertirse en una lista enlazada, lo que afecta negativamente el rendimiento.
"""

# abs(altura(izq) - altura(der)) <= 1

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def esta_balanceado(nodo):
    def altura_y_balance(n):
        if not n:
            return (0, True) # Variable Aux / Flags
        
        altura_izq, izq_balance = altura_y_balance(n.izquierdo)
        altura_der, der_balance = altura_y_balance(n.derecho)

        altura = max(altura_izq, altura_der) + 1
        balanceado = izq_balance and der_balance and abs(altura_izq - altura_der) <= 1

        # Impresión del estado nodo
        print(f"Nodo: {n.valor}")
        print(f" - Altura izquierda {altura_izq}, balanceado {izq_balance}")
        print(f" - Altura derecha {altura_der}, balanceado {der_balance}")
        print(f" - Altura actual: {altura}")
        print(f" - Balanceo: {balanceado}\n")

        return (altura, balanceado)

    _, balanceado = altura_y_balance(nodo)
    return balanceado

"""
     1
    / \
   2   3
  / \
  4  5
 /
6
"""
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derehco = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)
raiz.izquierdo.izquierdo.izquierdo = Nodo(6)

resultado = esta_balanceado(raiz)
print(f"Árbol balanceado {resultado}")


