#Numpy

"""
    NumPy (Numerical Python) es una librería fundamental para la computación numérica en Python. Su principal característica es la creación y manipulación eficiente de arreglos multidimensionales (arrays), estructuras de datos optimizadas para realizar operaciones matemáticas complejas. Está escrita en C, lo que le permite ser rápida y eficiente en el manejo de grandes volúmenes de datos.

    ¿Para qué sirve?
    - NumPy se utiliza en áreas como:
    - Cálculos científicos: Álgebra lineal, transformadas de Fourier, estadística.
    - Procesamiento de datos: Manipulación de matrices, filtrado, agregación.
    - Machine Learning: Preparación de datos y operaciones matemáticas en algoritmos.
    - Simulaciones: Modelado numérico, generación de números aleatorios.
    - Su ventaja principal es la velocidad, ya que evita el uso de bucles en Python puro al operar directamente sobre arreglos de forma vectorizada.

    Diferencias con otras librerías de Python
    - Listas nativas de Python:
    - NumPy no es una librería "alternativa" a las listas, pero sus arreglos son más eficientes para cálculos numéricos.
    - Otras librerías como Pandas (enfocada en datos tabulares) o SciPy (funciones matemáticas avanzadas) se construyen sobre NumPy, aprovechando sus arreglos.
    - Matplotlib (visualización) usa arreglos de NumPy para graficar datos.
    - Librerías como TensorFlow/PyTorch (machine learning) tienen estructuras similares a los arreglos de NumPy, pero orientadas a cálculos en GPU.
    En resumen, NumPy es la base para la mayoría de las herramientas de computación científica en Python, ofreciendo una interoperabilidad clave entre librerías.

    Lista: Pueden alamacenar elementos de distintos tipos (númericos, string, etc) Build-in
    Arreglos de NumPy: Todos los elementos son del mismo tiempo (homogénos), lo que optimiza memoria y rendimiento

    * Memoria: Los arreglos almacenan datos en bloque contiguos de memoria, reduciendo la sobrecarga. Las lista guardan referenica a objetos dispersos en memoria
"""

import numpy as np # La convención es usar 'np' como alisas


# Crear un arreglo
lista = [1, 2, 3, 4, 5]
arreglo = np.array(lista) # Converite la lista en un arreglo de NumPy
print(lista)
print(arreglo)

print("-----------------------------------------------------------------------------")

# Arreglo multidimensional (matriz)
matriz = np.array([[1,2,3], [4,5,6]])
print(matriz)

print("-----------------------------------------------------------------------------")

# Funciones útiles para crear arreglos
arreglo = np.array([[1,2,3], [4,5,6]])
print(arreglo.ndim) # Dimensión 2 (Matriz)
print(arreglo.shape) # Forma: (2, 3) -> 2 filas, 3 columnas
print(arreglo.size) # Total de elementos: 6
print(arreglo.dtype) # Int64 -> 8 Bytes -> -9,223,372,036,854,775,808 a 9,223,372,036,854,775,808
                    # Int32 -> 4 Byres  -> -2,147,483,648 a 2,147,483,648
                    # Int16 -> 2 Bytes -> -32,768 a 32,768


print("-----------------------------------------------------------------------------")

# Fuinciones comunes
ceros = np.zeros(5)
print(ceros)
unos = np.ones(5)
print(unos)
rango = np.arange(0, 10, 2) # Valores del 0 al 10 (excluisivo) con paso 2
print(rango)
aletorios = np.random.rand(30) # Genera numeros aleatorios entre 0 y 1
print(aletorios)

print("-----------------------------------------------------------------------------")

# Matemáticas
a = np.array([2,3,4])
b = np.array([7,8,9])

suma = a + b
resta = a - b
multi = a * b
division = b / a 

print(suma)
print(resta)
print(multi)
print(division)

print("-----------------------------------------------------------------------------")

# Producto matricial

matriz_a = np.array([[7,5], [1,2]])
matriz_b = np.array([[5,9], [16,14]])
producto = np.dot(matriz_a, matriz_b)
print(producto)

print("-----------------------------------------------------------------------------")

# Indexación y Slicing
arreglo = np.array([10,20,30,40,50])
print(arreglo[0])
print(arreglo[1:4])

matriz = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(matriz[2,1])
print(matriz[:, 1])

print("-----------------------------------------------------------------------------")

arreglo = np.array([1, 2, 3, 4, 5])
print(arreglo)
print(np.sum(arreglo))
print(np.mean(arreglo))
print(np.max(arreglo))

print("-----------------------------------------------------------------------------")

arreglo = np.arange(6)
matriz = arreglo.reshape(6, 1)
print(matriz)

print("-----------------------------------------------------------------------------")

a = np.array([2,4,6,8,10])
b = 2
print(a * b)

print("-----------------------------------------------------------------------------")

# Filtros
arreglo = np.array([5, 10, 15, 20])
filtros = arreglo[arreglo > 10]
print(filtros)

print("-----------------------------------------------------------------------------")

# Manipulación de arreglos reshape

arr = np.arange(12) # -> [0 1 2 3 4 5 6 7 8 9 10 11]
print(arr)
arr2 = arr.reshape(6, 2) # -> Array a Matriz
print(arr2)

print("-----------------------------------------------------------------------------")

# Álgebra Lineal
matriz = np.array([[1,2],[3,4]])
inversa = np.linalg.inv(matriz) # Matriz Inversa
print(inversa)
determinante = np.linalg.det(matriz) # Determinate
print(determinante)
autovalores, autovalores = np.linalg.eig(matriz) # Valores y vectores propios
print(autovalores)

print("-----------------------------------------------------------------------------")

arr = np.array([1, 4, 9])
raices = np.sqrt(arr)
exponcial = np.exp(arr)
print(raices)
print(exponcial)

print("-----------------------------------------------------------------------------")

# Guardar y cargar datos

# np.save('datos.npy', arreglo) # Guardar en formato binario
# cargado = np.load('datos.npy') # Carga

# np.savetxt('matriz.txt', matriz) # Guarda como texto (txt)
# matriz_txt = np.loadtxt('matriz.txt') #Carga desde un Text (txt)

print("-----------------------------------------------------------------------------")

# Integración con otras libreías
import pandas as pd

df = pd.DataFrame({"col1": [1,2], "col2": [3,4]})
arreglo_desde_df = df.to_numpy()

import matplotlib.pyplot as plt

# plt.plot(np.random.randn(100))
# plt.show()

"""
Ejercicio: Análisis de Temperaturas
Objetivo: Generar datos sintéticos de temperaturas, analizarlos con NumPy y visualizarlos con Matplotlib.

    Enunciado:
    Generación de datos:
        Crea un arreglo de NumPy con 30 valores aleatorios que representen temperaturas diarias (en °C) durante un mes.
        Las temperaturas deben oscilar entre 5°C (mínimo) y 35°C (máximo).
        Agrega un ruido aleatorio (valores pequeños +/-) a los datos para hacerlos más realistas.
    Cálculos con NumPy:
        Calcula:
            Temperatura promedio del mes.
            Días con temperaturas superiores a 25°C.
            Temperatura máxima y mínima (y sus posiciones en el arreglo).
            Visualización con Matplotlib:
            Grafica las temperaturas diarias como una línea azul.
            Marca con un punto rojo la temperatura máxima y con un punto verde la mínima.
            Dibuja una línea horizontal negra punteada para el promedio.
    Añade etiquetas, título y leyenda al gráfico.
    Bonus:
        Usa np.polyfit para ajustar una tendencia polinómica (grado 1) a los datos y grafica esta tendencia sobre el gráfico original.
"""

import numpy as np
import matplotlib.pyplot as plt

# Generar datos
dias = np.arange(1, 31)
temperaturas = np.linspace(5, 35, 30) + np.random.normal(0, 3, 30)


# AQUI VA LA TAREA


# GRAFICAS
plt.figure(figsize=(10, 6))
plt.plot() # AQUI VA LOS PARAMETROS (DIA DIARIO)
plt.plot() # AQUI VA LOS PARAMETROS (MAX)
plt.plot() # AQUI VA LOS PARAMETROS (MIN)
plt.plot() # AQUI VA LOS PARAMETROS (PROMEDIO)
plt.title("Temperaturas Diarias - Marzo 2025")
plt.xlabel("Dias")
plt.ylabel("Temperaturas (°C)")
plt.grid(True)
plt.show()

# Imprimir resultados
