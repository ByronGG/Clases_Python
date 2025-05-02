"""
Crea un programa en Python que haga lo siguiente:

Pida al usuario que ingrese una frase (una cadena de texto). [x]
Divida la frase en palabras y guarde cada palabra en una lista. [x]
Luego, usando un bucle, realiza las siguientes acciones: 
Imprime cada palabra junto con su número de caracteres. [x]
Guarda en otra lista todas las palabras que tengan más de 4 letras. [x]
Al final, muestra la nueva lista de palabras largas.

Extras (opcional):
Muestra cuántas palabras en total tienen más de 4 letras. [x] 
Ordena alfabéticamente la lista de palabras largas antes de imprimirla. []
"""

# frase = input("Ingresa una frase: ")
# palabras = frase.split()

# palabras_largas = []
# for palabra in palabras:
#     print(f"{palabra}: {len(palabra)} caracteres")

# frase = str(input("Ingresa una frase: ")) #Ingresamos
# palabras = frase.split() # dividimos
# palabras_largas = [] # Almacenar las palabras
# contador_largas = 0

# print("Palabras y su longitud")
# for palabra in palabras:
#     longitud = len(palabra)
#     print(f"{palabra}: {longitud} caracteres")
#     if longitud > 4:
#         palabras_largas.append(palabra)
#         contador_largas += 1

# palabras_largas_ordenadas = sorted(palabras_largas)

# print("Lista de palabras largas: ",palabras_largas)
# print("Total palabras con más de 4 letras: ", contador_largas)
# print("Orden alfabetico: ", palabras_largas_ordenadas)

"""
Crear un programa que realice las siguientes oepracione utilizando listas de comprensión, bucles y condicionales
Entrada:
    - Pide al usuario ingressar números enteros positivos uno por uno
    - El ingreso termina cuando el suaurio escribe -1
    - Ignora cualquier número negativo (excepto -1 para salir) y valores no númericos

Procesamiento:
    - Crea dos listas de comprensión:
        - pares: Números pares de la lista original
        - impares: Números impares de la lista original
    - Calcula usando bucles:
        - Suma total de todos los números
        - Promedio de los números pares
        - Número máximo de la lista original (sin usar la función max())
    -Identifica números primos de la lista original usando condiciones y bucles

Salida:
    - Muestra las listas de pares e impares
    - Imprime las estadísticas calculadas
    - Usa al menos 2 listas de compresión.
    - Usa al menos 1 blucle while y 3 for
    - Use condicionales para todas las verificaciones

"""

def es_primo(n):
    # Verificar si un número es primo
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Datos de entrada
numeros = []
print("Ingresa números positivos (o -1 para salir): ")
while True:
    entrada = input("> ").strip()
    try:
        num = int(entrada)
        if num == -1: # Rompo el WHILE INFITO con break
            break
        if num > 0:
            numeros.append(num) # Agrego a lista vacia "numeros[]" todos los valores mayor a 0 
        else:
            print(f"{entrada} (Ignorada)")
    except ValueError:
        print(f"{entrada} (Ignorado)")
print(f"Lista de números: {numeros}")

# Lista de compresion para pares e impares
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

# Calculo de suma total sin usar sum()
suma_total = 0
for n in numeros:
    suma_total += n

# calculo de promedio de pares
sum_pares = 0
cont_pares = 0
for i in pares:
    sum_pares += i
    cont_pares += 1
promedio_pares = sum_pares / cont_pares if cont_pares > 0 else 0

# Búsqueda del máximo sin usar max()
maximo = numeros[0] if numeros else 0
for n in numeros: # Max = 0 -> 5 -> 2 -> 19 -> 4 -> 10 -> 60 -> 1
    if n > maximo: # Max = 1 > 60?
        maximo = n # Max = 60

# Identificacion de primos
primos = [n for n in numeros if es_primo(n)]

print("\nResultados: ")
print(f"- Pares: {pares}")
print(f"- Impares {impares}")
print(f"- Suma total: {suma_total}")
print(f"- Promedio pares: {promedio_pares}")
print(f"- Maximo: {maximo}")
print(f"- Numeros primos: {primos}")
