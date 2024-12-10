print("-----------------------PART 2-----------------------")
"""
Procolo HTTP (Capa 7 modelo OSI - Aplicación)
GET = Obtener uno o varios recursos de una API
POST = Crear un nuevo recurso
PUT = Actualizar un recurso (Reemplaza un recurso por completo)
PATCH = Actualizar un recurso (Reemplza solo una parte del recurso)
DELETE = Eliminar un recurso
"""
import requests
import json

print("------------------GET ALL------------------")

# Get: Obtener una lista de recursos
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    print("Lista de publicaciones: ")
    for post in response.json()[:10]: # Mostrar solo las primeras 10 publicaciones
        print(f"ID: {post['id']}, Título: {post['title']}")
else:
    print(f"Error: {response.status_code}")

print("------------------GET------------------")

# Get: Obtener un unico recurso
post_id = 1 # Obtener una publicación específica (ID = 1)
url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
response = requests.get(url)

if response.status_code == 200:
    post = response.json()
    print(f"Publicación ID {post_id}:")
    print(f"Título: {post['title']}")
    print(f"Cuerpo: {post['body']}")
else:
    print(f"Error: {response.status_code}")

print("------------------POST------------------")

url = "https://jsonplaceholder.typicode.com/posts"
new_post = {
    "title": "Nuevo Post",
    "body": "Nueva publicación",
    "userId": 1
}
response = requests.post(url, json=new_post)

if response.status_code == 201:
    print("Publicación creada: ")
    print(response.json())
else:
    print(f"Error: {response.status_code}")

print("------------------PUT------------------")

# Actualizar un publicación existente (ID = 1)
post_id = 1
url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

updated_post = {
    "id": post_id,
    "title": "Actualizado",
    "body": "Nueva versión",
    "userId": 1
}
response = requests.put(url, json=updated_post)

if response.status_code == 200:
    print("Publicación actualizada: ")
    print(response.json())
else:
    print(f"Error: {response.status_code}")

print("------------------PATCH------------------")

# Actualizar solo el título de una publicación (ID = 1)

post_id = 1
url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

partial_update = {
    "title": "Titulo parcialmente actualizado"
}
response = requests.patch(url,json=partial_update)

if response.status_code == 200:
    print("Publicación parcialmente actualizada: ")
    print(response.json())
else: 
    print(f"Código resivido por el servidor: {response.status_code}")

print("------------------DELETE------------------")

post_id = 1
url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
response = requests.delete(url)

if response.status_code == 200:
    print(f"Publicación ID {post_id} elimiada.")
else: 
    print(f"Código resivido por el servidor: {response.status_code}")

