"""
    Función lambda es una función anónima (sin nombre) y pequeña, definida con la palabra clave lambda. Es ideal para operaciones simples que pueden escribirse en una sola línea.

    Sintaxis básica
    lambda argumentos: expresión
    
    * No tiene return: La expresión después de : se devuelve automáticamente.
    * No puede tener múltiples líneas: Solo una expresión (no aceptada bloques de código con "if/else" complejos o bucles)
"""

# Ejemplo Sumar

def sumar_def(a, b): # Función normal sumar
    return a + b

sumar = lambda a, b: a + b # Función lambda sumar


print(f"Resultado lambda: {sumar(5, 5)}")
print(f"Resultado def: {sumar_def(5, 5)}")

print("-------------------------------------------------------------------------------------------------------------")

"""
    - map()
    - filter()
    - sorted()
"""

# MAP: Elevar al cuadrado cada número
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros)) # [1, 4, 9, 16]
print(cuadrados)

# Filter: Números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

# Sorted: Ordernar por segunda letra de cada palabra
palabras = ["Arturo", "Luis", "Pepe", "Python", "Lambda"]
ordenado = sorted(palabras, key=lambda p: p[1])
print(ordenado)


print("-------------------------------------------------------------------------------------------------------------")

# Multiplicar tres números
multiplicar = lambda a, b, c: a * b * c
print(multiplicar(2, 3 ,4))

formato = lambda nombre, edad: f"{nombre} tiene {edad} años"
print(formato("Arturo", 20))


print("-------------------------------------------------------------------------------------------------------------")

"""
    Aunque no puedes usar 'if/else', si permniten expresiones ternarias
"""

clasificar = lambda x: "par" if x % 2 == 0 else "impar"
print(clasificar(4))
print(clasificar(7))

print("-------------------------------------------------------------------------------------------------------------")

"""
    LIMITACIONES LAMBDAS
    - No pueden tener bucles (for, while)
    - No manejan excepciones (try/except)
    - No son legibles si son complejas

    CUANDO USAR LAMBDAS
    - Operaciones simples (ejemplo: sumar, filtrar, transoformar)
    - Funciones temperales: que no necesitan nombre
    - Como argurmentos: para funciones de orden superior (map(), filter(), sorted(), etc.)
"""

print("-------------------------------------------------------------------------------------------------------------")

# EJERCICIOS

numeros = [1, 2, 3, 4, 5, 6]
cuadrados = list(map(lambda x: x**2, numeros))
print(f"Lambda Luis: {cuadrados}")

# def cuadrados_def():
#     x = list(map(int, numeros))
#     resultado = x ** 2
#     print(f"Resultado operación: {resultado}")

# cuadrados_def()

def cuadrados_def(lista: list) -> list:
    resultados = [] # Lista para guardar los cuadrados
    for num in lista: # Iteramos sobre cada elementos
        resultados.append(num ** 2) # Elevamos al cuadrado cada numero
    print(f"Def Arturo: {resultados}")
    return resultados

cuadrados_def(numeros)

print("-------------------")

clasificar = lambda x: "par" if x % 2 == 0 else "impar"
print(clasificar(4))
print(clasificar(7))


def clasificar_def():
    x = int(input("Estableca un número entero: "))
    if x % 2 == 0:
        print("Es par")
    else:
        print("Es inpar")

clasificar_def()

print("-------------------")
numeros = [5, 12, 8, 15, 3, 20, 18, 6] # CHECK 5

def filtrar_y_transformar(lista: list) -> list:
    resultado = [] # CHECK 1
    for num in lista: # CHECK 2
        if num > 10: # CHECK 4
            resultado.append(num * 3) #CHECK 3
    return resultado # CHECK 6

print(filtrar_y_transformar(numeros))

resultado = list(map(lambda num: num * 3, filter(lambda num: num > 10, numeros)))

print(resultado)

print("-------------------")

texto = "Hola Mundo"

def procesar_texto(s: str) -> str:
    texto_mayusculas = s.upper()
    texto_invertido = texto_mayusculas[::-1]
    return texto_invertido

print(f"def normal: {procesar_texto(texto)}")

procesar = lambda s: s.upper()[::-1]
print(f"Lambda: {procesar(texto)}")

print("-------------------")


validar = lambda password: len(password) >= 8

print(validar("abc123"))
print(validar("arturo123"))

def es_contraseña_segura(password):
    if len(password) < 8:
        return False
    
    tiene_numero = any(c.isdigit() for c in password)
    return tiene_numero

print(es_contraseña_segura("abc123"))
print(es_contraseña_segura("arturo123"))