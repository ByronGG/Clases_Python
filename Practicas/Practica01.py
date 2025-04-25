"""
Crea una función que rebiba una cadena y la devuleva al reves.
Por ejemplo, si la cadena es "Hola Mundo", la función debe devolver "odnuM aloH".
"""

# def reverse(texto):
#     texto_final = texto.reverse()
#     return texto_final


# def main():
#     texto = str(input("Introduce un texto"))

#     resultado = reverse(texto)
#     print(resultado)

# main()

print("------------------------------------------------------------")


def invertir_cadena(palabra):
    invertida = ""  # Str vacio
    for letra in reversed(palabra):
        invertida += letra
    return invertida


print(invertir_cadena("roma hola"))

print("------------------------------------------------------------")


def invertir_slincing(palabra):
    return palabra[::-1]  # [inicio:final:paso]


print(invertir_slincing("Arturo"))

print("------------------------------------------------------------")

"""
    Range que comieza en el ultimo índice (len(palabra) - 1) y termina en -1 (exclusivo), con paso -1
"""


def invertir_indices(palabra):
    invertida = ""
    for i in range(len(palabra) - 1, -1, -1):
        invertida += palabra[i]
    return invertida


print(invertir_indices("Luis"))

print("------------------------------------------------------------")


def invertir_lista(palabra):  # Str = Reyna
    lista = list(palabra)  # List = [R, e, y, n, a]
    lista.reverse()  # List = [a, n, y, e, R]
    return "".join(lista)  # anyeR


print(invertir_lista("Reyna"))

print("------------------------------------------------------------")


"""
    Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""
# CO x (1+Ti)^t


def calcular_capital(capatial_inicial, interes, años):
    for año in range(1, años + 1):
        capatial_inicial *= 1 + interes / 100
        print(f"Año {año}: Capital = {capatial_inicial:.2f}")


def main():
    capital = float(input("Cantidad a invertir: "))
    interes = float(input("interés anual (%): "))
    años = int(input("Número de años: "))
    calcular_capital(capital, interes, años)


# main()

print("------------------------------------------------------------")

"""
    Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""

def asignar_grupo():
    nombre = input("ingresa tu nombre: ").strip().capitalize()
    sexo = input("ingresa tu sexo (M para mujer, H para hombre): ").strip().capitalize()

    if (sexo == 'M' and nombre < 'M') or (sexo == 'H' and nombre > 'N'):
        grupo = 'A'
    else:
        grupo = 'B'

    print(f"Hola {nombre}, pertectes al grupo {grupo}")

asignar_grupo()

def obtener_sexo():
    sexo = input("Sexo (M/H): ").strip().upper()
    while sexo not in ['M', 'H']:
        sexo = input("Sexo no válido. Ingresa M (Mujer) o H (Hombre): ").strip().upper()
    return sexo

def determinar_grupo(nombre, sexo):
    if (sexo == 'M' and nombre < 'M') or (sexo == 'H' and nombre > 'N'):
        return 'A'
    else:
        return 'B'

def main():
    nombre = input("Nombre: ").strip().capitalize()
    sexo = obtener_sexo()
    grupo = determinar_grupo(nombre, sexo)
    print(f"{nombre}, estás en grupo {grupo}")

main()