# Validación cruzada

"""
    La cross-validation, CV es una técnica para evaluar qué tan bien generaliza un modelo a datos que no ha visto, usando todo el dataset de forma inteligente, no solo un úncio split

    Train/test simple
    80% entrenamiento
    20% test

        1. El resultado depende del azar (cómo cayo el split)
        2. Usas menos datos para entrenar
        3. Puede elegir un modelo 'bueno por suerte'

    Validación cruzada
        1. Usa TODOS LOS DATOS
        2. Reduce la varianza de la evalación
        3. Da un estimación más estable y confiable

    Imagia que tu dataset sea un pastel. En vez de quitar una sola rebanada para probar...
    Cortas el pastel en varias rebnanadas y:
        * Cada rebanada se usa una vez como test
        * Lada demás se usan como train
    
    K-Fold Cross-Validation
    ¿Cómo funciona un K-Fold?
        1. Divides el dataset en K partes (folds)
        2. Repeticienes:
            * 1 fold = test
            * K-1 folds = train
        3. Repites hasta que todos fueron test una vez
        4. Promedias los resultados

    Fold 1 -> test | resto -> train
    Fold 2 -> test | resto -> train
    Fold 3 -> test | resto -> train
    Fold 4 -> test | resto -> train
    Fold 5 -> test | resto -> train

    Restuldato final:
        score = promedio(score_1, score_2...score_5)

    ¿Por qué el promedio importa?
    Porque: Un fold puede ser fácil
    Porque: Otro fold puede ser dicil
    El promedio refleja comportamiento real, no suerte!

    Ejemplo:
    Supón estos accuracies:
    [0.81, 0.79, 0.83, 0.80, 0.78]
    Resulto CV:
    mean = 0.802
    std = 0.017

    Modelo estable
    No depende de un solo split

    TIPOS DE CROSS-VALIDATION (CV)
        * K-Fold
        * Stratified k-fold
        * Leave-One-Out (LOOCV) *
        * Time Series Split

---------------------------------TEORIA Buena practicas------------------------------------------------
    Validación cruzada + Pipeles
    X_scaled = scaler.fit_tranform(X)
    cross_val_score(model, X_scaled, y)

    ERROR!!! -> Estás usando información del test! ANTES DE VALIDAR!!!!

    FORMA CORRECTA!!!

    from sklearn.pipeline import Pipeline
    from sklearn.model_selection import cross_val_score

    pipe = Pipeline([
            ("scaler", StanderScaler()),
            ("model", LogisticRegression()
        )])

    scores = cross_val_score(pipe, X, y, cv=5)

    Cada fold aprender su propio "sclaer"
    No hay fuga de datos!
---------------------------------TEORIA------------------------------------------------

    REGLA DE ORO!!!

    TRAIN -> Validación cruzada -> elegir modelo
    TEST -> SOLA UNA VEZ al final

    Métricas + Validación cruzada
    Problema                                Métrica
    Clasificación Balanceada                accuracy
    Clases desbalanceadas                   f1, roc_auc
    Regresión                               neg_mean_squared_error * 
    Regresión                               r2 *

    Errores comunes (muy importantes)
        * Usar CV despues de ver el test
        * No usar Stratified K-Fold en clasificación
        * Escalar datos fuera del pipeline
        * Mezclar series temporales
        * Interpretar un solo fold

    ¿Cuántos folds usar? * Invetigar Tarea * 
    Dataset                 K recomendados
    Muy pequeño(<1k)        5 - 10
    Mediano                 5
    Grande                  3 - 5
    Series de tiempo        TimeSeriesSplit
"""

import numpy as np
import pandas as pd

# Dataset simple
df = pd.DataFrame({
    "X": [1,2,3,4,5,6,7,8,9,10],
    "y": [0,0,0,0,1,1,1,1,1,1]
})

X = df[["X"]]
y = df[["y"]]

from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

kf = KFold(n_splits=5, shuffle=True, random_state=42)
model = LogisticRegression()

fold_results = []

for fold, (train_idx, test_idx) in enumerate(kf.split(X), start=1):
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    fold_results.append(acc)

    print(f"\n Fold {fold}")
    print("Train indices ", train_idx)
    print("Test indices ", test_idx)
    print("Accuracy ", round(acc, 3))
