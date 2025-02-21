"""
Metodos asincronos Python

La programación asíncrona en Pythonpermite ejecutar múltiples tareas simultáneamente. Esto es útil cuando trabajanmos con operaciones de entrada o salida (I/O) como solicitudes HTTP, lectura escritura en archivos o conexiones a bases de datos, ya que evita que el programa se quede "esperando" mientras se complemetan estas operaciones.

Diferencias entre programación sincrónas y asíncrona

Caracteristicas                      Sincróna                                        Asícrona
Ejecición                            Lineal, una trarea a la vez                    Varias tareas pueden ejecutarse sin bloquerse
Bloqueo                              Bloque el flujo hasta la tarea termien        No bloque, permitiendo continuar con otras tarea
Rendimiento                         Puede ser lento si hay tareas pesadas           Más eficinte tareas de I/O

"""

import time
import asyncio # Libreria para crear funsiones anincronas
import aiohttp # Libreria aiohttp permite hacer solicitudes HTTP de forma asíncrona

# Ejemplo de funsiones sincrónas
def tarea_1():
    print("inciando tarea 1...")
    time.sleep(3) # Simula operación que tarda 3 segundo
    print("Tarea 1 terminada!")

def tarea_2():
    print("Iniciando tarea 2...")
    time.sleep(2)
    print("Tarea 2 terminada!")

tarea_1()
tarea_2()
print("Todas las tareas termiandas")

print("---------------------------------------------------------------------")

async def tarea_1():
    print("Iniciando tarea 1...")
    await asyncio.sleep(3) # Simula una espera sin bloquear
    print("Tarea 1 terminada!")

async def tarea_2():
    print("Iniciando tarea 2...")
    await asyncio.sleep(2)
    print("Tarea 2 terminada!")

async def main():
    await asyncio.gather(tarea_1(), tarea_2()) # Ejecuta ambas tareas en paralelo (Corrutinas)

asyncio.run(main()) # Ejecutar el método main

"""
Python permite trabajar con programación asíncrona a través del módulo 'asyncio', usando dos palabras clave principalmente:

1. async: Convierte una función en una corrutina (función asíncrona)
2. await: Espera a que una corrutina termuine sin bloquear la ejecución
3. La función asyncio.gather() permite ejecutar múltiples tareas en paralelo.

"""

print("---------------------------------------------------------")

async def obtener_datos(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as respone:
            print(f"Obteniendo datos de {url}")
            return await respone.text()

async def main():
    urls =["https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4",
        "https://jsonplaceholder.typicode.com/todos/5"]
    
    tareas = [obtener_datos(url) for url in urls] #Expreción obtener_datos() => for ulr en la lista de las urls => *tareas
    respuestas = await asyncio.gather(*tareas)

    for i, respuesta in enumerate(respuestas):
        print(f"Respuesta {i + 1}: {respuesta[:100]}...")

asyncio.run(main())

"""
    async def: Define una función asíncrona (corrutina).
    await: Permite esperar resultados sin bloquear la ejecución.
    asyncio.run(coroutine): Ejecuta una corrutina principal.
    asyncio.gather(task1, task2, ...): Ejecuta varias tareas en paralelo.
    asyncio.create_task(coroutine): Ejecuta una tarea en segundo plano.
    asyncio.sleep(segundos): Simula una pausa sin bloquear.
    run_in_executor(): Permite ejecutar funciones sincrónicas sin bloquear.


    * Intgerfaces gráficas (GUI).
    * Aplicaciones que dependen de múltiples eventos.
    * Descargas simultáneas.

    - Cálculos matemáticos complejos.
    - Inteligencia artificial o pocesamientos de imágenes en paralelo. (Entrenamiento Hilos)
"""

print("--------------------------------------------------------------------------------------")

"""
Desarrolla una app que necesita descargar múltiples archivos (ejemplos) desde diferentes URLS al mismo tiempo
Implementar una solución que utilice programación asíncrona para descargar archivos en paralelo

* Simular la descarga de archivos usando 'asyncio.sleep()'
* Cada archivo tiene un tiempo de descarga diferente 
* El programa debe iniciar todas las descargas al mismo tiempo y esperar a que termien
* Debe mostrar el inicio y el fin de cada descarga
"""


import asyncio
import random

# async def descarga ():
#     print("Iniciando descarga...")
#     await asyncio.gather(descarga_operacion())

# async def descarga_operacion():
#     urls = ["hppts://www.descarga.com"]


async def descargar_archivo(nombre: str, tiempo: int): # Definir la corrutina asíncrona (async def)
    print(f"Iniciando descarga de {nombre} (Tiempo estimado: {tiempo}s)")
    await asyncio.sleep(tiempo) # Simular tiempo de espera
    print(f"Descargar completada {nombre}")


async def main(): # Se crea una lista de archivos con nombres y tiempos de descarga aleatorios
    archivos = [("Archivo_1.pdf", random.randint(2, 5)), # String => Archivo_1.pdf | Int => 2 - 5 = Archivo_1.pdf, 2
                ("Arachivo_2.mp3", random.randint(3, 7)), # String => Archivo_2.mp3 | Int => 3 - 7 = Arachivo_2.mp3, 7
                ("Archivo_3.gif", random.randint(1, 4)), # String => Archivo_3.gif | Int => 1 - 4
                ("Archivo_4.jpg", random.randint(2, 6)) # String => Archivo_4.jpg | Int => 2 - 6
                ]
    
    tareas = [descargar_archivo(nombre, tiempo) for nombre, tiempo in archivos] # Se usa una lista por comprensión para crear las taras (tareas = [.....])
    await asyncio.gather(*tareas) # Ejecuta todas las descargas en paralelo

asyncio.run(main()) # Ejecuta el programa