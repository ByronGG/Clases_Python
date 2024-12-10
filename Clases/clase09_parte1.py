# XML

"""
XML: (eXtensiidble Markup Language) es un formato utilizado para almacenar y transportar datos estructurados
"""
# Etiquetda <user></user>
# Clase(Obj) <user id="1"> </user>

import xml.etree.ElementTree as ET
import json
from datetime import datetime
import requests


xml_data = """
<data> 
    <user id="1"> 
        <name>Arturo</name>
        <age>18</age>
        <email>arturo_slp@gmail.com</email>
    </user>
    <user id="2">
    <name>Luis</name>
        <age>24</age>
        <email>sa.luis@gmail.com</email>
    </user>
    <user id="3">
    <name>Pepe</name>
        <age>20</age>
        <email>pepe1@gmail.com</email>
    </user>
</data>
"""

# Parsear el XML
root = ET.fromstring(xml_data)

# Acceder a los elementos
for user in root.findall('user'):
    user_id = user.get('id') # Atributos de la clase ID
    name = user.find('name').text # Texto dentro de la etiqueta
    age = user.find('age').text # Texto de la etiqueta age
    email = user.find('email').text
    print(f"ID: {user_id}, Name: {name}, Age: {age}, Email: {email}")

# Crear la raíz
new_root = ET.Element("data")

# Agregar elementos
user1 = ET.SubElement(new_root, "user", id="1")
ET.SubElement(user1, "name").text = "Roberto"
ET.SubElement(user1, "age").text = "21"
ET.SubElement(user1, "email").text = "roberto@gmail.com"

user2 = ET.SubElement(new_root, "user", id="2")
ET.SubElement(user2, "name").text = "Jose"
ET.SubElement(user2, "age").text = "20"
ET.SubElement(user2, "email").text = "jose@gmail.com"

user3 = ET.SubElement(new_root, "user", id="3")
ET.SubElement(user3, "name").text = "Pablo"
ET.SubElement(user3, "age").text = "19"
ET.SubElement(user3, "email").text = "pablo@gmail.com"

# Convertir a string y guardarlo en el archivo
tree = ET.ElementTree(new_root)
tree.write("output.xml", encoding="utf-8", xml_declaration=True)

# Modificar un archivo XML
tree = ET.parse("output.xml")
raiz = tree.getroot()

# Modoficar un nodo
for user in raiz.findall("user"):
    if user.get("id") == "2":
        user.find("name").text = "Juanito"

# Guardamos los cambios
tree.write("output.xml", encoding="utf-8", xml_declaration=True)

print("--------------------JSON--------------------")

# JSON
"""
JSON represta datos como pares clave-valor (key-value) (Similar a un diccionario en Python)
y estructtas de listas anidadas. Es ideal para el alamacenamiento de datos, comunicación entre
aplicaciones (APIs) y también para configuraciones de servidores y/o frameworks
"""
# Cargar un string como si fuera un JSON
json_string = '{"name": "Arturo", "age": 18, "is_student": true}'
data =json.loads(json_string)
print(f"Nombre: {data["name"]}")

# Desde un archivo JSON
with open("example.json", "r") as file:
    data = json.load(file) # Convierte JSON a objeto Python (diccionario)
    print(data["name"]) # Acceso a datos

# Crear un JSON con código
data = {
    "name": "Reyna",
    "age": 23,
    "is_student": False
}

with open("example2.json", "w") as file:
    json.dump(data, file, indent=3) # Escribe JSON con identación

# convertir a un string JSON

new_json_string = json.dumps(data, indent=3) # Convierte un diccionar (OBJ PYTHON) a string JSON
print(new_json_string)

"""
JSON    |   Python
Object  |   dict
Array   |   list
String  |   str
int     |   int
float   |   float
true    |   True
false   |   False
null    |   None
"""

# Ordenar claves al escribir JSON
new_data = {
    "b": 2,
    "a": 1,
    "c": 3
}

json_string = json.dumps(new_data, indent=3, sort_keys=True)
print(json_string)

# Python no puede convertir cierto tipos de datos (datetime)
# Serializar objetos no compatibles
def custom_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat() # Convertir a string ISO 8601
    raise TypeError("Tipo de serializable")

time_data = {"timestamp": datetime.now()} # Diccionario (JSON OBJ)

jsonstring = json.dumps(time_data, default=custom_serializer)
print(jsonstring)

# JSON en APIs
print("-----------------------GET-----------------------")
"""
JSON es el formato más común para la comunicación entre servidores y cliente (REST APIs).
Con Python puedes trabajar fácilmente con API's usando biblotecas como "request"
Procotolo HTTP
"""

reponse = requests.get("https://jsonplaceholder.typicode.com/posts/1") # Petición HTTP metodo GET
data = reponse.json() # Convertir la respues JSON a un diccionario 
print(data["title"]) # Acceder a los datos

# Enviar datos JSON a una API

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "datos post facebook",
    "body": "ya quitaron el cambio de horario",
    "userId": 1
    }

reponse = requests.post(url, json=payload)
print(reponse.status_code) # Código de respuesta
print(reponse.json())

"""
Gestión de Inventario en una Tienda usando JSON

Diseña un programa que simule el sistema de gestión de inventario de una tienda. 
Este sistema debe manejar un archivo JSON como base de datos para el inventario y 
ofrecer las siguientes funcionalidades a través de un menú interactivo:

Mostrar productos por categoría
Permite al usuario buscar productos pertenecientes a una categoría específica del inventario.

Calcular el valor total del inventario
Calcula y muestra el valor monetario total de los productos en el inventario, 
considerando su precio y la cantidad disponible.

Encontrar productos con stock bajo
Permite al usuario buscar productos cuya cantidad en stock esté por debajo de un umbral especificado.

Agregar un nuevo producto
Permite agregar un nuevo producto al inventario con los siguientes datos:

ID único
Nombre del producto
Categoría
Precio
Cantidad en stock
Valida que el ID sea único y que los valores ingresados sean correctos.

Realizar una compra
Simula la compra de un producto especificando su ID y la cantidad deseada. Si el stock es suficiente, 
actualiza el inventario y muestra el costo total. Si no hay suficiente stock, notifica al usuario.

Salir del programa
Cierra la aplicación.
"""

# Función para cargar el archivo JSON
def load_store_data(filename):
    with open(filename, "r") as file:
        return json.load(file) 

# Función para guardar el archivo JSON
def save_store_data(filename, store_data):
    with open(filename, "w") as file:
        json.dump(store_data, file, indent=4)

# Función para mostar productos por categoría
def products_by_category(store_data):
    category = input("Introduce la categoría: ").strip()
    products = [item for item in store_data["inventory"] if item["category"].lower() == category.lower()]
    if products:
        print(f"Prodcutos en la categoría '{category}': ")
        for product in products:
            print(f"- {product["name"]} (${product["price"]})")
    else:
        print(f"No se encontraron productos en la categoría '{category}'.")

# Función para calcular el valor total del inventario
def calculate_invetory_value(store_data):
    total_value = sum(item["price"] * item["stock"] for item in store_data["inventory"])
    print(f"El valor total del invetario es: ${total_value:.2f}")

# Función para encontrar prodctos con stock bajo
def low_stock_products(store_data):
    threshold = int(input("Introduce el límite de stock (Umbral): "))
    low_stock = [item for item in store_data["inventory"] if item["stock"] <= threshold]
    if low_stock:
        print(f"Productos con menos de {threshold} unidades: ")
        for product in low_stock:
            print(f"- {product['name']} (Stock: {product['stock']})")
    else:
        print(f"No hay productos con menos de {threshold} unidades.")

# Función para agregar un producto al invetario
def add_product(store_data):
    while True:
        try:
            new_id = int(input("Introduce el ID del producto: "))
            if any(product["id"] == new_id for product in store_data["inventory"]):
                print("El ID ya existe. Por favor, introduce un ID diferente.")
                continue
            break
        except ValueError:
            print("ID no válido. Por favor, introduce un número entero.")

    while True:
        new_name = input("Introduce el nombre del producto: ").strip()
        if new_name:
            break
        else:
            print("El nombre no puede estar vacío. Por favor, introduce un nombre válido.")

    while True:
        new_category = input("Introduce la categoría: ").strip()
        if new_category:
            break
        else:
            print("La categoría no puede estar vacía. Por favor, introduce una categoría válida.")

    while True:
        try:
            new_price = float(input("Introduce el precio: "))
            if new_price < 0:
                print("El precio no puede ser negativo. Por favor, introduce un precio válido.")
                continue
            break
        except ValueError:
            print("Precio no válido. Por favor, introduce un número.")

    while True:
        try:
            new_stock = int(input("Introduce la cantidad en stock: "))
            if new_stock < 0:
                print("La cantidad en stock no puede ser negativa. Por favor, introduce un número válido.")
                continue
            break
        except ValueError:
            print("Cantidad en stock no válida. Por favor, introduce un número entero.")

    new_product = {
        "id": new_id,
        "name": new_name,
        "category": new_category,
        "price": new_price,
        "stock": new_stock
    }

    store_data["inventory"].append(new_product)
    print(f"Producto '{new_product['name']}' agregado exitosamente.")

# Función para realizar una compra
def purchase_product(store_data):
    product_id = int(input("Introduce el ID del producto: "))
    quantity = int(input("Introduce la cantidad a comprar: "))
    for product in store_data["inventory"]:
        if product["id"] == product_id:
            if product["stock"] >= quantity:
                product["stock"] -= quantity
                total_cost = product["price"] * quantity
                print(f"Compra exitosa. Total: ${total_cost:.2f}")
                return
            else:
                print(f"Stock insuficiente. Disponible: {product['stock']}")
                return
    print("Producto no encontrado.")

# Menú principal con match-case
def main():
    filename = "store_inventory.json"
    store_data = load_store_data(filename)

    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Mostrar productos por categoría")
        print("2. Calcular valor total del inventario")
        print("3. Encontrar productos con stock bajo")
        print("4. Agregar un nuevo producto")
        print("5. Realizar una compra")
        print("6. Salir")

        option = input("Selecciona una opción: ".strip())

        match option:
            case "1":
                products_by_category(store_data)
            case "2":
                calculate_invetory_value(store_data)
            case "3":
                low_stock_products(store_data)
            case "4":
                add_product(store_data)
                save_store_data(filename, store_data)  # Guardar cambios al agregar un producto
            case "5":
                purchase_product(store_data)
                save_store_data(filename, store_data)  # Guardar cambios tras la compra
            case "6":
                print("Saliendo del programa. ¡Adiós!")
                break
            case _:
                print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
