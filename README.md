# Clases_Python

## Clase 01 - Funciónes
- Clase para entender las funciones de usuario, dentro funsion, built-in (Python)
```Python
# Funciones usuario
def argViriables(*nombres):
    for nombre in nombres:
        print(f"Hola, {nombre}!")

argViriables("Arturo", "Luis", "Lola")
```
- Variables locales y globales dentro de funsiones
```Python
# Variables Locales y Globales

globalVar = "Arturo"

def saludo():
    localVar = "Hola"
    print(f"{localVar}, {globalVar}")
```

## Clase 02 - Listas, Tuplas, Sets, Diccionarios
Esta clase de estructa de datos casjadnajsndajnd



## Clase Tuplas

## 1. El uso de funciones y el llamarlas para ejecutar ciertos elementos como añadir, eliminar, insertar, buscar, salir
## 2. La verificación de "if name in agenda" por ejemplo para corroborar que no este ya escrito un dato o variable para no crear duplicados.
## 3. El uso del .pop para hacer eliminación por pila


## Clase Cadena de Caracteres
## 1 .replace() sirve para reemplazar una serie de caracteres seleccionados
## 2 .strip() elimina los espacios dentro de un string


## Clase Clases
## FIFO para las colas. LIFO para las pilas
## FIFO significa First in First Out
## LIFO significa Last in First Out
## En las clases se almacenan varios parametros que se pueden acceder a ellos mismos (self) y entre estos pero solo dentro de la misma clase.



## Clase Excepciones
## Las excepciones sirven para hacer que Python revise un codigo sin que bote error en automatico, y si no es valido o hay un error en esa parte el codigo except se lo puede saltar o proseguir, segun diga el usuario.
## Los mensajes de error se pueden imprimir en formato print() de una manera mas amigable al usuario en vez de botar un mensaje de error en rojo que pare todo el programa.
