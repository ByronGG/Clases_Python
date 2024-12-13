# For

"""
Un ciclo for se utiliza para iterar sobre una secuencia (como lista, tuplas, diccionario, conjuntos
o cadenas), y ejectuar un bloque de código para cada elemento de la secuencia.
"""

# for variable in secuencia:
#     # Bloque de código

print("-----------------FOR LISTAS--------------------")

nombres = ["Arturo", "Luis", "Reyna", "Pepe", "Jorge"]

for nombre in nombres:
    print(nombre)

print("---------------FOR LETRAS----------------------")

texto = "Arturo"

for letra in texto:
    print(letra)

print("---------------FOR RANGE----------------------")

# Función range()

for i in range(3):
    print(i)

print("----------------FOR RANGE INCIO FIN---------------------")

for i in range(1, 6):
    print(i)

print("----------------FOR RANGE INCIO FIN A PASOS---------------------")

for i in range(0, 10, 2): # Empieza en 0, termina antes del 10, incrementa 2 en 2
    print(i)

print("--------------FOR ELSE-----------------------")

# For - Else

for i in range(5):
    # Inicia el bloque FOR
    print(i)
    # Termina el bloque FOR
else:
    # Bloque que se ejecutara al terminar el FOR
    print("Fin")

print("-------------FOR IF------------------------")

# For - If/Else - Break

for i in range(10):
    if i == 9:
        break
    print(i)
else:
    print("FIN")

print("--------------FOR BREAK-----------------------")

# For - Break
# Break: Sale del ciclo inmediatamente.

for i in range(5):
    if i == 2:
        break
    print(i)

print("--------------FOR CONTINUE-----------------------")

# For - Continue
# Salta a la siguiente iteración

for i in range(5):
    if i == 2:
        # Si la compración es igual salta esa comparación
        continue
        # Compración ya saltada
    print(i)

print("--------------FOR DICT-----------------------")

# Iterar sobre diccionarios
# Key - Value
estudiantes = {"Arturo": 10, "Luis": 5, "Reyna": 9, "Pepe": 0}

# Iterar sobre las Key (claves)
for nombre in estudiantes:
    print(nombre)

# Iretar sobre los valores (Value)
for calificacion in estudiantes.values():
    print(calificacion)

# Iterar sobre Key y Value
for nombre, calificacion in estudiantes.items():
    print(f"{nombre} tiene una calificaion de {calificacion}")

print("-------------FOR ANIDADOS (MATRICES)------------------------")

# Anidación 

# [1][2][3] # Fila
# [4][5][6] # Fila
# [7][8][9] # Fila

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()

print("--------------FOR ENUMATERE-----------------------")

# enumarate() 
# agregar un índice a cada elementos mientras iteramos

frutas = ["Manzana", "Fresa", "Platano", "Sandia", "Mango"]

for indice, fruta in enumerate(frutas):
    print(f"Indice {indice}: {fruta}")

print("---------------FOR LISTA COMPRESION----------------------")

# Listas por compresión

raiz = [x**2 for x in range(10)]
print(raiz)

print("----------------EJERCICIO---------------------")

# Ejercicio práctico
# Crear un programa uqe imprima los números primos 1 al 30 usando for

for numero in range(2, 31): # El primer for solo esta recorriendo los número del 1 al 30
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(numero)
    
print("-----------------WHILE--------------------")

# While

"""
Un ciclo while ejecuta un bloque de código mientras una condición sea VERDADERA.
es ideal cuando no sabes cuántas veces necesitas iterar y la decisión de una condición dinamica.
"""

# Sintaxis básica

# while condicion:
#     # Bloque de código a ejecutar

contador = 1

while contador <= 5: 
    # Bloque verdadero
    print(contador)
    contador += 1 # Incrementar el contador en uno cada vuelta del bucle

# Evitar ciclo infinitos

print("----------------WHILE INFINITO DE LA MUERTE---------------------")

contador = 1

while True: # Siempre será verdadero
    print(contador) # Imprimir el contador
    contador += 1 # Incrementa
    if contador > 5: # Checa hasta mayor que 5
        break # Rompre el ciclo infinito

print("-------------WHILE ENTRADA USUARIO------------------------")

# While con entrada del usuario
# Puede usar un ciclo while para mantener una interacción continua con el usuario

respuesta = ""

while respuesta.lower() != "salir":
    respuesta = input(" Escribe algo o 'salir' para terminar el programa: ")
    print(f"Escribiste: {respuesta}")

# While - Else

print("--------------WHILE ELSE-----------------------")

contador = 1

while contador <= 5:
    print(contador)
    contador += 1
else:
    print("El ciclo termino correctamente")

print("--------------WHILE IF BREAK-----------------------")

#While - If/Else - Break
contador = 1

while contador <= 5:
    print(contador)
    if contador == 3:
        break
    contador += 1
else:
    print("El ciclo termino")

print("--------------WHILE CONTINUE-----------------------")

# While - Continue

contador = 0

while contador < 5:
    contador += 1
    if contador == 3:
        continue
    print(contador)

print("--------------WHILE ENTRADA USUARIO-----------------------")

# Ejemplo practico
# While para validar las entradas del usuario hasta que sean correctas

edad = -1

while edad < 0 or edad > 100:
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad < 0 or edad > 100:
            print("Por favor, ingresa un edad valida")
    except ValueError:
        print("Entrada no valida, ingresa un numero")

print(f" Edad registrada: {edad}")

print("--------------WHILE LISTAS-----------------------")

# While - Listas

tareas = ["Tarea POO", "Tarea C++", "Tarea BD", "Tarea IO", "Tarea Redes"]

while tareas:
    tarea_actual = tareas.pop(0)
    print(f"Haciendo la tarea: {tarea_actual}")

print("Ya termine todas mis tareas, amonos al Fonite")

# Ciclo inifo con una condicion dinámica

print("-------------WHILE RANDOM------------------------")

import random

numero_a_adivinar = random.randint(1, 10)
intento = 0

while True:
    intento += 1
    respuesta = int(input("Adivina el número entre 1 y 10: "))

    if respuesta == numero_a_adivinar:
        print(f"GANASTE lo hiciste a los {intento} intentos, el número era: {numero_a_adivinar}")
        break
    elif respuesta < numero_a_adivinar:
        print("Demasiado abajo. Intentalo de nuevo")
    else:
        print("Demasiado alto. Intentalo de nuevo")

print("-------------WHILE PRO------------------------")

# Bucle while para generar una contraseña valida

import random
import string

def generar_contraseña():
    return "".join(random.choices(string.ascii_letters + string.digits, k=12))

while True:
    contrasena = generar_contraseña()
    if any (c.isdigit() for c in contrasena) and any(c.isupper() for c in contrasena):
        print(f"Contraseña generada: {contrasena}")
        break

print("---------------FIN----------------------")
