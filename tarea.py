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
import matplotlib.pyplot as plt

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
for i in alumnos:
    print(f"{i['nombre'], i['promedio']}")
        





# 2. Promedio por materia
sumadematerias = dict.fromkeys(materias, 0)
for k in alumnos:
    for m in materias:
        sumadematerias[m] += k["calificaciones"][m]
for m in materias:
    promedio = sumadematerias[m] / len(alumnos)
    print(f"{m}: {promedio:.2f}")


# 3. Alumnos Reprobados
print("\n === Alumnos reprobador (promedio < 6) === ")
for a in alumnos:
    if a["promedio"] < 6:
        print(f"{a["nombre"]} {a["promedio"]:.2f}")
        print("tas tronado")


# 4. Alumno con mejor promedio
mejorpromedio = 0
mejor_nombre = "pepe"

for z in alumnos:
    if a["promedio"] > mejorpromedio:
        mejor_promedio = z["promedio"]
        mejor_nombre = z["nombre"]

print("El alumno con mejor promedio es", mejor_nombre, mejor_promedio)



# 5. Grafico de barras
nombres = [a["nombre"] for a in alumnos]
promedios = [a["promedio"] for a in alumnos]
plt.bar(nombres, promedios)
plt.xlabel("Alumno")
plt.ylabel("Promedio")
plt.title("Promedio por Alumno")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()