import numpy as np
import matplotlib.pyplot as plt

"""
    Índice Gini o como criterio de division, método de básico de árboles de decisión para seprara datos de dos clases (0 y 1)
    Aprendizaje supervisado donde el objetivo es predecir una variable categónica con dos calses (enfermo/sano - spam/nospam - gato/perro - etc/ect). En código las son 0 y 1

    G = A/(A+B) -> Gini = 1-∑^ni=1(Pi)^2
    Gini = 0: El nodo es puro (todas las muestras son de una misma clase)
    Gini ≈ 1: Máxima impureza (clase distribuidas uniformemente)

    Criterio de División con Gini
    Es un árbol de desición, en cada node se busca la mejor división (característica y umbral) que minimce la impureza Gini en los subgrupos

    Paso:
        1. Para cada caracteriscia:
            - Ordenar los valores de la cracterística.
            - Evaluar cada valor único como umbral de división
        2. Calcular el Gini ponderado para la división
                Giniponderado = Nizq/Ntotal * Giniizq + Nder/Ntotal * Ginider
        3. Seleccion la disivión con el menor Gini ponderado

        Ejemplo de datos:

        Caracteristica 0 | Caracteristca 1 | Clase
            2.0                 1.0             0
            1.5                 2.0             0 
            3.0                 4.0             0
            5.0                 7.0             1
            4.5                 6.5             1
            6.0                 5.0             1

        
"""

# Datos de ejemplo [Caractistica 1 - Caracteristica 2, Clase]
datos = np.array([
    [2.0, 1.0, 0],
    [1.5, 2.0, 0],
    [3.0, 4.0, 0],
    [5.0, 7.0, 1],
    [4.5, 6.5, 1],
    [6.0, 5.0, 1]
])

# Funcion para calcular la impureza de Gini
def gini_impurity(clases):
    clases_unicas, conteos = np.unique(clases, return_counts=True)
    probabilidades = conteos / len(clases)
    return 1 - np.sum(probabilidades ** 2)

# Giniponderado = Nizq/Ntotal * Giniizq + Nder/Ntotal * Ginider

# Funcion para encontrar la mejor división
def mejor_division(X, y):
    mejor_gini = float('inf')
    mejor_inidice = None
    mejor_valor = None
    for indice in range(X.shape[1]): # [0][1][2][pivote][][][]
        valores = np.unique(X[:, indice]) # [0][1][2]
        for valor in valores:
            umbral = X[:, indice] <= valor
            y_izq = y[umbral]
            y_der = y[~umbral]
            if len(y_izq) == 0  or len(y_der) == 0:
                continue
            gini = (len(y_izq) * gini_impurity(y_izq) + len(y_der) * gini_impurity(y_der)) / len(y)
            if gini < mejor_gini:
                mejor_gini = gini
                mejor_inidice = indice
                mejor_valor = valor
    return mejor_inidice, mejor_valor

# Dividir los datos en caracteristicas [X] y etiquetas [y]
X = datos[:, :2]
y = datos[:, 2]

#Encontrar la mejor división
indice, valor = mejor_division(X, y)
print(f"Mejor división: Caracteristicas {indice} <= {valor:.2f}")

"""
    Cálculo a Mano GINI
    Gini = 1 - ((2/4)^2 + (2/4)^2) = 1 - (0.25+0.25) = 0.5
"""
