import numpy as np
import pandas as pd

np.random.seed(42)

n = 10000

# ----- CLUSTER 1: Jóvenes gastadores -----
c1 = pd.DataFrame({
    "edad": np.random.normal(23, 4, n//4).astype(int),
    "ingreso_anual": np.random.normal(18000, 4000, n//4),
    "gasto_score": np.random.normal(80, 10, n//4),
    "visitas_mes": np.random.normal(12, 3, n//4),
    "compras_online": np.random.normal(70, 15, n//4),
    "fidelidad": np.random.normal(2, 1, n//4)
})

# ----- CLUSTER 2: Adultos ahorradores -----
c2 = pd.DataFrame({
    "edad": np.random.normal(45, 6, n//4).astype(int),
    "ingreso_anual": np.random.normal(42000, 6000, n//4),
    "gasto_score": np.random.normal(35, 8, n//4),
    "visitas_mes": np.random.normal(4, 2, n//4),
    "compras_online": np.random.normal(30, 10, n//4),
    "fidelidad": np.random.normal(8, 2, n//4)
})

# ----- CLUSTER 3: Clientes premium -----
c3 = pd.DataFrame({
    "edad": np.random.normal(38, 5, n//4).astype(int),
    "ingreso_anual": np.random.normal(85000, 9000, n//4),
    "gasto_score": np.random.normal(75, 12, n//4),
    "visitas_mes": np.random.normal(8, 3, n//4),
    "compras_online": np.random.normal(55, 12, n//4),
    "fidelidad": np.random.normal(6, 2, n//4)
})

# ----- CLUSTER 4: Clientes ocasionales -----
c4 = pd.DataFrame({
    "edad": np.random.normal(30, 7, n//4).astype(int),
    "ingreso_anual": np.random.normal(26000, 5000, n//4),
    "gasto_score": np.random.normal(20, 7, n//4),
    "visitas_mes": np.random.normal(2, 1, n//4),
    "compras_online": np.random.normal(20, 10, n//4),
    "fidelidad": np.random.normal(1, 0.5, n//4)
})

df = pd.concat([c1, c2, c3, c4], ignore_index=True)

# limpiar negativos
df[df < 0] = 0

df.to_csv("clientes_10000.csv", index=False)

print("Dataset generado correctamente")
print(df.head())
print(df.shape)
