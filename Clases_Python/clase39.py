# KNN
"""
    KNN (K-Nearest Neighbors) es un algoritmo sencillo pero poderosos para análisis de datos, no solo para ML "clasico".

    Clasificación y regresión, en análisis de datos se usan para:
        * Explorar similitud entre observaciones
        * Detentar patrones locales
        * Validar clusters
        * Imputadr valores faltantes
        * Entontar outliers

    Para encontrar punto nuevo:
        1. Mides la distancia a todos los puntos
        2. Tomas los K más cercanos
        3. Decides según esos vecinos

    ¿Qué es K?
    K = número de vecinos que mirar!

    1 K => Muy sencible (ruido)
    3 - 5 k => Blance ideal [X]
    6 > k => Suaviza demasiado

    KNN es distancia. Si no entiendes esto KNN falla!!
    Distancia Euclidiana

    √((x1 - x2)^2 + (y1 - y2)^2)

    Otras ditancias
        * Manhattan
        * Minkowski
        * Cosine
    (La distancia correcta depende del "TIPO de DATOS")

    Si K=3 y tus vecinos son:
    Clase A, A, B
"""

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Dataset simple
df = pd.DataFrame({
    "x": [1,2,3,6,7,8],
    "y": [1,1,2,6,7,8],
    "label": ["A","A","A","B","B","B"]
})

X = df[["x", "y"]]
y = df["label"]

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

nuevo = [[4,4]] # 4,4 está más cerca del grupo A | Aunque B este "cerca", la mayoria manda
pred = knn.predict(nuevo)
print("Predicción:", pred[0])

print("-----------------------------------------------------------------------------")

"""
    KNN no es solo para predecir
    KNN para análisis exploratorio
"""

distancia, indice = knn.kneighbors([[4,4]], n_neighbors=3)
print(indice)
print(df.iloc[indice[0]])

print("-----------------------------------------------------------------------------")

"""
    Detención de outliers
    Un punto es outlier si: "Está muy lejos de todos sus vecinos"
"""

from sklearn.neighbors import NearestNeighbors

nn = NearestNeighbors(n_neighbors=5)
nn.fit(X)

distances, _ = nn.kneighbors(X)
outlier_score = distances.mean(axis=1)

df["outlier_score"] = outlier_score
print(df.sort_values("outlier_score", ascending=False))

print("-----------------------------------------------------------------------------")

"""
    Ventajas
        * Muy intuitivo
        * No asume formas de los datos
        * Excelente para análisis local
        * Bueno con datasets pequeño/medianos

    Desventajas
        * Lento con muchos datos
        * Sensible a ruidos
        * Requiere escalado
        * Dificil en alta dimensión
"""