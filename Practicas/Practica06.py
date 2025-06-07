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
    3- Mostrar la lista de clientes frecuentes (más de 5 compras en la semana).
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
from collections import defaultdict, Counter

def cargar_ventas():
    try:
        with open("ventas.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("No se encontró el archivo ventas.json")
        return []

def total_ventas_por_dia(ventas):
    totales = defaultdict(float)
    for venta in ventas:
        fecha_por_dia = venta["fecha"]
        total_venta = venta["cantidad"] * venta["precio_unitario"]
        totales[fecha_por_dia] += total_venta
    
    print("\nTotal de ventas por día: ")
    print("{:<12} {:>12}".format("Fecha", "Total ($)"))
    print("-" * 25)
    for fecha, total, in sorted(totales.items()):
        print("{:<12} {:>12.2f}".format(fecha, total))
    

def producto_mas_vendido(ventas):
    conteo = Counter()
    for venta in ventas:
        producto = venta["producto"]
        conteo[producto] += venta["cantidad"]

    if conteo:
        producto, cantidad = conteo.most_common(1)[0]
        print(f"\nProducto más vendido: {producto} ({cantidad} unidades)")
    else:
        print("No hay ventas registradas.")

def clientes_frecuentes(ventas):
    conteo_clientes = Counter()
    for venta in ventas:
        cliente = venta["cliente"]
        conteo_clientes[cliente] += 1
        frecuentes = [cliente for cliente, veces in conteo_clientes.items() if veces > 5]
    # se itera en los frecuentes
    if frecuentes:
        print("Clientes frecuentes: ")
        print("-" * 26)
        for cliente in frecuentes:
            print("-", cliente)
        print("-" * 26)
    else:
        print("No hay mas clientes")


def buscar_ventas_por_fecha(ventas):
    fecha = input("Ingrese la fecha a buscar (YYYY-MM-DD): ").strip()
    encontrados = [v for v in ventas if v["fecha"] == fecha]
    if encontrados:
        print(f"\nVentas de día {fecha}: ")
        print("{:<5} {:<10} {:<10} {:<8} {:<8} {:<11}".format("ID", "Productos", "Cliente", "Cant.", "P. Unitario", "Total"))
        print("-" * 55)
        for v in encontrados:
            total = v["cantidad"] * v["precio_unitario"]
            print("{:<5} {:<10} {:<10} {:<8} {:<8.2f} {:<13.2f}".format(v["id_venta"], v["producto"], v["cliente"], v["cantidad"], v["precio_unitario"], total))
    else:
        print("\nNo hay ventas registradas para esa fecha")
    

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
