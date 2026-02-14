# K-Means
"""
    Un centroide es un punto "promedio" que representa a un grupo de datos en un espacio de caractetísticas.

    Ejemplo:
        Tienes clientes con columnas como:
            * edad
            * ingreso anual
            * gastos
            * vistas al mes
            * compras online
            * fidelidad
    
    Cada cliente es un pinto en un espacio de 6 dimenciones, Un centroide es como decir: "Si este grupo de clientes fuera UNA solo persona promedio, ¿qué valores tendría?

    Si cluster tiene puntos x1, x2...,xn, el centroide es:

    c = 1/n∑_i=1^n xi

    O sea: promedio columna por columna, es importante usar en el K-Mean centroides como "imanes"
        * cada punto se pega al centroide más cercano
        * luego el centroide se mueve al promedio del grupo
        * y repite hasta estabilizar la muestra

    Inticion fuerte: "error" y por qué se mueve el centroide
    K-Means intenta minimizar una cantidad llamada inercio o SSE:
        * Suma de distancias (al cuadrado) de cada punto al centroide como su cluster

    SSE = ∑_k=1^K∑xεC_k ||X-μ_k||^2
    ============================================================================
    Algortimos básico K-Means
        1. Divide datos en K grupos
        2. Cada grupo tiene un centroide
        3. Asigna cada punto al centroide más cercano
        4. Recalcula centroides
        5. Repite hasta converger
    ============================================================================

    Cómo funciona K-Means paso a paso
    Paso 0 : eliges K
        Ejemplo: K = 4 (por qué pensamo que hay 4 tipos de clientes)
    Paso 1: Inicializa centroides
        Escoge K puntos inicilaes (al azar o con un método más inteligente)
    Paso 2: asignación
        Para cada cliente:
            - Calcula distancias a cada centroide
            - Lo asigna al más cercano
        Esto crea K gruipos provisioanales.
    Paso 3: actualización
        Para cada grupo:
            - recalculamos el centroide = promedio de los puntos asignados
    Paso 4: repetir
        Vuelves al paso 2, se detiene cuando:
            - ya casi no cambian las asignaciones
            - o los centroides se mueven muy poco
            - o se llega al máximo de iteraciones

    Distancia: el corazón de K-Means
    
    Por defecto se usa la distnaica auclidiana:
    en 2D:

    d = √(x1-x2)^2+(y1-y2)^2

    Qué significa "Converger"
    K-Means converge cuando ya no hay mejoras (o mejora casi nada) el SSE
    NOTA: K-Means no garantiza el mejor cluster global, solo llega a un mínimo local.
    Por eso suele!:

        * Correr varias veces con diferentes inicializaciones(n_init)
        * Usar K-Means++ para empezar con mejores centroides
    
    Cómo elegir el K correcto
    Método del codo (Elbow)
        * entranas K=1,2,3,...,10
        * calculas SEE
        * la curva baja rápido y luego baja lento
        * el "codo" es un buen K

    Iterpretar:
        * antes del codo, agregar clusters mejora mucho
        * después del codo, agregar cluister casi no ayuda!
    
        A veces no hay un codo claro.
        Estnonces se usa también metodos como:
            * silhouette score
            * calinski-harabasz
            * davies-bouldin index

    Ventajas de K-Means
    * rápido, escala bien
    * fácil de implementar
    * funciona excelente en cluster tipo "bola"
    * Ideal para segmnetación

    Desventajas
    - necetias escoger bien K
    - sensible a oulier (un outlier jala el promedio)
    - sensible a escala (requiere normalización)
    - asume cluister "redondos" y de tamaño similar
    - depende de la inicialización (puede dar diferentes resultados)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score


# =======================
# 1) Cargar dataset
# =======================
df = pd.read_csv("clientes_10000.csv")

# (Opcional) resiva nulos
if df.isna().any().any():
    df = df.dropna()

# Selecciona features numéricas
features = ["edad", "ingreso_anual","gasto_score", "visitas_mes", "compras_online", "fidelidad"]
X = df[features].copy()

print("Dataset cargado:", df.shape)
print(df.head())

# =======================
# 2) Grafica 2 variables para intuición (antes de escalar!!!!)
# =======================
plt.figure()
plt.scatter(df["ingreso_anual"], df["gasto_score"], s=10)
plt.title("ingreso anual vs Gasto score (sin clusters)")
plt.xlabel("ingreso_anual")
plt.ylabel("gasto_score")
plt.show()

# =======================
# 3) Escala variables (Muy importante para K-Means)
# =======================
scaler = StandardScaler()
X_sclaed = scaler.fit_transform(X)

# =======================
# 4) Elbow Methos (inercia/SEE) para elegir K (y extra: silhouette_score para apoyar la descición)
# =======================
Ks = range(2, 11) # 2 a 10 K's
inertias = []
silhouette = []

for k in Ks:
    km = KMeans(n_clusters=k, init="k-means++", n_init=20, random_state=42)
    labels_k = km.fit_predict(X_sclaed)
    inertias.append(km.inertia_)
    silhouette.append(silhouette_score(X_sclaed, labels_k))

# Elbow plot
plt.figure()
plt.plot(list(Ks), inertias, marker="o")
plt.title("Elbow method (Inercia) - Datos escalados")
plt.xlabel("K")
plt.ylabel("Inercia (SEE)")
plt.xticks(list(Ks))
plt.grid()
plt.show()

# Silhouette plot
plt.figure()
plt.plot(list(Ks), silhouette, marker="x")
plt.title("Silhouette Score - Datos escalados")
plt.xlabel("K")
plt.ylabel("Silhouette Score")
plt.grid()
plt.xticks(list(Ks))
plt.show()

# =======================
# 5) Entrenar K-Means con K elegido (ajusta K según tus gráficas; por tu dataset)
# =======================
K = 4 # 4 es el resultado de los métodos Elbow y Silhouette (Esto cambia según el resultado y el dataset)
kmeans = KMeans(n_clusters=K, init="k-means++", n_init=30, random_state=42)
labels = kmeans.fit_predict(X_sclaed)

df["cluster"] = labels
print("\nDistribución de clusters:")
print(df["cluster"].value_counts().sort_index())

# =======================
# 6) Intepretar centroides (perfil promedio por cluster)
#   OJO: kmeans.cluster_centers_ está en escala estandatizada.
#   Lo regresamos a escala original para intepretarlo fácil
# =======================

centroids_scaled = kmeans.cluster_centers_
centroids_origanl = scaler.inverse_transform(centroids_scaled)

centroids_df = pd.DataFrame(centroids_origanl, columns=features)
centroids_df["cluster"] = range(K)

print("\nCentroides (escala original):")
print(centroids_df.sort_values("cluster").round(2))

# Perfiles promedio reales (por asignación final)
print("\nPromedio relaes por cluster (para comprar)")
print(df.groupby("cluster")[features].mean().round(2))

# =======================
# PCA (visualización en 2D)
#       - reducimos en 6D a 2D para graficar
# =======================

pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X_sclaed)

print("\Varianza explicada por PCA:")
print("PC1:", round(pca.explained_variance_ratio_[0], 4),
      "PC2:", round(pca.explained_variance_ratio_[1], 4),
      "Total:", round(pca.explained_variance_ratio_[:2].sum(), 4))

centroids_pca = pca.transform(centroids_scaled)

plt.figure()
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, s=10)
plt.scatter(centroids_pca[:, 0], centroids_pca[:, 1], marker="X", s=200)
plt.title(f"K-Means (K={K}) visualizado con PCA")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()