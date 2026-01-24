import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"pip install numpy, pandas, matplotlib, sklearn"

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA

# =================
# 1) Cargar dataset
# =================

df = pd.read_csv("food_store_purchases.csv")

# =================
# Configuración
# =================

K = 10 # número de vecinos (clintes similares)
TARGET_ROW = 0 # fila objetivo (puedes cambiar: 0...len(df) - 1)

# =================
# 2) Selección de variables (features)
# =================

features = [
    "visits_per_month",
    "avg_ticket",
    "burgers",
    "pizza",
    "tacos",
    "drinks",
    "desserts",
    "total_items"
]

X = df[features].copy()

# =================
# 3) Escalado (CLAVE para KNN)
# =================

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =================
# 4) KNN: vecinos más cercanos (similitud)
# =================
# Usamos NearestNeighbors (es KNN para similitud, no para clasificar!!!)

knn = NearestNeighbors(n_neighbors=K + 1, metric="euclidean")
knn.fit(X_scaled)
distances, indices = knn.kneighbors(X_scaled[TARGET_ROW].reshape(1, -1))

# indices incluye al mismo punto como vecino 0 (distancia 0)
neighbor_rows = indices[0]
neighbor_distances = distances[0]

# Quitamos el primero (es el mismo cliente objetivo)
neighbor_rows = neighbor_rows[1:] #POV 
neighbor_distances = neighbor_distances[1:]

target_customer_id = df.loc[TARGET_ROW, "customer_id"]

print("\n==========================================")
print("Cliente objetivo")
print("==========================================")
print(f"Fila objetivo: {TARGET_ROW}")
print(f"customer_id: {target_customer_id}")
print(df.loc[TARGET_ROW, ["customer_id"] + features + ["favorite_category"]])

print("\n==========================================")
print(f"TOP {K} clientes más similares (por distancia euclidiana en features escaladas)")
print("==========================================")

neighbor_table = df.loc[neighbor_rows, ["customer_id"] + features + ["favorite_category"]].copy()
neighbor_table["distance"] = neighbor_distances
neighbor_table = neighbor_table.sort_values("distance")

print(neighbor_table.head(K).to_string(index=True))

# =================
# 5) Visualización 2D con PCA (para poder graficar)
# =================
# PCA reduce de 8 dimenciones -> 2 dimensiones, solo para visualizar

pca = PCA(n_components=2, random_state=42)
X_2d = pca.fit_transform(X_scaled)

target_point = X_2d[TARGET_ROW]
neighbors_points = X_2d[neighbor_rows]

plt.figure()
plt.scatter(X_2d[:, 0], X_2d[:, 1], alpha=0.25)

# Resaltar vecinos
plt.scatter(neighbors_points[:, 0], neighbors_points[:, 1], marker="o", alpha=0.9)

# Resaltar objetivo (más grande)
plt.scatter([target_point[0]], [target_point[1]], marker="X", s=160)

# Conectar objetivo con vecinos (lineas)
for p in neighbors_points:
    plt.plot([target_point[0], p[0]], [target_point[1], p[1]], linewidth=0.8, alpha=0.6)

# Mostrar grafica
plt.title(f"KNN: Clientes similares (PCA 2D) | objetivo row={TARGET_ROW} id={target_customer_id}")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.grid(True, alpha=0.5)
plt.show()

# =================
# 6) Visualización: distancia a vecinos
# =================

plt.figure()
plt.plot(np.arange(1, K + 1), neighbor_distances, marker="o")
plt.xticks(np.arange(1, K + 1))
plt.title("Distancias a los K vecinos más cercanos")
plt.xlabel("Vecino # (orden por cercanía)")
plt.ylabel("Distancia (en espacio escaladp)")
plt.grid(True, alpha=0.5)
plt.show()

# =================
# 7) Extra: explicar qué significa la distancia
# =================
print("\n==========================================")
print("Cómo intepretar la distancia")
print("==========================================")
print("- Distncia prqueña = compras y comportamientos similares (en promedio)")
print("- Distancia grande = pefil distino (frecuencia, ticket, mix de productos)")
print("\nTip: prueba cambiardo TAGET_ROW y K para ver diferentes perfiles")