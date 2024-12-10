# Pilas / Stack (LIFO) Last In Fist Out

stack = [] # Lista (LIFO)

# Push
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

print(stack)

# Pop
item = stack[len(stack) - 1] # Mostramor el ultimo valor de la PILA
del stack[len(stack) - 1] # Aquí eliminamos el ultimo valor de la PILA
print(item) # Muestra el ultumo valor
print(stack) # Muestra la PILA sin el ultimo valor

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
# print(stack.pop()) # Aquí ya la lista (PILA) ya esta vacia y hace un error de index

print("--------------------------------------------------------------------------------------------")

# Cola / Queue (FIFO) First In First Out

queue = []

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

print(queue)

queue_item = queue[0]
del queue[0]
print(queue_item)
print(queue)

print(queue.pop(0))
print(queue)

"""
Descripción:
Crea un programa que implemente una pila para gestionar una lista de tareas pendientes. 
Cada vez que se agregue una nueva tarea, esta debe ser añadida al final de la pila, 
y cada vez que se complete una tarea, debe ser removida de la parte superior de la pila.

Requisitos:

Crear la pila como una lista vacía (tareas = []). [x]
Implementar una función agregar_tarea(tareas, tarea) que añada una tarea a la pila. [x]
Implementar una función completar_tarea(tareas) que elimine la última tarea añadida. [x]
Implementar una función ver_tareas(tareas) que muestre las tareas actuales en la pila. [x]
"""

def agregar_tarea(tareas, tarea):
    tareas.append(tarea)
    print(f"Tarea {tarea} fue añadida")

def completar_tarea(tareas):
    if tareas:
        tarea = tareas.pop()
        print(f"Tarea {tarea} ha sido completada!!") #  Flag == True
    else:
        print("No hay tareas pendientes en la lista") # Flag == False
    #print(f"{tarea.pop()} ha sido completada")

def ver_tareas(tareas):
    print(tareas)

# Casos
tareas = []
agregar_tarea(tareas, "Dormir")
agregar_tarea(tareas, "Jugar")
agregar_tarea(tareas, "Estudiar")

ver_tareas(tareas)

completar_tarea(tareas) # Dormir
completar_tarea(tareas) # Jugar
completar_tarea(tareas) # Estudiar
completar_tarea(tareas) # NONE

ver_tareas(tareas)


print("--------------------------------------------------------------------------------------------")

"""
Descripción:
Implementa una cola para simular una fila de atención en un banco. 
Cada cliente nuevo se agrega al final de la cola, y cada vez que un cajero atiende a un cliente, 
el cliente es removido del inicio de la cola.

Requisitos:

Crear la cola como una lista vacía (clientes = []). [x]
Implementar una función agregar_cliente(clientes, cliente) que añada un cliente a la cola. [x]
Implementar una función atender_cliente(clientes) que elimine el cliente en el inicio de la cola. [x]
Implementar una función ver_cola(clientes) que muestre la cola de clientes actual. []
"""

clientes = []

def agregar_cliente(clientes, cliente):
    clientes.append(cliente)
    print(f"El Cliente {cliente} añadido a la cola.")

def atender_cliente(clientes):
    #print(len(clientes))
    if len(clientes) == 0:
        print("Ya se acabo")
    else:
        print(f"Se atendio a: {clientes.pop(0)}")
    #print(f"Se atendio al cliente {clientes}")

def ver_cola(clientes):
    print(clientes)

agregar_cliente(clientes, "Arturo")
agregar_cliente(clientes, "Luis")
agregar_cliente(clientes, "Pepe")

ver_cola(clientes) # Arturo - Luis - Pepe

atender_cliente(clientes) # Arturo
atender_cliente(clientes) # Luis
atender_cliente(clientes) # Pepe
atender_cliente(clientes) #4to cliente que existe

ver_cola(clientes)

print("--------------------------------------------------------------------------------------------")

# Clases

# Una clase es como plano o molde que define las propiedades (Atributos), y acciones (métodos)

class Persona: # Clase Persona
    # Constructor para inicializar los atributos
    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre # Atributo Nombre
        self.edad = edad # Atriburo Edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}, mi edad es {self.edad}")

# Crear objetos de la clase Persona
persona1 = Persona("Arturo", 18)
persona2 = Persona("Luis", 24)

# Llamar al método saludar que la clase Persona
persona1.saludar()
persona2.saludar()

print("--------------------------------------------------------------------------------------------")

# Clase bancaria

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad: int):
        self.saldo += cantidad
        print(f"Se ha depositado {cantidad}. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad: int):
        if cantidad > self.saldo or self.saldo == 0:
            print("No hay suficientes fondos para retirar")
        else:
            self.saldo -= cantidad
            print(f"Se han retidado {cantidad}. Nuevo saldo: {self.saldo}")
        # if cantidad > self.saldo:
        #     print("Fondos insuficientes")
        # else:
        #     self.saldo -= cantidad
        #     print(f"Se han retidado {cantidad}. Nuevo saldo: {self.saldo}")

# Crear un objeto de la clase CuentaBancaria

mi_cuenta = CuentaBancaria("Arturo", 500)

# Realizar las operacion (métodos)
mi_cuenta.depositar(500)
mi_cuenta.retirar(2000)

