"""
Supón que eres el encargado de analizar los reportes semanales de ventas de una pequeña tienda. Te entregan un archivo JSON que contiene el registro de todas las ventas de la semana, con cada venta como un diccionario que incluye:

    * id_venta (único, entero)
    * fecha (string en formato "YYYY-MM-DD")
    * producto (string)
    * cantidad (entero)
    * precio_unitario (float)
    * cliente (string)

Tu tarea es crear un programa de análisis con un menú de opciones que permita:

    1- Calcular y mostrar el total de ventas ($) por día.
    2- Mostrar el producto más vendido de la semana.
    3- Mostrar la lista de clientes frecuentes (más de 2 compras en la semana).
    4- Buscar y mostrar todas las ventas de un día específico (por fecha ingresada).
    5- Salir del programa.

Requisitos:

    * El archivo se llama ventas.json.
    * Usa funciones y bucles.
    * Valida entradas donde sea necesario.
    * El programa debe ser claro, útil y demostrar organización.
    * Bonus: Muestra los resultados en forma tabulada (puedes usar la librería estándar tabulate).
"""

import json

def cargar_ventas():
    try:
        with open("ventas.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("No se encontró el archivo ventas.json")
        return []

def total_ventas_por_dia(ventas):
    pass

def producto_mas_vendido(ventas):
    pass

def clientes_frecuentes(ventas):
    pass

def buscar_ventas_por_fecha(ventas):
    pass

def menu():
    ventas = cargar_ventas()
    if not ventas:
        print("No hay datos de ventas.")
        return
    
    while True:
        print("\n--- Analizador de Ventas Semanales ---")
        print("1. Total de ventas por día")
        print("2. Producto más vendido de la semana")
        print("3. Clientes frecuentes (más de 2 por semana)")
        print("4. Buscar ventas por fecha")
        print("5. Salir")

        opcion = input("Seleccione una opción (1 - 5): ").strip()
        if opcion == "1":
            total_ventas_por_dia(ventas)
        elif opcion == "2":
            producto_mas_vendido(ventas)
        elif opcion == "3":
            clientes_frecuentes(ventas)
        elif opcion == "4":
            buscar_ventas_por_fecha(ventas)
        elif opcion == "5":
            print("¡Hasta Luego!")
            break
        else:
            print("Opción invalida")

if __name__ == "__main__":
    menu()