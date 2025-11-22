# Regresión Logística

"""
    La Regresión logística es uno de los modelos más importantes en toda la historia del ML. Se utilizan en bancos, aseguradoras, marketing, gobiernos y también en la base matemática de las neuronales modernas.

    ¿Qué es la Regresión logística?
    Es un modelo que sirve para clasificación binaria:
        * Sí / No
        * 0 / 1
        * Fraude / No Fraude
        * Spam / No spam
        * Autorizado / No autorizado
        * Efermo / Sano

    Intución antes de matemática
    La regresión logística "no intenta" predecir directamente un 0 o 1.
    En lugar de eso:
        Predice una probabilidad
        "La probabilidad de que el cliente abandode un servicio es 0.82"
        * si prob > 0.5 -> clase = 1
        * si prob <= 0.5 -> clase = 0
        Esto lo convierte en un modelo "suave", no rígido como un árbol

    ¿Por qué no sirve la regresión lineal para clasificación?
    Si intentántamo usar regresión lineal para predecir 0/1, habría problemas:
        * Podría dar valores como 1.8, -0.3 (inválidos como probabilidad)
        * No separa bien en problemas no lineales
        * No modela la relación entre variables y probabilidad de forma correcta

    La función sigmoide
    La idea clase es esta:

        La sigmoide toma cualquier número y lo transforma en una probabilidad entre 0 y 1.
            Fórmula
                σ(z)= 1/1+e^-z

        Si z -> grande -> σ(z) -> 1
        Si z -> negativo -> σ(z) -> 0

        ¿Qué es z?
        Es una combianación lineal de las variables
            z = w1x1 + w2x2 + ... + wnxn + b
        Con regresión lineal:
                y = z
        Con regresión logística
                p = σ(z)

        Interpretación real de Data Science
        Si tenemos un modelo como este:

                p = σ(0.8 * edad + 1.2 * deudas - 3.1)

        Entonces:
            * coeficiente positivo -> aumenta la probilidad de 1
            * ceoficiente negativo -> disminuye la probabilidad
            * deuda = 1.2 -> mayor impacto
            * edad = 0.8 -> menor impocato comparado con deudas

            Regresión logística = interpretación directa de efectos

        Función de pérdida: Log-Loss
        La pérdida del modelo es:

                -[y log(p) + (1-y) log(1-p)]

        Esto penaliza fuertemente:
            * predecir probabilidad alta cuando debería ser baja
            * y viceversa
        Es la misma pérdida que usa las redes neuronales de clasificación binaria

        El modelo prodecir probabilidad.
        Luego elegimos un umbral (normalmente 0.5)

        prob > 0.5 -> 1
        prob <= 0.5 -> 0
        Por en negocio peude mover el umbral:
            * 0.3 para detectar fraude (permite más alertas)
            * 0.7 para prestamos (permite menos falsos positivos)

        -------------------------------------------------------------
        EJEMPLO VIDA REAL
        
        Tenemos clietnes con:
            * edad
            * gasta mensual
            * números de llamadas a soporte
            * historial de pago

            Qureremos predecir ¿se dará de baja?
            prob = modelo.predict_proba(cliente)

            Si = 0.78 -> mando ofera de retención
            Si = 0.12 -> no necesito actuar.

        -------------------------------------------------------------
        EJEMPLO VIDA REAL HYTECK

        Tenemos clientes:
            * nombre empresa
            * fecha contrato (inicio/actual)
            * tipo empresa
            * ubicación
            * prom x contrato

            Queremos predecir ¿Cuanto gastará en su proximo pedido?
            prob = modelo.predict_proba(cliente)

            Si = 0.57 -> TAREA
            Si = 0.89 -> Producción lista
            Si = 0.13 -> Dia libre
"""

import numpy as np
import pandas as pd

# Para reproducibilidad
rng = np.random.default_rng(42)
n = 2000  # número de clientes

# 1) Generamos las features (características)
edad = rng.integers(18, 70, n)                 # 18 a 69 años
ingreso_mensual = rng.integers(1500, 9000, n)  # $1,500 a $9,000 MXN
meses_cliente = rng.integers(1, 60, n)         # 1 a 59 meses como cliente
llamadas_soporte = rng.integers(0, 10, n)      # 0 a 9 llamadas al mes
historial_pago = rng.integers(0, 2, n)         # 0 = malo, 1 = bueno
plan_premium = rng.integers(0, 2, n)           # 0 = básico, 1 = premium

# 2) Definimos una función sigmoide
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 3) Creamos una "puntuación de churn" basada en reglas semi-realistas
#    (esto simula el comportamiento de la vida real)
score = (
    0.05 * (edad - 40) +             # más edad, un poco más de riesgo
    0.001 * (ingreso_mensual - 4000) * -1 +  # más ingreso, MENOS riesgo
    0.15 * (llamadas_soporte - 3) +  # más llamadas a soporte, más riesgo
    -1.2 * historial_pago +          # buen historial reduce riesgo
    0.4 * (1 - plan_premium) +       # plan básico, un poco más de riesgo
    0.5 * (meses_cliente < 6) +      # clientes nuevos, más riesgo
    rng.normal(0, 0.8, n)            # ruido gaussiano para hacerlo realista
)

# 4) Convertimos esa score en probabilidad de churn usando sigmoide
churn_prob = sigmoid(score)

# 5) Generamos la variable objetivo (y) a partir de la probabilidad
churn = rng.binomial(1, churn_prob)

# 6) Construimos el DataFrame
df = pd.DataFrame({
    "edad": edad,
    "ingreso_mensual": ingreso_mensual,
    "meses_cliente": meses_cliente,
    "llamadas_soporte": llamadas_soporte,
    "historial_pago": historial_pago,
    "plan_premium": plan_premium,
    "churn": churn
})

print(df.head())
print("\nDistribución de churn:")
print(df["churn"].value_counts())


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Features (X) y target (y)
X = df[["edad", "ingreso_mensual", "meses_cliente", "llamadas_soporte",
        "historial_pago", "plan_premium"]]
y = df["churn"]

# Train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Pipeline con escalado + regresión logística
from sklearn.pipeline import make_pipeline
modelo = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)

modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nReporte de clasificación:\n", classification_report(y_test, y_pred))
