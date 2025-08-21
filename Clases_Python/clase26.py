"""
    Árbol B y B+
    Un Árbol es una generalización de un árbol binario  de busqueda (BTS), es que cada nodo tenga 2 hijo como máximo

    - Cada nodo puede tener múltiples cavles y múltiples hijos.
    - Se utilizan principalmente en alamacenamiento de disco (basde de datos, sistemas de archivos, etc.) porque reduce acessos a disco.

    Propiedad principales de un Árbol B en orden m:
    1. Cada nodo puede tener máximo m hijos
    2. Cada nodo (excepto raiz y hojas) tiene al menos [m/2] hijos
    3. Todas las hojas están al mismo nivel (es un árbol balanceado)
    4. Las claves dentro de un nodo están ordenadas
    5. Los hijos se dividen en rangos según esas claves.
    
    Ejemplo de un árbol B orden 3 (m=3):
          [10 | 20]
        /     |     \
   [5 | 7]  [12 | 15]  [22 | 30 | 35]

   El nodo raiz [10 | 20] tiene 2 claves -> divide 3 rangos:
        * Todo < 10
        * Entre 10 y 20
        * Todo > 20
"""

"""
    Árbol B+ es una variante del Árbol B que optimiza búsquedas y recorridos.
    
    1. Es un B+, todas las claves reales están en las hojas,
        * Los nodos internos solo sierver como "índices" de búsqueda.
    2. Las hojas están enlazadas como lista doble -> recorrido secuencial muy rapido
    3. Se usa muchisimo en base de datos (MySQL, PostgreSQL, Oracle, MondoDB, ect.) y sistemas de archivos (NTFS, ext4, HFS+, FAT32).

            [10 | 20 | 30]
        /      |      |      \
      ...     ...    ...     ...
  
Hojas: [5, 8] <-> [10, 12, 15] <-> [20, 22, 25] <-> [30, 32, 35]

    * Las hojas están enlzadas (<->) para faclitar búsquedas por rango (ej: dame todas las ID's entre 10 y 25)
    * Esto hace que los scans y rangos sean muy rápidos, mucho mejor que en el árbol B normal.

"""

"""
    Aplicaciones reales

    1. Base datos relacionales (SQL)
        * Los índices de las tablas se impemental en con árboles B+
        * Ejemplo: cuando haces SELECT * FROM usuarios WHERE edad BETWEEN 20 AND 30, el motor usa el B+
            para encontrar rápidamente ese rango.
    2. Sistema de archivos
        * NTFS (windows), ext4(Linux), HFS+ (macOS) -> usan B+ para directorios y metadatos
    3. Motores de búsqueda y diccionarios
        * Estructuras de índice invertido en motores como Elasticsearch también se apoyan en B/B+
"""

class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf    # True si es hoja, False si es interno
        self.keys = []      # Claves ordendas
        self.children = []  # Punteros a hijos (solo en nodos interno) (n = len(keys) + 1 hijos)
        self.next = None    # enlace entre hojas
        
class BPlusTree:
    def __init__(self, t=3): # t = orden
        # Máx. Claves por nodo: 2*t-1 (aqui es 5)
        # Min. Claves por nodo: (excepto la raíz): t - 1 (aqui es 2)
        self.root = BPlusTreeNode(leaf = True)
        self.t = t

    def search(self, node, key):
        if node.leaf:
            return key in node.keys
        for i, item in enumerate(node.keys):
            if key < item:
                return self.search(node.children[i], key)
        return self.search(node.children[-1], key)

    def intert(self, key):
        root = self.root
        if len(root.keys) == (2*self.t - 1):
            new_root = BPlusTreeNode()
            new_root.children.append(self.root)
            self.split_children(new_root, 0)
            self.root = new_root
        self._intert_non_full(self.root, key)

    def _intert_non_full(self, node, key):
        if node.leaf:
            node.keys.append(key)
            node.keys.sort()
        else:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2*self.t - 1):
                self.split_children(node, i)
                if key > node.keys[i]:
                    i +=1
            self._intert_non_full(node.children[i], key)

    def split_children(self, parent, i):
        t = self.t
        node = parent.children[i]
        new_node = BPlusTreeNode(leaf=node.leaf)
        parent.keys.insert(i, node.keys[t-1])
        parent.children.insert(i+1, new_node)

        new_node.keys = node.keys[t:]
        node.keys = node.keys[:t-1]

        if not node.leaf:
            new_node.children = node.children[t:]
            node.children = node.children[:t]

# -------------------------------------------
# Ejemplo de uso
tree = BPlusTree(t=3)
for num in [5, 10, 15, 20, 25, 30, 35]:
    tree.intert(num)

print(tree.search(tree.root, 20)) # True
print(tree.search(tree.root, 50)) # False
        
"""
Inserciones con t=3 y claves 5, 10, 15, 20, 25, 30, 35
1. Tras insertar 5, 10, 15, 20, 25, 30, 35, la raíz-hoja tiene 5 claves: [5, 10, 15, 20, 25, 30, 35] (llena)
2. Llega 30: instert detecta raíz llena y hace split_child:
    * sube 15 al nuevo root => root (interno queda con keys=[15])
    * hijo izquierdo (hoja): keys=[5,10]
    * hijo derecho (hoja): keys=[20,25]
    * (No se enlazando hojas, next sigue None)
3. Inserta 30 en la hoja derecha => [20, 25, 30]
4. Inserta 35 en la hoja deracha => [20, 25, 30, 35]
Árbol final:
    * Raiz (interna): keys=[15]
    hijo 0 (hoja): [5,10]
    hijo 1 (hoja): [20,25,30,35]

Search(20) -> True (está en hoja derecha)
Search(50) -> False.

"""

print("-----------------------------------------------------------------------------------------------------------")

# SELECT * FROM tabla WHERE id BETWEEN 10 AND 30

"""
    * Cada nodo tendra claves ordenadas
    * Las hojas estarán enlazadas como en un B+
    * Implementaciones:
        - instert(id, valor) -> como si fuera un registro en la tabla
        - buscar(id) -> búsquedad puntual (SELECT * WHERE id=...)
        - buscar_rango(inicio, fin) -> búsqueda por rango (BETWEEN ... AND ...)
"""

class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf    # True si es hoja, False si es interno
        self.keys = []      # Claves ordendas
        self.children = []  # Punteros a hijos (solo en nodos interno) (n = len(keys) + 1 hijos)
        self.next = None    # enlace entre hojas

class BPlusTree:
    def __init__(self, t=3): # t = orden
        # Máx. Claves por nodo: 2*t-1 (aqui es 5)
        # Min. Claves por nodo: (excepto la raíz): t - 1 (aqui es 2)
        self.root = BPlusTreeNode(leaf = True)
        self.t = t

    #-------------------------------------------------------
    # Insertar clave-valor (id, registro)
    def insert(self, key, value):
        root = self.root
        if len(root.keys) == (2*self.t - 1):
            new_root = BPlusTreeNode()
            new_root.children.append(self.root)
            self.split_children(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, (key, value))

    def _insert_non_full(self, node, pair):
        if node.leaf:
            node.keys.append(pair)
            node.keys.sort(key=lambda x: x[0])
        else:
            key = pair[0]
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i][0]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2*self.t - 1):
                self.split_children(node, i)
                if key > node.keys[i][0]:
                    i += 1
            self._insert_non_full(node.children[i], pair)

    def split_children(self, parent, i):
        t = self.t
        node = parent.children[i]
        new_node = BPlusTreeNode(leaf=node.leaf)

        mid = len(node.keys) // 2
        split_key = node.keys[mid][0]

        parent.keys.insert(i, (split_key, None))
        parent.children.insert(i+1, new_node)

        new_node.keys = node.keys[mid:]
        node.keys = node.keys[:mid]

        if not node.leaf:
            new_node.children = node.children[mid+1:]
            node.children = node.children[:mid+1]
        else:
            new_node.next = node.next
            node.next = new_node
    
    #------------------------------------------
    # Buscar un registro putal (Motor SQL)
    def search(self, node, key):
        if node.leaf:
            for k, v in node.keys:
                if k == key:
                    return v
            return None
        for i, (k, _) in enumerate(node.keys):
            if key < k:
                return self.search(node.children[i], key)
        return self.search(node.children[-1], key)
    
    #--------------------------------------------
    #Buscar un rango de registro
    def search_range(self, start, end):
        node = self.root
        #bajar hasta las hojas
        while not node.leaf:
            node = node.children[0]

        results = []
        while node:
            for k, v in node.keys:
                if start <= k <= end:
                    results.append((k,v))
                elif k > end:
                    return results
            node = node.next
        return results
    
#------------------------------------------------
#Ejmplo tabla de usuario
tree = BPlusTree(t=3)

usuarios = [
    (5, "Ana"), (10, "Luis"), (15, "Reyna"), (20, "Pepe"), (25, "Arturo"), (30, "Pedro"), (35, "Roberto")
]

for id_, nombre in usuarios:
    tree.insert(id_, {"id": id_, "nombre": nombre})

# Consulta puntual (como SELECT * FROM usuarios WHERE id=20)
print("Buscar id=20: ", tree.search(tree.root, 20))

# Consulta por rango (como SELECT * FROM usuarios WHERE id BETWEEN 10 AND 30)
print("Buscar ids 10 - 30: ", tree.search_range(10, 30))

# Segment Tree y Fenwick Tree (Binary Indexed Tree)

# Árbol de prefijos (Trie) -> Árbol de Toma de deciones (IA/Machine Learning)

