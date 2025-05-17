"""
Crea una aplicación en Python que gestione un inventario de productos electrónicos (por ejemplo, celulares, laptops, tablets). Toda la información se almacenará en un archivo JSON. El programa debe permitir al usuario realizar las siguientes operaciones:

    -Crear producto: Permite agregar un nuevo producto al inventario.
    -Leer productos: Permite listar todos los productos o buscar por nombre, marca o categoría.
    -Actualizar producto: Permite modificar los datos de un producto existente.
    -Eliminar producto: Permite eliminar un producto del inventario.

    Requisitos:

Cada producto debe tener al menos estos campos:

    id (numérico, único)
    nombre (string)
    marca (string)
    categoria (string: “Celular”, “Laptop”, “Tablet”)
    precio (float > 0)
    stock (entero >= 0)

El archivo JSON se llamará inventario.json.
Implementa validaciones de entrada para que:

    No se ingresen datos vacíos o no válidos.
    El precio sea mayor a 0.
    El stock no sea negativo.
    La categoría solo pueda ser una de las permitidas.

Cada operación CRUD debe confirmarse mostrando el resultado.
El sistema debe permitir realizar varias operaciones hasta que el usuario decida salir.
"""

import json
import os

def cargar_inventario():
    if not os.path.exists("inventario.json"):
        return []
    with open("inventario.json", "r", encoding="utf-8") as f:
        return json.load(f)
    
def guardar_inventario(invetario):
    with open("inventario.json", "w", encoding="utf-8") as f:
        json.dump(invetario, f, indent=2, ensure_ascii=False)

#Validadr entrada de usario

def input_opcion(texto, opciones):
    while True:
        valor = input(texto).strip()
        if valor in opciones:
            return valor 
        else:
            print("Opcion inválida. Opciones validas: ",opciones)