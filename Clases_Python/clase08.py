# Ficheros TXT

# sintaxis básica Crear un archivo

"""
MODOS
* r = Read Lectura.
* w = Write Escritura (Crea el archivo en caso de que no exista)
* a = Appends Agregar (Añade contenido al final del archivo)
* x = Exclusive Creation (Crea el arcivo "Da error si el archivo ya existe") 
* b = Binary (Trabajar con archivos binarios (rb - wb))
* + = Lectura y escritura (r+ - w+)
"""

#variable = open("nombre", "modo" )

# with open("nombre_archivo", "modo") as f
    # Realizar operaciones
# close() <- Python no es necesario
# No es necesario cerrar el archivo, porque se cierra automaticamente (Python)

"""
OPERACIONES DE LECTURA
* read() = Lee todo archivo como una cadena
* readline() = Lee solo una linea
* readlines() = Lee todas las líneas y devuelve una lista
"""

with open("ejemplo.txt", "r") as f:
    contenido = f.read() # Lee todo el archivo
    print(contenido)

with open("ejemplo.txt", "r") as f:
    linea = f.readline() # Lee la primera línea
    print(linea)

with open("ejemplo.txt", "r") as f:
    lineas = f.readlines() # Lee todas las líneas como una lista
    print(lineas)

"""
ESCRIBIR EN UN FICHERO
* write() = Escribe una cadena en el archivo
* writelines() = Escribe una lista de cadenas en el archivo
"""


with open("ejemplo.txt", "w") as f:
    f.write("Hola Luis\n") #Escribir texto (Sobrescribe el archivo si YA EXISTE)
    f.write("Nueva linea de texto\n")

with open("ejemplo.txt", "a") as f:
    f.write("Texto adicional\n") #Añade texto al final del archivo
    f.write("Adios")

# Escribir varias líneas
lista_lineas = ["Linea 1\n", "Linea 2\n", "Linea 3\n"]

with open("ejemplo.txt", "w") as f:
    f.writelines(lista_lineas)

"""
"b" Binario (Modo leer binario ("rb") - Modo escribir binario ("wb"))
"""

# Leer un archivo binario
with open("imagen.jpg", "rb") as f:
    contenido = f.read()
    print(contenido)

with open("imagen.jpg", "wb") as f:
    f.write(contenido)

try:
    with open("ejemplo.txt", "r") as f:
        contenido = f.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe")
except Exception as e:
    print(f"Ocurrio un error: {e}")

# Leer el contenido de un archivo, convertilo a mayúsculas y guardarlo en otro archivo

try:
    with open("entrada.txt", "r") as entrada:
        cont = entrada.read().upper()
    with open("salida.txt", "w") as salida:
        salida.write(cont)
    print("Archivo procesado y guardado exitosamente.!!!!")
except FileNotFoundError:
    print("El archivo de entrada no existe")
except Exception as e:
    print(f"Error: {e}")

"""
BUENAS PRACTICAS EN ARCHIVOS
* Usa "with" para asegurar que los archivos se cierren correctamente.
* Manejo grande ficheros, considera leer y procesar en fragmentos.
* Maneja las excepciones para prevenir errores en tiempo de ejecución.
"""

"""
Descripción: El programa realizará lo siguiente:

Crear un fichero si no existe.
Agregar contenido al fichero.
Actualizar una línea específica.
Borrar una línea específica.
Eliminar todo el contenido del fichero.
Salir del programa (con o sin borrar el fichero).
"""

import os #Libreria Opration System (Sistema operativo)

def monstrar_menu():
    print("""
    === GESTOR DE ARCHIVOS ===
    1. Crear el archivo
    2. Agregar contenido al archivo
    3. Actualizar una línea del archivo
    4. Borrar una línea del archivo
    5. Eliminar todo el contenido del archivo
    6. Salir sin borrar el archivo
    7. Salir y eliminar el archivo
    """)

"""
CRUD de Archivos
C = Create
R = Read
U = Update
D = Delete
"""

def main():
    nombre_fichero = "archivo_ejemplo.txt"

    while True:
        monstrar_menu()
        opcion = input("Elige una opción (1 - 7): ")

        match opcion:
            case "1": # Crear el archivo
                if not os.path.exists(nombre_fichero):
                    with open(nombre_fichero, "w") as f:
                        print(f"Archivo '{nombre_fichero}' creado exitosamente.")
                else:
                    print(f"El archivo '{nombre_fichero}' ya existe.")
            case "2": # Agregar contenido al archivo
                contenido = input("Introduce el texto a agregar: ")
                with open(nombre_fichero, "a") as f:
                    f.write(contenido + "\n")
                print("Contenido agregado al archivo!")
            case "3": # Actualizar una línea específica
                try:
                    with open(nombre_fichero, "r") as f:
                        lineas = f.readlines()
                    print("Contenido actual del fichero: ")
                    for i, linea in enumerate(lineas, start=1):
                        print(f"{i}: {linea.strip()}")
                    num_linea = int(input("Número de línea a actualizar: "))
                    if 1 <= num_linea <= len(lineas):
                        nuevo_contenido = input("Nuevo contenido para la línea: ")
                        lineas[num_linea - 1] = nuevo_contenido + "\n"
                        with open(nombre_fichero, "w") as f:
                            f.writelines(lineas)
                        print("Línea actualizada exitosamente.")
                    else:
                        print("Número de línea es inválido")
                except FileNotFoundError:
                    print("El archivo no existe, Por favor, créalo primero :D")
            case "4": # Borrar una línea específica
                try:
                    with open(nombre_fichero, "r") as f:
                        lineas = f.readlines()
                    print("Contenido actual del fichero: ")
                    for i, linea in enumerate(lineas, start=1):
                        print(f"{i}: {linea.strip()}")
                    num_linea = int(input("Número de línea a borrar: "))
                    if 1 <= num_linea <= len(lineas):
                        lineas.pop(num_linea - 1)
                        with open(nombre_fichero, "w") as f:
                            f.writelines(lineas)
                        print("Línea borrada exitosamente!")
                    else:
                        print("Número de línea inválido")
                except FileNotFoundError:
                    print("El archivo no existe, Por favor, créalo primero :D")
            case "5": # Elimina todo el contenido del archivo
                try:
                    with open(nombre_fichero, "w") as f:
                        pass
                    print("Contenido del archivo eliminado.")
                except FileNotFoundError:
                    print("El archivo no existe, Por favor, créalo primero :D")
            case "6": # Salir sin borrar el fichero
                print("Saliendo del programa. El archivo se conserva!")
                break
            case "7": # salir y eliminar el fichero
                if os.path.exists(nombre_fichero):
                    os.remove(nombre_fichero)
                    print(f"Archivo '{nombre_fichero}' eliminado.")
                else:
                    print("El archivo no existe.")
                print("Saliendo del programa.")
                break
            case _: #Operacion no valida
                print("Opción no válida. Intenalo de nuevo")

if __name__ == "__main__":
    main()


