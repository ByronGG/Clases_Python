# Funciones usuario
def argViriables(*nombres):
    for nombre in nombres:
        print(f"Hola, {nombre}!")

argViriables("Arturo", "Luis", "Lola")

# Funciones dentro de funciones
def primeraFuncion(): 
    def segundaFuncion():
        print("Función dentro de una función") 
    segundaFuncion()

primeraFuncion()

#Funciones del lenguaje (Python) (build-in method)
print(len("Arturo"))
print("Arturo".upper())
print("ARTURO".lower())
print("--------------------------------------------------")

# Variables Locales y Globales

globalVar = "Arturo"

def saludo():
    localVar = "Hola"
    print(f"{localVar}, {globalVar}")

saludo()
print("---------------------------------------------")

#Ejercicio Fizz Buzz
"""
La función imprime todos los números del 1 al 100 [X]. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro (Fizz) [X].
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro (Buzz) [X].
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas (FizzBuzz)[X].
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos [X].
"""

def unoACien(Fizz, Buzz):
    contadorImpresiones = 0
    for number in range(1, 101):
        if(number % 3 == 0) and (number % 5 == 0):
            print(Fizz, Buzz)
        elif number % 3 == 0:
            print(Fizz)
        elif number % 5 == 0:
            print(Buzz)
        else:
            print(number)
            contadorImpresiones += 1
    return print(f"Numero de veces que aparecen: {contadorImpresiones}")

"""
def unoACien(Fizz, Buzz):
    contadorImpresiones = 0
    for number in range(1, 101):
        print(number)
        if(number % 3 == 0) and (number % 5 == 0):
            print(Fizz, Buzz)
            contadorImpresiones += 1
        elif number % 3 == 0:
            print(Fizz)
            contadorImpresiones += 1
        elif number % 5 == 0:
            print(Buzz)
            contadorImpresiones += 1
    return print(f"Numero de veces que aparecen: {contadorImpresiones}")
"""

print(unoACien("Fizz", "Buzz"))

