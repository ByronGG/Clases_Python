# KNN -> Sistema para recomendar a los usuarios

"""
La idea será:
* Tenemos clientes con historial de compras
* Encontramos clienjtes similares con KNN
* Recomendamos productos que:
    - Los vecinos compran mucho
    - Pero el cliente objetivo compra poco (o nada)

Esto es User-Based Collaborative Filtering
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA

# =======================
# 0) Configuración
# =======================
DATA_PATH = "food_store_purchases.csv"

K = 15  # Flods
TAGERT_ROW = 710  # vecino a usar (Este valor lo puedes cambiar)
TOP_N_RECS = 3  # cuántas recomendaciones dar (Este valor lo puedes cambiar)

# Productos (items) que vamos a recomendar
ITEMS_COLS = ["burgers", "pizza", "tacos", "drinks", "desserts"]

# Variables para encontrar similitud (comportamiento)
FEATURES = [
    "visits_per_month",
    "avg_ticket",
    "burgers",
    "pizza",
    "tacos",
    "drinks",
    "desserts",
    "total_items",
]

# =======================
# 1) Cargar dataset
# =======================
df = pd.read_csv(DATA_PATH)
X = df[FEATURES].copy()

# =======================
# 2) Escalado (IMPORTANTE)
# =======================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =======================
# 3) KNN para vecinos similares (User-Based)
# =======================
knn = NearestNeighbors(n_neighbors=K + 1, metric="euclidean")
knn.fit(X_scaled)

distances, indices = knn.kneighbors(X_scaled[TAGERT_ROW].reshape(1, -1))

# El primer vecino es el mismo usuario (dist=0). Lo quitamos
neighbor_rows = indices[0][1:]
neighbor_distance = distances[0][1:]
target_customer_id = df.loc[TAGERT_ROW, "customer_id"]

print("\n============================")
print("Cliente objetivo")
print("============================")
print(f"Fila objetivo: {TAGERT_ROW} | customer_ud: {target_customer_id}")
print(df.loc[TAGERT_ROW], ["customer_id"] + FEATURES + ["favorite_category"])

# =======================
# 4) Recomendación
#   Idea:
#       - Perfil del usuario objetivo:  compras actuales (ITEMS_COLS)
#       - Perfil proimedio de vecino: compras promedio de vecinos (ITEM_COLS)
#       - Score de rtecomendación = (promedio vecinos) - (usuario)
#       - Recomendar items con score alto
# =======================

target_items = df.loc[TAGERT_ROW, ITEMS_COLS].astype(float)
neighbor_items = df.loc[neighbor_rows, ITEMS_COLS].astype(float)

# Paso por distacnia (opcional, recomiendo):
# Vecinos más cercanos pesan más
# Convertimos distancias a peso: weigh = 1 / (dist + eps)
eps = 1e-9
weights = 1.0 / (neighbor_distance + eps)
weights = weights / weights.sum()

# Promedio ponderado de compras de vecinos
neighbor_mean = (neighbor_items.T * weights).T.sum(axis=0)

# Score: qué tanto "falta" en el usario vs vecino
recommendation_score = neighbor_mean - target_items

recs = pd.DataFrame(
    {
        "item": ITEMS_COLS,
        "user_count": target_items.values,
        "neighbors_avg": neighbor_mean.values,
        "score": recommendation_score.values,
    }
).sort_values("score", ascending=False)

# Recomendamos solo donde el score sea positivo (vecinos compras más que el usuario)
recs_positive = recs[recs["score"] > 0].head(TOP_N_RECS)

print("\n============================")
print(f"Recomendaciones TOP {TOP_N_RECS} (Basado en vecinos)")
print("============================")
print(recs_positive.to_string(index=False))

# =======================
# 5) Visualización: comparación usuario vs vecinos
# =======================

plt.figure()
x = np.arange(len(ITEMS_COLS))

plt.bar(x - 0.2, target_items.values, width=0.4, label="Cliente objetivo")
plt.bar(x + 0.2, neighbor_mean.values, width=0.4, label="Promedio vecinos")

plt.xticks(x, ITEMS_COLS)
plt.ylabel("Cantidad comprada")
plt.title("Perfil de compras: objetivo vs vecinos (KNN)")
plt.grid(True, axis="y", alpha=0.3)
plt.legend()
plt.show()

# =======================
# 6) Visualización: score de recomendación
# =======================

plt.figure()
plt.bar(recs["item"], recs["score"])
plt.axhline(0, linewidth=1)
plt.ylabel("Score (vecinos_avg - usuario)")
plt.title("Score de recomendación por producto (positivo = recomendado)")
plt.grid(True, axis="y", alpha=0.3)
plt.show()

# =======================
# 7) Visualización 2D con PCA: objetivo y vecinos
# =======================
pca = PCA(n_components=2, random_state=42)
X_2d = pca.fit_transform(X_scaled)

target_point = X_2d[TAGERT_ROW]
neighbors_points = X_2d[neighbor_rows]

plt.figure()
plt.scatter(X_2d[:, 0], X_2d[:, 1], alpha=0.2, label="Todos los clientes")
plt.scatter(neighbors_points[:, 0], neighbors_points[:, 1], alpha=0.9, label="Vecinos Similares")
plt.scatter([target_point[0]], [target_point[1]], marker="X", s=160, label="Objetivo")

for p in neighbors_points:
    plt.plot([target_point[0], p[0]], [target_point[1], p[1]], linewidth=0.8, alpha=0.5)

plt.title(f"Clientes similares con KNN (PCA 2D) | Objetivo id={target_customer_id}")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()