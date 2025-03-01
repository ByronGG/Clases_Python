# Listas de compresión

"""
Una lista por compresión, en Python son concisa y eficiente de crear lista nuevas

nombre_lista = [expresión for elemento in iterable if condición]

expresion -> Lo que queremos agregar a la lista
elemento -> cada elemento del iterable 'i'
iterable -> una lista, tupla, rango, etc.
condición (opcional) -> un if opcional para filtrar elementos

Ventajas de usar listas por compresión
- Código más corto y legible: Reduce la cantidad de líneas de código
- Más eficiente: Son más rápidas que los bluces 'for' traducionales
- Evita append(): No necesitas llamar lista.append(), lo que mejora la eficincia

Cuando no usarlas
- Si la expresión es muy compleja, puede hacer que el código sea menos legible. En esos casos, un 'for' normal es mejor
- Si necesitas realizar múltiples pasos dentro del bucle 'for'
"""

print("-------------------EJEMPLO 1-------------------")
numeros = [1,2,3,4,5,6,7,8,9]
cuadrados = []
for n in numeros:
    cuadrados.append(n ** 2)
    
# cuadrados = [n ** 2 for n in numeros]

print(cuadrados)

print("-------------------EJEMPLO 2-------------------")

numeros = [1,2,3,4,5,6,7,8,9]
# pares = []
# for n in numeros:
#     if n % 2 == 0:
#         pares.append(n)

pares = [n for n in numeros if n % 2 == 0]
# pares = [] for n in numeros: if n % 2 == 0: pares.append(n)

print(pares)

print("-------------------EJEMPLO 3-------------------")

# Convertir palabras a mayúsculas usando una funsión build-in (python) .upper()

palabras = ["hola","mundo", "python"]
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)

print("-------------------EJEMPLO 4 (MALA PRACTICA)-------------------")

resultado = [x if x % 2 == 0 else x * 2 for x in range(10)]

resultado = []
for x in range(10):
    if x % 2 == 0:
        resultado.append(x)
    else:
        resultado.append(x * 2)

print(resultado)

print("-------------------EJEMPLO 5-------------------")

matriz = [[j for j in range(3)] for i in range(3)] # TAREA POR QUE ES 3x3 y no 2x2
print(matriz)

print("-------------------EJEMPLO 5-------------------")

frases = "Hola Arturo, Esta Aprendiendo listas de compresión" # Esto no es una lista [] más bien es un string ""
vocales = [i for i in frases if i.lower() in "aeiou"]
print(vocales)

print("-------------------EJEMPLO 6-------------------")
import timeit

#Bucle 'for' normal
def con_for():
    lista = []
    for i in range(1000):
        lista.append(i ** 2)
    return lista

# List comprehension
def con_list_comprehension():
    # return [for i in range(1000) lista.append(i ** 2)]
    return [i ** 2 for i in range(1000)]

# Comparar el tiempo 
print(timeit.timeit(con_for, number=1000))
print(timeit.timeit(con_list_comprehension, number=1000))

print("-------------------EJEMPLO 7 (NO WHILE)-------------------")
# El while requiere una condición dinámica, y las listas por compresión están diseñadas para recorrer iteracon con 'for'

# i = 0
# lista = [i for while i < 5] # ESTO ES UN ERROR DE SINTAXIS (FISICO)

i = 0
lista = []
while i < 5:
    lista.append(i)
    i+=1
print(lista)

print("-------------------EJEMPLO 7 (NO FOR-EACH)-------------------")
# En python, for-each no es una estrucutra seperada como otros lenguajes (C++), el for en python ya actúa como un for-each

nombres = ["Ana","Luis","Reyna", "Arturno"]
# C++ 'for' for(i = 0; i < nombre.size(); i++) => 'for-each' for (nombre : nombres)
# Python 'for' for nombre in nombres
for nombre in nombres:
    print(nombre)

#Python build-in len() retorna el int de un elemento

longitudes = [len(nombre) for nombre in nombres] # Lista de compresión
print(longitudes)

print("-------------------EJEMPLO 8 (NO ELIF)-------------------")
# No direcemtne, Pero puedes combianr if-else dentro de la expresión ANTES del for

numeros = [1,2,3,4,5]
#resultado = [n for n in numeros if n % 2 == 0 elif n > 3] # ERROR DE SINTAXIS

resultado = [n if n % 2 == 0 else "impar" for n in numeros] # QUE LAS LISTAS EN PYTHON PUEDEN TENER DIFERENTE TIPO DE DATOS INT & STR (STRING)
print(resultado)

"""
    ✓ Se puede usar 'for' y 'if' dentro de una lista por compresión
    x No se puede usar 'while', 'elif' ni estructuras de control complejas
    ✓ Alternativas: Usar 'range()' en lugar de 'while',y 'if-else' dentro de la expresión
"""
print("-------------------EJEMPLO 9 (OPERADOR TERNARIO)-------------------")

# valor_si_verdero if condición else valor_si_falso 

numeros = [1, 2, 3, 4 ,5 ,6]
resultado = ["Par" if n % 2 == 0 else "Impar" for n in numeros]
print(resultado)

notas = [75, 80, 74, 93, 99, 71]
calficaciones = ["Aprobado" if nota >= 80 else "Reprobado" for nota in notas]
print(calficaciones)

valores = [10, None, 25, None, 50]
limpios = [v if v is not None else 0 for v in valores]
print(limpios)

palabras = ["Hola", "Arturo", "Python", "es", "facil"]

"""
for palabra in palabras:
    if len(palabra) > 3
        print(palabras.append(palabra.upper()))
    else:
        palabra
"""

mayusculas = [palabra.upper() if len(palabra) > 5 else palabra for palabra in palabras]
print(mayusculas)

print("-------------------EJEMPLO 10 (ERRORES COMUNES)-------------------")
# No puedes poner el fi despues del else

numeros = [1, 2, 3, 4 ,5 ,6]
# pares = [n if n % 2 == 0 for n in numeros] # ERROR DE SINTAXIS (Expected 'else')

print("-------------------TAREA-------------------")

"""
Procesamiento de Datos en una Lista por Comprensión
Enunciado: Tienes una lista de diccionarios donde cada diccionario representa a un estudiante con su nombre y su calificación.

La tarea es usar una lista por comprensión con un operador ternario para generar una nueva lista de cadenas con el siguiente formato:

* Si la calificación es mayor o igual a 60, el estudiante está "Aprobado".
* Si la calificación es menor a 60, el estudiante está "Reprobado".
* El resultado debe ser una lista de cadenas con este formato:

["Ana: Aprobado", "Luis: Reprobado", "Carlos: Aprobado", "Marta: Aprobado", "Elena: Reprobado"]

"""
# Tarea

estudiantes = [
    {"nombre": "Ana", "calificacion": 85},
    {"nombre": "Luis", "calificacion": 40},
    {"nombre": "Carlos", "calificacion": 72},
    {"nombre": "Marta", "calificacion": 90},
    {"nombre": "Elena", "calificacion": 50}
]

resultado = [f"{estudiantes['nombre']}: {'Aprobado' if estudiantes['calificacion'] >=70 else 'Reprobado'}" for estudiantes in estudiantes]

print(resultado)