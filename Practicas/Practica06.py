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
