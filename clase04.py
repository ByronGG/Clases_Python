# Variables Globales y Locales

x = 10 # Variable Global

def mostrarX():
    #Código
    #Sino declaro la misma variable dentro de esta función, entonces si puedo acceder a ella
    print(x) #Acceder a variable global

mostrarX()

print("-------------------------------------------------------")

y = 20 #Global

def interatuarVariableGlobal():
    # Si se necesita modificar una variable global dentro de una función, esta debe declararce "global" dentro de esta
    global y #Accedo a una variable global dentro de una función
    y += 20

interatuarVariableGlobal()
print(y)

print("-------------------------------------------------------")

def mi_funcion():
    z = 50 # Variable local
    print(z)

mi_funcion()
#print(z)

print("-------------------------------------------------------")

a = 60 # Global

def otraFuncion():
    a = 70 # Local
    print(a)

otraFuncion() # Llamada de la función que tiene una variable local
print(a) #Imprime la variable global

print("-------------------------------------------------------")

# Recursividad

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

#Fibunacci sin recursividad
def fibonacci(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    fib = [0, 1] #Creo la lista fibunacci con los dos primero números
    for i in range(2, num):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print(fibonacci(10))

print("-------------------------------------------------------")

def fibonacci_recursiva(num):
    if num <= 0:
        return []
    if num == 1:
        return [0]
    elif num == 2:
        return[0, 1]
    else:
        fib = fibonacci_recursiva(num - 1)
        fib.append(fib[-1] + fib[-2])
        return fib
    
print(fibonacci_recursiva(10))

print("-------------------------------------------------------")

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memo(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci_memo(num - 1) + fibonacci_memo(num - 2)

# Imprime los primeros 10 números de la secuencia de Fibonacci
fibonacci_sequence = [fibonacci_memo(i) for i in range(20)]
print(fibonacci_sequence)  # Salida: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
