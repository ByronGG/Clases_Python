import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

N = 5000

customer_id = rng.integers(1000, 5000, size=N)
age = rng.integers(18, 70, size=N)
visits_per_month = rng.integers(1, 20, size=N)

# Patrones realistas de consumo
burgers = rng.poisson(lam=2, size=N)
pizza = rng.poisson(lam=3, size=N)
tacos = rng.poisson(lam=4, size=N)
drinks = rng.poisson(lam=5, size=N)
desserts = rng.poisson(lam=1, size=N)

# Gasto promedio influenciado por consumo
avg_ticket = (
    burgers * 60 +
    pizza * 80 +
    tacos * 30 +
    drinks * 25 +
    desserts * 40 +
    rng.normal(50, 20, size=N)
).clip(50, None)

total_items = burgers + pizza + tacos + drinks + desserts

# Categoría favorita
categories = np.array(["burgers", "pizza", "tacos", "drinks", "desserts"])
favorite_category = categories[
    np.argmax(
        np.vstack([burgers, pizza, tacos, drinks, desserts]).T,
        axis=1
    )
]

df = pd.DataFrame({
    "customer_id": customer_id,
    "age": age,
    "visits_per_month": visits_per_month,
    "avg_ticket": avg_ticket.round(2),
    "burgers": burgers,
    "pizza": pizza,
    "tacos": tacos,
    "drinks": drinks,
    "desserts": desserts,
    "total_items": total_items,
    "favorite_category": favorite_category
})

df.to_csv("food_store_purchases.csv", index=False)

print("✅ Dataset generado: food_store_purchases.csv")
print(df.head())
