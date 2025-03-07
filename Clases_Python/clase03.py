# Cadenas de caracteres

str1 = "Bienvenido"
str2 = "Arturo"

# Concatenación
print(str1 + ", " + str2 + "!")

# Repetición SOLO PASA EN PYTHON
print(str2 * 10)

# Logintud
print(len(str1))
print("--------------------------------------------------------------------------------------")

# Slicing
#string[inicio:final:paso]
print(str1[2:6])
print(str2[:-1])
print("--------------------------------------------------------------------------------------")

# Busqueda
print("x" in str1)
print("A" in str2)

# Mayusculas y minusculas (por alguna razón en problemas ASCII)
print(str2.upper())
print(str2.lower())
print("luis alardin".title())
print("luis alardin".capitalize())

# Remplazar
print(str2.replace("r", "n"))

# Eliminar espacios
print(" hola mundo ".strip())

# Búsqueda al princio o final
print(str1.startswith("Luis"))
print(str2.endswith("s"))

# Búsqueda por indice
print(str2.find("Arturo"))

# Interpolación
print(f"{str1}, Como estas {str2}")

# Formato
print("Saludos, {}!".format(str2))

# Tranformación (Cast)
l1 = [str1, ", ", str2, "!"]
print(l1)
print("".join(l1))

str3 = "1"
print(str3)
print(type(str3))
str3 = int(str3)
print(str3)
print(type(str3))

# Comprobación
str4 = "Python"
print(str4.isalnum())
print(str4.isdigit())
print(str4.isdecimal())
print(str4.isupper())
print(str4.isascii())

print("-----------------------------------------------------------------------")
"""
* Crear un programa que analice dos palabras y realizar comprobaciones para descubrir si son:
-Palíndromos [X]
-Anagramas [X]
-Isogramas [X]

*Palindrimos: Palabra o frase cuyas letras están dispuestas
de tal manera que resulta la misma leída de izquierda a derecha.
*Anagramas: Cambio en el orden de las letras de una palabra o
frase que da lugar a otra palabra o frase distinta.
*Isogramas: Palabra o frase en la que cada letra aparece la misma cantidad de veces.
"""

def esPalindromo(palabra):
    return palabra == palabra[::-1]

def esAnagrama(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

def esIsograma(palabra):
    return len(set(palabra)) == len(palabra)

palabra1 = input("Ingrese la primera palabra: ").replace(" ", "").lower()
palabra2 = input("Ingrese la segunda palabra: ").replace(" ", "").lower()

print(f"{palabra1} es un palindromo: {esPalindromo(palabra1)}")
print(f"{palabra2} es un palindromo: {esPalindromo(palabra2)}")

print(f"{palabra1} y {palabra2} son anagramas: {esAnagrama(palabra1, palabra2)}")

print(f"{palabra1} es un isograma: {esIsograma(palabra1)}")
print(f"{palabra2} es un isograma: {esIsograma(palabra2)}")

print("-------------------------FIN CLASE CADENA-------------------------")

# Tipo de datos por VALOR (PASO POR VALOR)
a = 10
b = a
b = 20
print(f"Valor de A", {a})
print(f"valor de B", {b})
print("--------------------------------------")

# Tipos de datos por REFERENCÍA (Estos aplican a Estructuras de datos lista, tuplas, sets)
lista_a = [10, 20, 30]
lista_b = lista_a
lista_b.append(40)
lista_a.append(50)
print(lista_a)
print(lista_b)
print("--------------------------------------")

# Funciones con datos por referencia
def listaFunsion(mi_lista_A: list):
    mi_lista_A.append(60) # Creo el primer y UNICO apuntador de memoria
    mi_lista_B = mi_lista_A # Local (Se asigno el apuntador de la lista A a la lista B)
    mi_lista_B.append(70)
    print(mi_lista_A) # NO APARECE SOLAMENTE [60]
    print(mi_lista_B) # NO APARECE SOLAMENTE [60, 70]

mi_lista_C = [80, 90] # Global (Crea una lista nueva C con su apuntador UNICO)
listaFunsion(mi_lista_C) # NO APARECE SOLAMENTE [80, 90]
print(mi_lista_C)

#print(listaFunsion(mi_lista_A=[10]))

# LISTA DE LISTAS (MATRIZ)
productos = [["Producto1", "Producto2", "Producto3"], #Alimentos
            ["Producto4", "Producto5", "Producto6"], #Ferreteria
            ["Producto7", "Producto8"] #Snacks
            ]

# Diccionario de Listas
productos = {
    "consolas": ["Xbox", "PS5", "Nintendo Switch", "SteamDeck"],
    "ropa": ["Camisa", "Tenis", "Pantalones", "Calcetas"],
    "telefonos": ["Iphon X15Pro", "Huawei P30", "Poco X6 Pro","Galaxi S22"],
}

print("--------------------------------------")

"""
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */
"""

# Valor
def value(value_a: int, value_b: int):
    temp = value_a 
    value_a = value_b 
    value_b = temp 
    return value_a, value_b

valor_1 = 10
valor_2 = 20
valor_3, valor_4 = value(valor_1, valor_2) # Valor 1 es A y valor 2 es B por el orden de paramatros
print(f"{valor_1}, {valor_2}")
print(f"{valor_3}, {valor_4}")

print("--------------------------------------")

# Referencia
def ref(dato_a: list, dato_b: list):
    temp = dato_a #temp = A [10,20]
    dato_a = dato_b #A = B [30,40]
    dato_b = temp #B = temp [10, 20]
    return dato_a, dato_b

my_list_A = [10, 20]
my_list_B = [30, 40]

my_list_C, my_list_D = ref(my_list_A, my_list_B)
print(f"{my_list_A}, {my_list_B}")
print(f"{my_list_C}, {my_list_D}")
