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

#Validar entrada de usario
"""
Estas funciones validad cada entrada de datos: string no vacíos, opciones válidas, número flotate mayor que un mínimo,
entero mayor que un minimo
"""

def input_opcion(texto, opciones):
    while True:
        valor = input(texto).strip()
        if valor in opciones:
            return valor 
        else:
            print("Opcion inválida. Opciones validas: ",opciones)

def input_no_vacio(texto):
    while True:
        valor = input(texto).strip()
        if valor:
            return valor
        print("No puede estar vacío.")


def input_float(texto, minimo=None):
    while True:
        try:
            valor = float(input(texto))
            if minimo is not None and valor < minimo:
                print(f"Debe ser mayor o igual a {minimo}")
            else:
                return valor
        except ValueError:
            print("Debe ser un número")

def input_int(texto, minimo=None):
    while True:
        try:
            valor = int(input(texto))
            if minimo is not None and valor < minimo:
                print(f"Debe ser mayor o igual a {minimo}")
            else:
                return valor
        except ValueError:
            print("Debe ser un número")

def crear_producto(inventario):
    print("\n--- Crear Producto ---")
    categorias = ["Celular", "Laptop", "Tablet"]

    nuevo_id = max([p["id"] for p in inventario], default=0) + 1

    nombre = input_no_vacio("Nombre: ")
    marca = input_no_vacio("Marca: ")
    categoria = input_opcion("Categoría (Celular, Laptop, Tablet): ", categorias)
    precio = input_float("Precio (>0): ", minimo=0.01)
    stock = input_int("Stock (>=0): ", minimo=0)

    producto = {
        "id": nuevo_id,
        "nombre": nombre,
        "marca": marca,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }
    inventario.append(producto)
    print("Producto agregado con éxito!")

def buscar_por_id(invetario, id_producto):
    invetario_ordenado = sorted(invetario, key=lambda p: p["id"])
    izqueirda = 0
    derecha = len(invetario_ordenado) - 1

    while izqueirda <= derecha:
        medio = (izqueirda + derecha) // 2
        producto = invetario_ordenado[medio]

        if producto["id"] == id_producto:
            return producto
        elif producto["id"] < id_producto:
            izqueirda = medio + 1
        else:
            derecha = medio - 1
    return None

def eliminar_producto(invetario):
    print("\n--- Eliminar prducto ---")
    id_prodcuto = input_int("Ingresa el ID del producto a eliminiar: ")
    prodcuto = buscar_por_id(invetario, id_prodcuto)
    if not prodcuto:
        print("Producto no encontrado.")
        return
    invetario.remove(prodcuto)
    guardar_inventario(invetario)
    print("Producto eliminado con éxito")

"""
Pull Request para el Jr Arturo -> Arreglar el bug de leer_productos()
    * La función debe mostrar primero la pregunta de filtrado de busqueda (linea 155)
    * La opcion de omitir debe ser la iteración de todos los productos...(linea 152/153)
    * IMPORTANTE! fixear el bug de filtrado de opciones!!!!!!!!!
"""

def leer_productos(inventario):
    print("\n--- Lista de productos ---")
    if not inventario:
        print("Inventario esta vácio")
        return
    for producto in inventario:
        print(producto)

    print("\n¿Deseas buscar por nombre, marca o categoría? (deja vacio para omitir) ")
    clave = input("Buscar: ").strip().lower()
    if clave:
        resultados = [
            p for p in inventario if
            clave in p["nombre"].lower() or
            clave in p["marca"].lower() or
            clave in p["categoria"].lower()
        ]
        if resultados:
            print(f"\nResultados de búsqueda para '{clave}': ")
            for p in resultados:
                print(p)
            else:
                print("No se enocntraron coincidencias.")

def actualizar_producto(invetario):
    print("\n--- Actualizar producto ---")
    id_producto = input_int("Ingresa el ID del producto a actualizar: ")
    producto = buscar_por_id(invetario, id_producto)
    if not producto:
        print("Producto no encontrado.")
        return
    
    print("Deja en blaco si no quieres camibar el valor.")
    nombre = input(f"Nombre [{producto['nombre']}]: ").strip()
    marca = input(f"Marca [{producto['marca']}]: ").strip()
    categorias = ["Celular", "Laptop", "Tablet"]
    categoria = input(f"Categoría [{producto['categoria']}]: ").strip()
    precio = input(f"Precio [{producto['precio']}]: ").strip()
    stock = input(f"Stock [{producto['stock']}]: ").strip()

    if nombre:
        producto["nombre"] = nombre
    if marca:
        producto["marca"] = marca
    if categoria in categorias:
        producto["categoria"] = categoria
    if precio:
        try:
            precio_f = float(precio)
            if precio_f > 0:
                producto["precio"] = precio_f
            else:
                print("Precio inválido, se mantiene el anterior.")
        except:
            print("Precio inválido, se mantiene el anterior.")
    if stock:
        try:
            stock_f = int(stock)
            if stock_f >= 0:
                producto["stock"] = stock_f
            else:
                print("stock inválido, se mantiene el anterior.")
        except:
            print("stock inválido, se mantiene el anterior.")
    guardar_inventario(invetario)
    print("Producto actualizado.")

def menu():
    inventario = cargar_inventario()
    while True:
        print("\n---- Inventario de Productos ----")
        print("1. Agregar producto")
        print("2. Listar y buscar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input_opcion("Elige una opción (1-5): ", ["1", "2", "3", "4", "5"])

        if opcion == "1":
            crear_producto(inventario)
        elif opcion == "2":
            leer_productos(inventario)
        elif opcion == "3":
            actualizar_producto(inventario)
        elif opcion == "4":
            eliminar_producto(inventario)
        elif opcion == "5":
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    menu()