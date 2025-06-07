"""
Crear un script que lea un archivo CSV con calificaciones de alumnos y genere un resumen estadístico y reportes simples, incluyendo:

    * Promedio general de cada alumno
    * Promedio por materia
    * Alumnos con calificación reprobatoria (< 6)
    * Alumno con mejor promedio
    * Gráfica de distribución de calificaciones

    ----------------------------------------------------------------------------------------------------------------------
    Habilidades a calificar!!

    * Lectura de archivos con csv.DictReader.
    * Manipulación de listas y diccionarios.
    * Cálculo de promedios y filtros con condicionales.
    * Visualización básica con matplotlib.
"""

import csv
import matplotlib.pyplot as ptl

datos = "calificaciones_ampliado.csv" #Ruta relativa del CSV

# Leer datos
alumnos = [] # Lista vacia de los alumnos
with open(datos, newline='', encoding='utf-8') as f:
    lector = csv.DictReader(f) # el DictReader es para leer archivos Excel 
    for fila in lector:
        alumno = {"nombre": fila["nombre"]}
        materias = ["matematicas", "espanol", "ciencias", "historia"] # Lista representa los encabezados del archivo
        calificaciones = [int(fila[m]) for m in materias]
        alumno["calificaciones"] = dict(zip(materias, calificaciones))
        alumno["promedio"] = sum(calificaciones) / len(calificaciones)
        alumnos.append(alumno)

print(alumnos)
# 1. Promedio por alumno

# 2. Promedio por materia

# 3. Alumnos Reprobados
print("\n === Alumnos reprobador (promedio < 6) === ")
for a in alumnos:
    if a["promedio"] < 6:
        print(f"{a["nombre"]} {a["promedio"]:.2f}")

# 4. Alumno con mejor promedio

# 5. Grafico de barras