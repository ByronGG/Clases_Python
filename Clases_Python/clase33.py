# Random Forest (RF)

"""
    Random Forest es un algoritmo de ML supervisado basado en ensambles.

    Ensenmble = conbiar muchos modelos simepres y débiles -> para crear un modelo más fuerte
    RF crea muchos árboles de decisión (DT Deccion Trees), pero no totam la mismo info para cada árbol, sino que:

        1. Toma diferentes muestras de dataset
        2. toma diferentes subset para cada split
            Vota/promedia el resultado final
        Es decir:
            * diferntes árboles -> diferntes puntos vista del mismo problema
            * eso reduce overfitting brutal que tiene DT están solo

    ¿Para qué sirve?
    Clasificación           ->          fraude / no fraude, spam / no spam
    Regresión               ->          predicción de presios de obj, volumentes de venta, tiempo estiamdo de entraga

    RF se usa muchisimo en industria porque funciona muy bien aunque los datos no sean perfectos

    Caso real y muy comunes:
        * Fintech -> detectar fraude transaccional
        * Salud -> prediccioón diagnóstica
        * Economia -> predicción de ventas de un producto
        * Marketing -> chrun 
        * Meterologia -> predicción climatica

    Comparación vs otras técnicas

    Técnica                     Mejor en                Peor en vs RF
    Decision Tree               Interpretación          Overtiffing masivo
    Logistic Regression         Velocidad               RF captutra de relaciones no lineales
    XGBoost                                             Más facil y rapido para aprender ML
    NN/Deep Learning            multimodal              Computacinal Visual

"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score, roc_auc_score

# 1) Dataset
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
Y = pd.Series(data.target, name="target")

# 2) Train / Test Split (estratificado para mantener proporciones de clases)
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42, stratify=Y
)

# 3) Entranar RF
rf = RandomForestClassifier(
    n_estimators=300,       # más árboles = más robusto (hasta cierto punto)
    max_depth=None,         # sin límite, deja que el bosque controle el overfitting
    min_samples_leaf=2,     # hojas con al menos 2 muestras (suaviza un poquito)
    max_features="sqrt",    # típico en claficiacion
    n_jobs=1,               # usa todos los cores
    random_state=42
)

"""
    * n_estimators = cuántos árboles usa (más = más potencia, más tiempo)
    * max_depth = hasta qué profundidad puede crecer cada árbol
    * max_features = cuántas columnas se usan aleatoriamente por árbol
    * min_samples_split y min_samples_leaf = controlan overfitting
"""

rf.fit(X_train, Y_train)

# 4) Métricas en test
y_pred = rf.predict(X_test)
y_proba = rf.predict_proba(X_test)[:,1]

print("Accuracy: ", round(accuracy_score(Y_test, y_pred), 4))
print("Balanced Accuracy: ", round(balanced_accuracy_score(Y_test, y_pred), 4))
print("F1 (class 1): ", round(f1_score(Y_test, y_pred), 4))
print("ROC  AUC: ", round(roc_auc_score(Y_test, y_proba), 4))