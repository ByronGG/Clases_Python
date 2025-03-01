"""
Listas anidadas son estructuras de datos que nos permiten almacenar listas dentro de otras listas. 
Son muy útiles para representar matrices, tablas, estructuras jerárquicas o datos multidimensionales.

Sintaxis de una lista anidadad:
    lista = [[1,2,3],[4,5,6],[7,8,9]] # Matriz 3x3
    lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]] # Matriz 4x3
    lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]] # Matriz 5x3

    Se utilizan bucles anidados para recorrer los elementos de una lista anidada.
    Copiar una lista anidada con el método copy() o con la función deepcopy() del módulo copy.
    Se pueden crear listas anidadas con listas por comprensión.

    append()    lista.append([5, 6])        Agrega una sublista al final
    extend()    lista.extend([7, 8])        Extiende la lista (no anidada)
    insert()    lista.inster(0, [0])        Insertar una sublista en la posición 0
    remove()    lista.remove([1, 2])        Elimina la primera sublista [1, 2]
    index()     lista.index([3, 4])         Devuelve el índice de la sublista
"""

# Ejemplo básico
lista_anidada = [[1,2,3], [4,5,6], [7,8,9]] # Una lista de lista o como matriz
print(lista_anidada)

print("--------------------------------------------------------------------------------------")

# Listas con direntes niveles anidación
mixta = [int(1), float(6.2), ["a", "b", 3, [10,20]], True, False, [3.14, 2.71, "Arturo"]]
print(mixta)

print("--------------------------------------------------------------------------------------")

# Acceder a elemtnos
matriz = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

print(matriz[0][0])
print(matriz[1][1])
print(matriz[1][2])
print(matriz[2][2])

lista_compleja = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(lista_compleja[1][0][1]) # Salida 6

print("--------------------------------------------------------------------------------------")

# Modificar elementos
matriz [1][1] = 500
print(matriz)

print("--------------------------------------------------------------------------------------")

# Itera sobre listas anidadas

for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ')
    print()

print("--------------------------------------------------------------------------------------")

# Usando list comprehensions

salida = [[10 + i * 30 + j * 10 for j in range(3)] for i in range(3)]
"""
Estrucutra de la lista de compresión
    - Bucle externo (for i in range(3)): Genera 3 sublistas
    - Bucle interno (for j in range(3)): Crear 3 elementos por sublista
    - Cálculo de valor (10 + i * 30 + j * 10):
        - i * 30: Define el inicio de cada sublista (10, 40, 70)
        - j * 10: Añade los incrementos de 10 dentro de cada sublista
"""
print(salida)

# Version alternativa
numeros = list(range(10, 100, 10)) # range(inicio, final(es excluido), paso)
lista_anidada_2 = [numeros[i : i + 3] for i in range(0, 9, 3)]
"""
    - range(0, 9, 3): genera los índice 0, 3, 6 [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    - numeros[i:i+3]: toma los elementos desde el índice 'i' hasta 'i+3'
"""
print(lista_anidada_2)

lista_anidada_3 = [[10 + i * 20 + j * 10 for j in range(2)] for i in range(4)]
print(lista_anidada_3)

print("--------------------------------------------------------------------------------------")

# Ejemplo práctico: Calificaciones de estudiantes

estudiantes = [
    ["Arturo", [40,60,30]], # ["Arutor", [40,60,30]]
    ["Luis", [10, 90, 50]], 
    ["Reyna", [80,70,65]],
    ["Pepe", [0, 0, 0]]
]

# Calcular el promedio por estudiante
for estudiante in estudiantes:
    nombre = estudiante[0]
    calificaciones = estudiante[1]
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"{nombre}: {promedio:.2f}")


# En consola quiero que se muentre como:
# Arturo: 43.33
# Luis: 50.00
# Reyna 71.66
# Pepe: 0

print("--------------------------------------------------------------------------------------")

"""
Crea una lista anidada que represente un tablero de ajedrez (8x8), donde:

"♜" representa una torre negra en la posición (0,0).

"♖" representa una torre blanca en la posición (7,7).

Los demás elementos son cadenas vacías "".
"""

# Crear un table de ajedrez 8x8 lleno de cadenas vacías "" CON LISTA DE COMPRESIÓN (1 linea de código)
tablero = [["" for _ in range(8)]for _ in range(8)]
"""
    1. Creacióin de table vació:
        - Usamos una lista de comprensión anidada para crear una matriz de 8x8
        - ["" for _ in range(8)]: crea una fila de 8 elementos vaciós ""
        - for _ in range(8): repite este proceso para crear 8 filas más
"""


# Colocar las torres en sus posiciones (2 lineas de código)
tablero[0][0] = "♜"
tablero[7][7] = "♖"
"""
    2. Colocanción de torres
        - tablero[0][0] = "♜" : coloca la torre en la primera fila [0] y primera columna [0]
        - tablero[7][7] = "♖" : coloca la torre en la última final [7] y última columna [7]
"""

# Mostrar el tablero (2 lineas de código)
for fila in tablero:
    print(fila)

"""
["♜","","","","","","",""],
["","","","","","","",""],
["","","","","","","",""],
["","","","","","","",""],
["","","","","","","",""],
["","","","","","","",""],
["","","","","","","",""],
["","","","","","","","♖"]
"""

# El guion bajo '_' en Python se usa como variable anónima o placehoilder, y si significado en ese línea es:
# "NO ME INTERESA EL VALOR DE LA VATRIALBE DE ITERACION, SOLO NECESITO QUE EL BUCLE SE EJECUTE UN NÚMEROS DE VECES"

nombre, _, edad = ["Ana", "corre@ejemplo.com", 20] # Ignora el correo


print("--------------------------------------------------------------------------------------")

lista = [[1,2], [3,4,5]]
print(len(lista)) # Salida: 2 (elementos en el nivel superior de la lista)

total = sum(num for sublista in lista for num in sublista)
print(total)

doble = list(map(lambda x : [num * 2 for num in x], lista))
print(doble)

print("--------------------------------------------------------------------------------------")

# Aplnar una lista anidada
lista = [[1,2], [3,4]]
print(f"Lsita antes de ser aplanada: {lista}")
aplanda = [num for sublista in lista for num in sublista]
print(f"Lsita despues de ser aplanda {aplanda}")

# Filtrar una lista anidada
pares = [[num for num in sublista if num % 2 == 0] for sublista in lista]
print(f"Lista filtrada por pares {pares}")

print("--------------------------------------------------------------------------------------")
