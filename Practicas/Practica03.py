"""
Crea un pequeño sistema que permita registrar estudiantes, asignarles calificaciones y calcular estadísticas básicas.
---------------------------------------------------------------------------------------------------------------------------
Requisitos:
Crea una clase Estudiante que tenga como atributos:
    nombre (string)
    edad (int)
    calificaciones (lista de floats)

Implementa en la clase Estudiante:

    Un método agregar_calificacion(self, calificacion) que agregue una nueva calificación si está entre 0 y 10.
    Una propiedad promedio que calcule el promedio de calificaciones.
    Un método estado(self) que regrese "Aprobado" si el promedio es mayor o igual a 6.0, de lo contrario "Reprobado".

Crea una función filtrar_aprobados(estudiantes) que reciba una lista de objetos Estudiante y devuelva una lista con los nombres de los estudiantes aprobados, usando lista por comprensión.

Usa bucles para:

    Crear al menos 3 estudiantes y agregarles calificaciones de forma dinámica.
    Mostrar el nombre, promedio y estado de cada estudiante.

Ejemplo esperado de salida

Nombre: Ana, Promedio: 8.5, Estado: Aprobado
Nombre: Luis, Promedio: 5.3, Estado: Reprobado
Nombre: Marta, Promedio: 7.0, Estado: Aprobado

Estudiantes aprobados: ['Ana', 'Marta']
"""


class Estudiante():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = []

    # Metodo agregar nueva calificacion
    def agregar_calificacion(self, calificacion):
        if 0 <= calificacion <= 10: 
            self.calificaciones.append(calificacion)
        else:
            print(f"Calificación inválida para {self.nombre}: {calificacion}")

    @property
    def promedio(self):
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones) # califaciones = [10.0, 7.0, 8.5]

    def estado_estudiante(self):
        return "Aprobado" if self.promedio >= 6.0 else "Reprobado"

def filtrar_aprobados(estudiantes):
    return [e.nombre for e in estudiantes if e.promedio >= 6.0]

# Programa principal
estudiantes = []
cantidad = int(input("¿Cuantos estudiantes quieres registrar? "))

for i in range(cantidad):
    print(f"\nEstudiante {i+1}: ")
    nombre = input("Nombre: ") 
    edad = int(input("Edad:"))
    estudiante = Estudiante(nombre, edad)

    n_califs = int(input(f"¿Cuantas calificaiones quieres ingresar para {nombre}? "))
    for j in range(n_califs):
        while True:
            try:
                calif = float(input(f"Calificaión #{j+1}: "))
                estudiante.agregar_calificacion(calif)
                break
            except ValueError:
                print("Ingresa un número válido.")

    estudiantes.append(estudiante)

# Mostrar resultados
print("\nResultados: ")
for e in estudiantes:
    print(f"Nombre: {e.nombre}, Promedio: {e.promedio:.1f}, Estado: {e.estado_estudiante()}")

# Mostrar aprobados
aprobados = filtrar_aprobados(estudiantes)
print(f"\nEstudiantes aprobados: {aprobados}")