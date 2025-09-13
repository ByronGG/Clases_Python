"""
    Árbol de decisión.
    Un árbol de desición es un modelo de machine learning supervisado que se usa tanto para clasificación como para regresión.
    Su funcionamiento se basa en representar la decisiones en forma de un árbol donde:

        * Nodos internos -> representan una condición o prubea sobre un característica (ejemplo: ¿edad < 18?)
        * Ramas -> representan el resultado de la condición (ejemplo: sí o no)
        * Hojas -> representan una decisión final o una preducción (ejemplo: Clase = Niño o ingreso = 10,000 )

    La idea es dividir el espacio de los datos en regiones cada vez más homogéneas:
        * Si es clasificación -> cada hoja intenta conectener instancias de una sola clase.
        * Si es regresión -> cada hoja intenta predecir un valor lo más cercano posible a los datos reales.

        Ejemplo (Clasificación):
        * Quieres predecir si una persona comprará un producto:
            * Nodo raíz: ¿Edad < 30?
                * Sí -> ¿Ingreso > 50k?
                    * Sí -> Compra.
                    * No -> No Compra.
                * No -> Compra.

    Ventajas:
        1. Fácil de entener
        2. Reuiqere poca preparación de los datos (no necesita normalización ni escalado)
        3. Puede manejar tanto variables categóricas como numéricas

    Deventajas:
        1. Puede sobreajustar (overfitting) si no se controla la profundidad
        2. Menos precisos que modelos más complejos (Ramdon Forest o Gradient Boosting)
        3. Son inestables (pequeños cambios en los datos -> gran cambio en el árbol)

    ¿Cómo decide un árbol dónde dividir?
    Teoria:
        * Para clasificación, se usan métricas como:
            * Entropía y Ganancia de información (ID3, C4.5)
            * Índice Gini (CART)
        * Para regresión:
            * Error cuadratico medio (MSE) o desviación absoluta media (MAE)

    1. Clasificación
    La entropía mide la incertidumbre de un conjunto de datos:
            
            H(S)=−i=1∑k​pi​⋅log2​(pi​)

        Donde:
            S = conjunto de ejemplos de el nodo
            k = número de clases
            pi = proporción de elementos de la clase i

    ¿Qué es el indice Gini?

            Gini(S)=1-∑ki=1p^2i

    Mide la impureza de un nodo usada en árboles de desición (CART). Mide la probabilidad esperada de clasificar incorrectamente un ejemplo si lo etiquetamos aleatoriamente según la distribucipin de clases del nodo.

        * Si todas las instancias en el nodo pertecene a una sola clase -> pi = 1 para esa clase y Gini = 0 (nodo puro)
        * Si las clases están mezclas de forma uniforme -> Gini es mayor (máximo cuando las clases son uniformes)
        * En clasificación binaria con p para la clase positiva: Gini=2p(1-p)

    Cálculo para una división (split)
        Para un atributo A que crea particiones Sv (por cada valor o cada rama), el Gini post-split ponderado es:
            
            Ginisplit(S,A)=∑|Sv|/|S|Gini(Sv)
        
        Y para la reducción de impureza (Gini descrese) es:

            ΔGini=Gini(S)−Ginisplit​(S,A)

    Ejemplo paso a paso (aritmética explicada dígito a dígito)
    Datos en el nodo raíz: 10 instancias -> 6 de clase Sí y 4 clase No.
        1. Probabilidades:
            * pSi = 6 / 10 = 0.6
            * pNo = 4 /10 = 0.4
        2. Cuadrados:
            * p^2Si = 0.6^2 (porque 0.6 * 0.6 = 0.36)
            * p^2No = 0.4^2 (porque 0.4 * 0.4 = 0.16)
        3. Suma de cuadros: 0.36 + 0.16 = 0.52
        4. Gini raíz 1 - 0.52 = 0.48

    Ahora una division por "Edad < 30" resulta en dos tamas con 5 instancias cada una:
        * Rama A: 4 Sí, 1 No -> total 5.
            * pSi = 4/5 = 0.8 pNo = 1/5 = 0.2
            * p^2Si = 0.8^2 = 0.64 p^2No = 0.2^2 = 0.04
            * Suma = 0.64 + 0.04 = 0.68
            * Gini(A) = 1 - 0.68 = 0.32

        * Rama B: 2 Si, 3 No -> total 5.
            * pSi = 2/5 = 0.4 pNo = 3/5 = 0.6
            * p^2Si = 0.4^2 = 0.16 p^2No = 0.6^2 = 0.36
            * Suma = 0.16 + 0.36 = 0.52
            * Gini(B) = 1 - 0.52 = 0.48

        Gini ponderado tras el split:
            Ginisplit = 5/10 * 0.32 + 5/10 * 0.48 = 0.5 * (0.32 + 0.48) = 0.5 * 0.80 = 0.40

        Reducción de gini:
            ΔGini = 0.48 - 0.40 = 0.08
        Interpretación: la división redujo la impureza en un 0.08

        Pseudocódigo rápido para evaluar un split en una catacterística continua:

        ordenar muestras por x
        calcular conteos totales por clase (right_counts = total_counts)
        left_counts = cero
        mejor_delta = 0
        para cada posición i desde 1 a n-1:
            mover muestra i de right_counts a left_counts
            si label(i) != label(i+1):  # candidato de split entre i y i+1
                calcular Gini(left) y Gini(right) usando left_counts/right_counts
                gini_split = (n_left/n_total)*Gini(left) + (n_right/n_total)*Gini(right)
                delta = Gini(parent) - gini_split
                si delta > mejor_delta: guardar umbral y mejor_delta
        retornar mejor umbral, mejor_delta

"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
import matplotlib.pyplot as plt

# Datos de ejemplo
data = {
    "Edad": [22, 25, 47, 52, 46, 56, 48],
    "Ingreso": [15000, 40000, 50000, 60000, 80000, 52000, 30000],
    "Compra": ["No", "No", "Sí", "Sí", "Sí", "Sí", "No"]
}
df = pd.DataFrame(data)

# 1. Exploración incial del dataset
print("Primeras filas del dataset:")
print(df.head(),"\n")

print("Resumen estadístico:")
print(df.describe(), "\n")

print("Distribuciíon de la variable objetivo (Compra):")
print(df["Compra"].value_counts(), "\n")

# 2. Preparación de variables
X = df[["Edad", "Ingreso"]]
y = df["Compra"]

# 3. Entrenamiento del modelo
clf = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42)
clf.fit(X, y)

# 4. Reglas del árbol
print("Reglas del árbol de decisión:")
print(export_text(clf, feature_names=list(X.columns)), "\n")

# 5. Importancia de las variables
importancia = pd.DataFrame({
    "Caracteristicas" : X.columns,
    "Importancia": clf.feature_importances_
}).sort_values(by="Importancia", ascending=False)

print("Importancia de las caracteristicas:")
print(importancia, "\n")

# 6. Visualizacion grafica
plt.bar(importancia["Caracteristicas"], importancia["Importancia"], color="skyblue")
plt.title("Importancia de las características")
plt.xlabel("Caracteristicas")
plt.ylabel("Importancia")
plt.show()