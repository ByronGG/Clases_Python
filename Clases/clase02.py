# Estructura de datos

#Listas
mi_list = ["Arturo", "Luis", "Pepe", "Roberto"] #str
print(mi_list)
mi_list.append("Lupe") #Inserción
print(mi_list)
mi_list.pop()
print(mi_list)
mi_list.pop(1) #Eliminación por pila (indice)
print(mi_list)
mi_list.remove("Pepe") #Eliminación
print(mi_list)
mi_list.sort() #Ordenar
print(mi_list)
mi_list[1] = "Memo" #Actualizar
print(mi_list)
print(type(mi_list))
print("------------------------------------------------------------------------")

#Tuplas
mi_tupla = ("Arturo", "contraña", "arturo@gmail.com", "25970", "Arturo")
print(mi_tupla[2]) #Acesso
print(mi_tupla[1])
mi_tupla = tuple(sorted(mi_tupla)) #Ordenar por metodos de sistema (castenado - sorted)
print(mi_tupla)
print(type(mi_tupla))
print("------------------------------------------------------------------------")

#Sets
mi_set = {"Arturo", "Luis", "13457"}
print(mi_set)
mi_set.add("Hola") #Inserción
print(mi_set)
mi_set.add("Hola") #No se pueden repetir valores en un set
print(mi_set)
mi_set.remove("13457") #Eliminación
print(mi_set)
print(type(mi_set))
print("------------------------------------------------------------------------")

#Diccionario
mi_diccionario = {"name": "Arturo",
                "lastname": "Solis",
                "email": "hola",
                "phone": "8333394139"
            } # Creación diccionario

mi_diccionario["email"] ="arturo@gmail.com" #Insertar
print(mi_diccionario)
mi_diccionario["phone"] = "" #Sustituir el 'valor' a una cadena vacia
print(mi_diccionario)
del mi_diccionario["phone"] #Eliminación (de todo clave-valor)
print(mi_diccionario)
print(mi_diccionario["lastname"]) #Acceso (Leer)
mi_diccionario = dict(sorted(mi_diccionario.items())) #Ordenar
print(mi_diccionario)
print(type(mi_diccionario))
print("------------------------------------------------------------------------")

"""
* Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de inserción, búsqueda, actualización
 *   y eliminación de contactos. [X]
 * - Cada contacto debe tener un nombre y un número de teléfono. [X]
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo. [X]
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 10 dígitos. [X]
 * - También se debe proponer una operación de finalización del programa. []
"""

def Agenda():
    agenda = {} #Diccionario (Agenda)

    def insertar():
        phone = input("Introduce numero telefonico: ")
        if phone.isdigit() and len(phone) == 10:
            agenda[name] = phone
        else:
            print("Ingresar un número de teléfono de un maximo de 10 digitos")

    while True:
        print("") #Menú de la Agenda
        print("1. Inserción")
        print("2. Búsqueda")
        print("3. Actualización")
        print("4. Eliminación")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")
        match opcion:
            case "1": #Insertar
                name = input("Introduce el nombre contacto: ")
                insertar()
            case "2": #Buscar
                name = input("Introduce el nombre del contacto a buscar: ") 
                if name in agenda:
                    print(f"El número de telefono de {name} es {agenda[name]}")
                else:
                    print(f"El contacto de {name} no exite!")
            case "3": #Actualizar
                name = input("Ingrece el nombre del contacto a actualizar: ")
                if name in agenda:
                    insertar()
                else:
                    print(f"El contacto {name} no exite!")
            case "4":
                name = input("Ingrese el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe!")
            case "5":
                print("Saliendo de la agenda!")
                break
            case _:
                print("Opcion no valida. Marque del 1 al 5")

Agenda()