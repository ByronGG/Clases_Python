from __future__ import annotations
# Pipelines

"""
    Un pipelines es una cadena de etapas conectadas que toman información "cruda" (raw), la preparan, la mueven a un lugar confiable, y la dejan lista para consumo. La idea central es: automatizar y estandarizar un proceso repetible para que sea confiable, trazable y escalable.

    ¿Para qué sirve un pipeline?
        * Repetibilidad: que el proceso salga igual hoy y mañana.
        * Calidad: detectar datos rotos antes de que causen decisiones/modelos malos.
        * Escalabilidad: pasar de "un excel" a millones de filas sin rehacer todo.
        * Trazabilidad: saber de dónde salió cada dato y qué le hiciste.
        * Velocidad: reducir tiempo de preparar datos/entrenar/desplegar.
        * Mantenibilidad: cambios controlados, versinados y probados.

    Tipo comunes
        * ETL: Extract -> Transform -> Load
        * ELT: Extract -> Load -> Transform
        * Pipeline de ML: Datos -> feactures -> entrenamiento -> validación -> registro del modelo -> despliegue -> monitoreo.

    ETAPAS -> RECOPILACIÓN, TRANFORMACIÓN, ALMACENAMIENTO Y GESTIÓN

    1) Recopilación (Ingesta / Extract)
        Aquí defines qué datos entran, de dónde, cada cuánto, y qué garantías.

        - Fuentes típicas: BD (SQL/NoSQL), archivos (CVS/Excel), APIs (CRM, ERP), logs, sensores, eventos.

    2) Tranformación (Clean/Normalize/Enrich)
        Es donde conviertes datos crudos en datos útiles y consisntes.
        
        Transformaciones típicas
            - Limpieza: nulos, valores fuera de rango, corrección de tipos, trimming de strings.
            - Normalización: fechas en UTC, unidades (kg vs lb), categorías estandarizadas.
            - Deduplicación: reglas por llave o por similitud.
            - Uniones y enriquecimiento: joins con catálogos, cálculo de métricas.
            - Agregaciones: por día/semana, por cliente, por región.
            - Feature engineering (ML): one-hot, escalado, binning, embeddings, etc.
    
    3) Almacenamiento (Load/Persistencia)
        Define dónde vive cada etapa y con qué objetivo.

        Almacenes típicos
            - Data lake: barato, flexible
            - Data werehouse: consultas rápidas y SQL
            - Base transaccional: para apps
            - Feature store: feactures consistentes entre entrenamiento e inferencia
            - Cache/serving store: baja latencia

    4) Gestión (Orquestación, Observabilidad, Gobernanza)
        Esta parte es la diferencia entre "un script" y "un pipeline profesional"

        Orquestación
            - Programación y dependencias: “primero ingesta, luego transformaciones, luego cargas”.
            - Reintentos, alertas, ejecución paralela, ventanas de tiempo, backfills.

        Observabilidad
            - Logs: qué pasó en cada paso.
            - Métricas: tiempos, filas procesadas, % errores, costo.
            - Alertas: fallos, datos fuera de rango, retrasos (SLA).
            - Lineage: de qué fuente vino cada dato y a qué tablas impactó.

        Gobernanza y seguridad
            - Control de acceso (quién puede ver qué).
            - Catálogo de datos (descubrimiento y documentación).
            - Auditoría: quién cambió una transformación y cuándo. 
            - Privacidad: enmascarado/tokenización de datos sensibles.

        Pruebas y CI/CD
            - Tests de transformaciones y de calidad de datos.
            - Versionado de código y configuraciones
            - Entornos: dev/staging/prod.

        --------- Ejemplo mental aplicado a tu "plataforma de órdenes de trabajo" ---------

            * Recopilacición: extraer órdenes desde la DB
            * Tranformación: estandarizas estados ("pendiente/en proceso/cerrada"), arreglas fechas,    calculas tiempo de resolución
            * Almacenamiento: guardar raw por día, y un tabla "gold" para reportes (KPIs por OT/cliente/concepto)
            * Gestión: orquestas cada noche, validas que no hay órdenes sin id/fecha, alertas sin falta de datos
"""

# ETL

"""
    Que hacer
        - Recopilación: lee un CVS "crudo"
        - Tranformación: limpiar columas, fecha, nulos, dedup, calcula métricas
        - Validación: reglas básicas de calidad
        - Almacenamiento: gurdar "silver" limpio y el "gold" agregado
        - Gestión: logs y manejo de errores
"""
import pandas as pd
from dataclasses import dataclass
import logging
from pathlib import Path

#--------------------
# 0) Gestión loggin básico
#--------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger("etl_pipeline")

@dataclass(frozen=True)
class Config:
    raw_path: Path = Path("raw_workorders.csv")
    silver_path: Path = Path("silver_workorders.parquet")
    gold_path: Path = Path("gold_kpis_by_tech.parquet")

#--------------------
# 1) Recopilación
#--------------------

def extract_raw(cfg: Config) -> pd.DataFrame:
    logger.info("EXTRACT: leyendo datos crudos desde %s", cfg.raw_path)
    df = pd.read_csv(cfg.raw_path)
    logger.info("EXTRACT: filas=%d, columas=%d", len(df), df.shape[1])
    return df

#--------------------
# 2) Tranformación 
#--------------------

def tranform(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("TRANFORM: Inicio")

    # Normalizar nombres de columnas (opcional)
    df = df.copy()
    df.columns = [c.strip().lower() for c in df.columns]

    # Lipiar strings
    for col in ["status", "technician", "priority"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.lower() # CASTEO

    # Parsear fechar (si existen)
    for col in ["start_date", "end_date"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce") #Si no existe alguna fecha => NaT

    # Reglas simple de imputación
    # - Prioridad vacía -> "Media"
    if "priority" in df.columns:
        df["priority"] = df["priority"].replace({"nan":None})
        df["priority"] = df["priority"].fillna("media")

    # Quitar duplicados por id si existen
    if "workorder_id" in df.columns:
        before = len(df)
        df = df.drop_duplicates(subset=["workorder_id"], keep="last")
        logger.info("TRANFORM: dedup por workorder_id: %d -> %d", before, len(df))

    # Métrica: duración (días) sin fechas 
    if {"start_date", "end_date"}.issubset(df.columns):
        df["duration_days"] = (df["end_date"] - df["start_date"]).dt.total_seconds() / 86400

    logger.info("TRANFORM: fin (filas=%d)", len(df))   
    return df

#--------------------
# 3) Validación / calidad
#--------------------

def validate(df: pd.DataFrame) -> None:
    logger.info("Validate: inicio")

    if "workorder_id" in df.columns:
        if df["workorder_id"].isna().any():
            raise ValueError("Validate: Hay workorder_id nulos")
        
    if "status" in df.columns:
        allowed = {"open", "in_progress", "closed", "cancelled"}
        bad = set(df["status"].dropna().unique()) - allowed 
        if bad:
            raise ValueError("Validate: status inválidos {bad}")
        
    if {"start_date", "end_date"}.issubset(df.columns):
        invalid = df["end_date"].notna() & df["start_date"].notna() & (df["end_date"] < df["start_date"])
        if invalid.any():
            raise ValueError("VALITE: Hay registros con end_date < start_date")
        
    logger.info("VALIDATE: OK")

#--------------------
# 4) Almacemainto (Load)
#--------------------
def load_silver(df: pd.DataFrame, cfg: Config) -> None:
    logger.info("LOAD(Silver): guardado %s", cfg.silver_path)
    df.to_parquet(cfg.silver_path, index=False)

def build_gold(df_silver: pd.DataFrame) -> pd.DataFrame:
    logger.info("GOLD: contruyendo KPIs por ténico")

    # Ejemplo: KPIs por ténico
    # - total ordénes
    # - % cerradas
    # - promedio duración
    g = df_silver.copy()

    if "technician" not in g.columns:
        g["technician"] = "unknown"
    if "status" not in g.columns:
        g["status"] = "unknown"
    if "duration_days" not in g.columns:
        g["duration_days"] = pd.NA

    gold = (
        g.groupby("technician", dropna=False)
        .agg(
            total_orders = ("technician", "size"),
            closed_rate = ("status", lambda s: (s == "closed").mean()),
            avg_duration_days = ("duration_days", "mean")
        )
        .reset_index()
        .sort_values("total_orders", ascending=False)
    )
    return gold

def load_gold(df_gold: pd.DataFrame, cfg: Config) -> None:
    logger.info("LOAD(Gold): guardado %s", cfg.gold_path)
    df_gold.to_parquet(cfg.gold_path, index=False)

#--------------------
# 5) Orquestación del pipeline
#--------------------

def run_pipeline(cfg: Config) -> None:
    try:
        df_raw = extract_raw(cfg)
        df_silver = tranform(df_raw)
        validate(df_silver)
        load_silver(df_silver, cfg)

        df_gold = build_gold(df_silver)
        load_gold(df_gold, cfg)

        logger.info("PIPELINE: terminado con éxito")
    except Exception as e:
        logger.exception("PIPELINE: falló | %s", e)
        raise

if __name__ == "__main__":
    run_pipeline(Config())