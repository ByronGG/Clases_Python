# Excepciones


"""
* ZeroDivionError: Intentar dividir entre 0
* IndexError: Intento de acceder a un índice fuera del rango (Lista, Tupla, etc)
* KeyError: Acceso a una clave que no existe (Diccionario = {"nombre": "Arutro"})
* FileNotFoundError: Intento de abrir un archivo que no existe
* ValueError: Ocurre cuando un función recibe un argumento de otro tipo (Int != Str)
"""

# # Try - except
try:
    # Código que podría generar un error
    number = int(input("Ingrese un número: "))
    resultado = 10 / number
except ValueError:
    # Código para manejrar la excepción
    print("Debes ingresar un número valido!")
except ZeroDivisionError:
    # Código para manejrar la excepción
    print("No se puede divir entre cero!")
else:
    # Código que se ejecuta si no ocurre ninga expceción
    print(f"El resultado es: {resultado}")
finally:
    # Código que se ejecuta SIEMPRE, ocurra o no una excepción
    print("Gracias por usar el programa! :3")

# Raise - Traceback
def divir(a, b):
    if b == 0:
        raise ZeroDivisionError("ERROR! - El divisor no puede ser cero!!")
    return a / b


# Creación de una excepcion personalizada:
class MiError(Exception):
    pass
try:
    raise MiError("Error 404")
except MiError as e:
    print(e)

"""
Ejercicio: Sistema de reservas de vuelos
Descripción: Crea un programa que simule un sistema de reservas de vuelos.

Define las siguientes excepciones personalizadas:

ErrorDeReserva: Clase base (Clase Padre) para todas las excepciones relacionadas con reservas. [x]
VueloNoDisponible: Excepción para cuando un vuelo no está disponible. [x]
AsientosAgotados: Excepción para cuando no hay asientos disponibles en el vuelo. [x]
ReservaDuplicada: Excepción para cuando un pasajero intenta reservar más de una vez. [x]
Implementa las siguientes funcionalidades:

Una función reservar_asiento(vuelo, pasajero) que: []
Verifica si el vuelo está disponible. [x]
Verifica si hay asientos disponibles en el vuelo. [x]
Verifica si el pasajero ya tiene una reserva en ese vuelo. [x]
Si todo está en orden, registra la reserva.
Usa un bloque try-except para manejar las excepciones.

Requisitos:

Define un diccionario para representar los vuelos y su disponibilidad ({vuelo: asientos_disponibles}). [x]
Usa una lista para rastrear las reservas ([{"vuelo": vuelo, "pasajero": pasajero}]). [x]
"""

class ErrorDeReserva(Exception):
    pass

class VueloNoDisponible(ErrorDeReserva):
    pass

class AsientosAgotados(ErrorDeReserva):
    pass

class ReservaDuplicada(ErrorDeReserva):
    pass

# Diccionario (Key: Value)
vuelos_disponibilidad = { 
    "UK505": 210, # STR Vuelo -> Int Asientos disponibles
    "MX201": 80,
    "JAP600": 180,
    "USA205": 1
    }

# Lista de reservas
reservas = []

def reservar_asiento(vuelo, pasajero):
    try:
        # Verificar si el vuelo está disponible o no
        if vuelo not in vuelos_disponibilidad:
            raise VueloNoDisponible (f"El vuelo {vuelo} no está disponible o no existe!!!.")
        # Verificar si el aciento esta disponible
        if vuelos_disponibilidad[vuelo] == 0:
            raise AsientosAgotados (f"No hay asientos disponibles en el vuelo {vuelo}")
        # Verificar si el pasajero ya cuenta con un vuelo asignado
        for reserva in reservas:
            if reserva["vuelo"] == vuelo and reserva["pasajero"] == pasajero:
                raise ReservaDuplicada (f"El pasajero {pasajero} ya tiene una reserva {vuelo}")
        
        # Registrar la reserva
        reservas.append({"vuelo":vuelo, "pasajero": pasajero}) #Una lista de diccionarios
        vuelos_disponibilidad[vuelo] -=1 #Restamos a value asientos
        print(f"Reserva exitosa para {pasajero} en el vuelo {vuelo}")

    except ErrorDeReserva as e:
        print(f"Error al intentar reservar: {e} ({type(e).__name__})")
    
reservar_asiento("JAP600", "Arturo") # Caso de existo en reserva!
reservar_asiento("HAWAI100", "Pepe") # Error de vuelo que no existe
reservar_asiento("USA205", "Luis") # Aciento disponible 1 -> 0
reservar_asiento("USA205", "Jose") # Aciento disponible 0
reservar_asiento("JAP600", "Arturo") # Error pasajero ya tiene este vuelo asignado
reservar_asiento("MX201", "Arturo")

