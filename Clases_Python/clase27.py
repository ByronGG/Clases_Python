# Árboles Sufijos

"""
    Un árbol de sufijos es una estructura de datos en forma de árbol de prefijos comprimido que contiene todos los sufijos de una cadena de texto dada.

    Sufijos:
    Sustancia$
    ustancia$
    stancia$
    tancia$
    ancia$
    ncia$
    cia$
    ia$
    a$
    $

    Trie
        * Guarda todos los prefijos (cada carácter ocupa un nodo)
        * Un árbol de sufijos pero comprienido ramas comunes en "aristas" con subadenas

    1. Insertar: Casa Casco Castillo Casquillo Cascada Casino

    (root)
    |__c
        |__a
            |__s
                |__a*
                |__c
                    |__o

    Busqueda de patrones en tiempo lineal O(m) -> Donde m es la longitud de patrón
    Algoritmos de compresión existen gzip y bzip2
    Aplicaciónes bioinformática (comparar secuencias ADN/ARN)
    
    Diferencias
        * Trie guardar TODOS los prefijos (cada carácter ocupa un nodo)
        * Árbol de sufijos guarda todos los subjos pero compriemiendo ramas comunes en aristas con subcadenas

"""

class SuffixTreeNode:
    def __init__(self):
       self.children = {} # Diccionario de hijos {char: nodo}
       self.indexes = [] # Guarda los índices de los sufijos que pasan por aquí

class SuffixTree:
    def __init__(self, text):
        self.root = SuffixTreeNode()
        self.text = text # Sustancia
        self._build_suffix_tree()

    def _build_suffix_tree(self):
        """Construye el árbol insetando todos los sufijos"""
        for i in range(len(self.text)): # HOLA -> len(4) = i -> H -> O -> L -> A
            suffix = self.text[i:] # [inicio:fin:paso]
            self._insert_suffix(suffix, i)

    def _insert_suffix(self, suffix, index):
        """Inserta un sufijo en el árbol"""
        node = self.root
        for char in suffix: # suffix => "Arturo" -> char => "A" => "r"... n
            if char not in node.children:
                node.children[char] = SuffixTreeNode()
            node = node.children[char]
            node.indexes.append(index)

    def search(self, pattern):
        """Buscar un pátron en el texto original"""
        node = self.root
        for char in pattern:
            if char not in node.children:
                return [] # No encontrado
            node = node.children[char]
        return node.indexes
    
# Reyna => R e y n a => input = Z => [] != index

tree = SuffixTree("cloro")

print(tree.search("ro")) # -> [3 y 4]
print(tree.search("clo")) # -> [0, 1, 2]
print(tree.search("r")) # -> [3]
print(tree.search("a")) # -> []

"""
    Esta implemantación es: O(n^2) es contruir el árbol porque inserta sufijo por sufijo.
    Existen algoritmos como Ukkonen logra hacerlo O(n) en forma más elegante.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False # Marcar si es el final de una palabra

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word: # Word = Juanita
            if char not in node.children: 
                node.children[char] = TrieNode() # Node = J
            node = node.children[char] # Children -> Node -> a
        node.is_end = True # Flag False => True

    def _dfs(self, node, prefix, results):
        """Recorre en profundidad para encontrar todas las palabras a partir de un prefijo"""
        if node.is_end:
            results.append(prefix)
        for char, child in node.children.items():
            self._dfs(child, prefix + char, results)

    def autocomplete(self, prefix):
        """Devuelve lista de autocompletado para un prefijo dado."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return [] # Prefijo no encontrado
            node = node.children[char]

        results = []
        self._dfs(node, prefix, results)
        return results
    

# DEMO TIEMPO REAL
if __name__ == "__main__":
    
    palabras = ["reyna", "luis", "arturo", "saltillo", "mexico", "mesa", "luz", "reno", "reynosa", "argentino", "arbitro", "merenge", "hola", "hermano", "hombre", "histeria", "himno", "nena", "naranja", "nevada"]

    trie = Trie()
    for palabra in palabras:
        trie.insert(palabra)

    print("== Autocompletado en tiempo real ==")
    print("Escribe letra por letra (enter para salir)\n")

    prefijo = ""

    while True:
        letra = input("Escribe siguiente letra: ")
        if letra == "":
            break
        prefijo += letra
        sujerencias = trie.autocomplete(prefijo)
        if sujerencias:
            print(f"Sugerencias para '{prefijo}': {sujerencias}: ")
        else:
            print(f"No hay sugerencias para '{prefijo}': ")


"""
    Ejercicio: Sistema de Autocompletado con Prioridad por Popularidad Objetivo:

    Construir un autocompletador de palabras en Python usando un Trie, pero con la mejora de ordenar las sugerencias por popularidad (imitando cómo lo hace Google).

        Parte 1: Construcción del Trie
            1. Implementa una clase TrieNode con:
                Un diccionario de children.
                Un booleano is_end.
                Un contador frequency que indique cuántas veces se ha buscado esa palabra.
            2. Implementa la clase Trie con métodos:
                insert(word) → inserta una palabra.
                search(word) → retorna True/False.
                autocomplete(prefix) → retorna las sugerencias, ordenadas por frecuencia.

        Parte 2: Simulación de uso
            Inserta un diccionario inicial de palabras.
            Cada vez que un usuario elija una palabra de las sugerencias, incrementa la frecuencia de esa palabra.
            Muestra cómo con el tiempo las más buscadas suben en el ranking.
"""

