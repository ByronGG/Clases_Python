# Pruebas Unitarias


"""
Las pruebas unitarias son un tipo que se utilizan para verificar que las partes
más pequeñas de un programa (unidades) funcionan correctamente.

* Aislamiento: Se enfocan en una unica unidad de código
* Automatización: En código que se ejecuta idefinidamente 
* Rápidas: Probar pequeñas unidades
* Repetibles: Prueban rendimiento, se ejecuta tantas veces como sea necesario

- Liberias 
unittest ->Python
Jest -> JS
JUnit -> Java
"""

import unittest

def sumar(a: int, b: int) -> int:
    return a + b

# Prueba unitaria usando unittest
class TestSumar(unittest.TestCase):

    def test_sumar_positivos(self):
        self.assertEqual(sumar(3, 5), 8)

    def test_sumar_negativos(self):
        self.assertEqual(sumar(-5, -3), -8)

    def test_sumar_mixtos(self):
        self.assertEqual(sumar(-2, 5), 3)

# if __name__ == '__main__':
#     unittest.main()

"""
Escribe una función llamada gestionar_cadena que reciba una cadena de texto 
y un parámetro opcional accion. Según el valor de accion, 
la función debe realizar lo siguiente:

"reversa": Devuelve la cadena al revés.
Ejemplo: "hola" → "aloh".
"mayusculas": Devuelve la cadena en mayúsculas.
Ejemplo: "hola" → "HOLA".
"minusculas": Devuelve la cadena en minúsculas.
Ejemplo: "HOLA" → "hola".
"longitud": Devuelve la longitud de la cadena.
Ejemplo: "hola" → 4.
Si accion no es válida o no se proporciona, 
lanza una excepción con el mensaje: "Acción no válida".
"""

def gestionar_cadena(cadena, acccion=None):
    if acccion == "reversa":
        return cadena[::-1]
    elif acccion == "mayuscaulas":
        return cadena.upper()
    elif acccion == "minusculas":
        return cadena.lower()
    elif acccion == "longitud":
        return len(cadena)
    else:
        raise ValueError("Acción no válida")
    
