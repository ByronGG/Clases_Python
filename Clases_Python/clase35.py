# DSU Union-Find

"""
    DSU es una estructura de datos que sirve para agrupar elementos en conjuntos disjuntos y saber si dos elementos pertencen al mismo conjuto.

    Su objeto es poder responder muy rápido a dos operaciones:
        1. Find(x) -> "¿a qué grupo pertenece el elemento x?"
        2. Union(x, y) -> "Une el grupo de x con el grupo de y."

    Imagina que tienes estudiantes en una universidad y vas creando grupos de amigos.
        * Al principio cada estudiante está solo (su propio grupo)
        * Si dos estudiantes se hacen amigos -> fusionas sus grupos (Union)
        * Si quieres saber si dos personas están en el mismo grupo -> preguntas a quién pertenece cada uno (Find)
    Esto lo mismo hacen las computadoras, pero con nodo y conjutos

    Concepto
    Imaga una lista parent[] donde:
        * parent[i] = índice del "padre" del nodo i
        * si parent[i] == i, entonces i es el "líder" de un conjuto
    Ejemplo incial (5 nodos):

    parent = [0,1,2,3,4]
    Cada quien es su prodio líder.
    ---------------------------------------------------------------------------------
    Operación Find(x)
    Buscar líder raíz del conjuto al que pertenece x:

    Ejemplo
    Find(3) -> devuelve el líder del grupo que contiene 3
    Si 3 está conectado 2, y 2 está conecta a 0, el líder es ?
    3 -> 2 -> 0 -> 0
    ---------------------------------------------------------------------------------
    Operación Union(x, y)
    Une los grupos de x y y.
    Pasos:
        1. Encuntra los líderes de ambos
        2. Si son distintos -> uno se vuelve padre del otro.

    Ejemplo: Union(2, 4)
    Si el líder de 2 es 0, y el de 4 es 4 ahora 4 se une a 0:
    parent[4] = 0
    así ambos están en el mismo conjutos.
    ---------------------------------------------------------------------------------

    Optimizaciones (para que sea rápido)
    DSU tien dos optimizaciones:

    1. Path Compression (compresión de camino)
        Cada vez que hacemon find(x), acortamos el camino al líder.
        Así la proxima vez que busquemos el mismo nodo, será directo
        Ejemplo
        3 -> 2 -> 0
        Despues find(3) con compresión:
        3 -> 0
        Esto mejor el tiempo de consultas a casi O(1)

    2. Union by Rank (unión por rango)
        Cuando unimos dos conjutos, el más pequeño se cuelga del más grande.
        Así mantenemos los árbol planos y búsquedas son más rápidas.

        Ejmplo práctico paso a paso
        Quiere conectar estos pares:
        Paso 1 => (0,1), (1,2), (3,4)
        Paso 2 => parent = [0,1,2,3,4]
                  Union(0,1) -> parent=[0,0,2,3,4]
        Paso 3 => Union(1,2): -> Find(1) = 0, Find(2) = 2 -> unir líderes -> parent[2] = 0
                  parent = [0,0,0,3,4]
        Paso 4 => Union(3,4):
                  parent = [0,0,0,3,3]
        Ahora hay dos conjutos:
        Grupo 1 = {0,1,2}
        Grupo 2 = {3,4}


"""

class DSU:
    def __init__(self, n):
        # Cada nodo empieza siendo su propio padre
        self.parent = list(range(n))
        # Rank (o altura aproxima) inicia de cada árbol desde 0
        self.rank = [0] * n

    def find(self, x):
        # Encuentra el represtante (líder) del conjunto de x
        if self.parent[x] != x:
            # Path compression: conecta x directamente con el líder
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        # Une los conjutos que contiene a y b
        ra = self.find(a)
        rb = self.find(b)

        # Si ya tienen el mismo representante, y están unicos
        if ra == rb:
            return False # no hubo unión nueva
        
        # Union by rank: el árbol más bajo se cuelga del más alto
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[rb] < self.rank[ra]:
            self.parent[rb] = ra
        else:
            # Si tiene el mismo rank, elegimos uno como padre
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True #sí se union
    
"""
i:         0    1   2   3   4
parent    [0,   1,  2,  3,  4]
rank      [0,   0,  0,  0,  0]

Cada nodo está solo, su propio conjunto:
{0}, {1}, {2}, {3}, {4}

Idea
    * Queremos encontrar el repsentante / líder del conjutos al que pertenece x.
    * Si parent[x] == x, x es líder.
    * Si no, seguimos subiendo: parent[parent[x]], etc.

    Sin path compressión (idea básica)
    Imagina que por varias unions terminamos así:
    0 -> 0
    1 -> 0
    2 -> 1
    3 -> 2
    4 -> 4
    Árbol (visto vertical)

    0
    |_1
      2
      |_3
        |_4

    find(4)
        * parent[4] = 3 -> no es líder -> sube a 3
        * parent[3] = 2 -> subes a 2
        * parent[2] = 1 -> subes a 1
        * parent[1] = 0 -> subes a 0
        * parent[0] = 0 -> líder encontrado

    Con path compression
    Antes:
        parent = [0,0,1,2,3]
    Después el find(4):
        parent = [0,0,0,0,0]

    Árbol
    0
    |-1
    |-2
    |-3
    |-4
    Ahora todos aputan directo al líner -> las proximas búsquedas son O(1) casi siempre.

    ¿Por qué usamos rank?
    rank intenta representar la "altura" del árbol
    La regla union by rank dice:
        * el árbol más bajo se cuelga del árbol más alto
        * así envitamos generar árboles con muchas alturas -> find se mantien rápido

    Ejemplo de diagrams
    Supon que tenemos:
    
    Conjuton 1:
    ra = 0
    rank[0] = 2

    Conjunto 2:
    rb = 3
    rank[3] = 1

    parent:
    0 -> 0
    1 -> 0
    2 -> 0
    3 -> 3
    4 -> 3

    Visualmente

    0              3
    /\            /
   1  2          4
  rank = 2    rank = 1

  Hacemos union(1, 4):
  find(1) = 0 -> ra = 0
  find(4) = 3 -> rb = 3
  rank[0](2) > rank[3](1) -> el líder se cuelga de 0:

  self.parent[rb] = ra

    Nuevo estado
    parent

    0 -> 0
    1 -> 0
    2 -> 0
    3 -> 3
    4 -> 3

    rank:
    0: 2
    3: 1
    4: 0
    1: 0
    2: 0

    Union de rb -> ra
         0
        /|\
       1 2 3
            \
             4

    Si los dos árboles tiene la misma altura, da igual cuál va arriba, PERO ahora el nuevo árbol resultante tendrá una altura 1 unidad mayor, por eso se hace rank[ra] +=1
    Ejemplo

    ra = 0, rank[0] = 1
    rb = 3, rank[3] = 1

    0           3
    |           |
    1           4

    Luego del union

    0
    |\
    1 3
       \
        4
    rank[0] = 2
"""
