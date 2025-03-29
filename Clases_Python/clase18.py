# REGEX Expresiones Regulares

"""
    - Son secuancias de caracteres que forman un patrón de búsqueda
        * Buscar texto en cadena
        * Validar formatos
        * Extraer información específica
        * Remplazar fragmentos de texto

    a) Literales
        - Coinciden extactemente con el carácter especifico
            * Ejemplo 'a' coincide con la letra 'a'
    
    b) Metacaracteres
        - Caracteres especiales con significado único
            * . Cualquier carácter (expecto nueva línea)
            * ^ Inicio de la cadena
            * $ Fin de la cadena
            * | Operador 'OR' (esto o aquello)
    
    c) Cuantificadores
        - Para encontrar números
            * * 0 o más repeticiones del elemento anterior
            * + 1 o más repeticiones
            * ? 0 o 1 repetición
            * {n} Exactamente n repeticiones
            * {n,m} Entre 'n' y 'm' repeticiones

    d) Clases de Caracteres
        - Caracteres
            * [abc] Cualquier de los caractres 'a, b o c'
            * [a - z] Cualquier letra minuscula
            * [A - Z] Cualquier letra mayusculas
            * [^abc] Negación (cualquier caracter 'a, b o c')

    e) Senciancis Especiales
        - Secuencias
            * \d Digitos (0 - 9)
            * \D No digitos
            * \w Carácter alfanumerico (letras, números, guión bajo)
            * \W No alfanumericos
            * \s Especio en blaco (espacios, tab, nueva línea)
            * \S No espacion en blanco
        
    f) Grupos
        * () Agrupar parte de la expresión para aplicar cuantificadores o capturar subclases

    * Validar formatos: fechas, emails, contraseñas.
    * Buscar patrones en logs o archivos grandes.
    * Extraer datos de texto estructurados.
    * Limpiar o tranformar texto.

    Ejmplo REGEX
    Supongamos que queremo validar un número de teléfono en el formato 833-234-1659, donde cada X es un digito

        Patrón Regex:
            ^\d{3}\d{3}-\d{4}$
            
            * ^ y $ aseguran que toda la caderna cumpla el patrón
            * \d{3} Tres dígitos seguidos de un guión

    re.search(pattern, string): Buscar patrón en cualquier parte del texto
    re.match(pattern, string): Buscar el patrón solo al inicio del texto
    re.findall(pattern, string): Busca todas las coincidencias del patrón
    re.finditer(pattern, string): Similar findall(), pero retorna un iterador de obejtos
    re.sub(pattern, string): Reemplaza todas las cindiciones del patrón con replacement
    re.split(pattern, string): Divide el string usando el patrón como separador
    re.compile(): Si usas el mismo patrón muchas veces, compílalo para mayor eficiencia
"""

import re

texto = "El gato está en el jardín"
resultado = re.search(r'gato', texto)

if resultado:
    print("Cincidencia encontrada: ", resultado.group())
else:
    print("No hay concidencia")


print("----------------------------------------------------------------------")

texto = "123 es un número"
resultado = re.match(r'\d+', texto)

if resultado:
    print("Coincidencia al incio:", resultado.group())

print("----------------------------------------------------------------------")

texto = "Los números son 42, 7 y 100"
numeros = re.findall(r'\d+', texto)
print(numeros)

print("----------------------------------------------------------------------")

texto = "abc 123 xyz 456"
for coincidencia in re.finditer(r'\d+', texto):
    print(coincidencia.group(), "en posición ", coincidencia.span())

print("----------------------------------------------------------------------")

texto = "Hoy es 28/03/2025"
texto_modificado = re.sub(r'\d{2}/\d{2}/\d{4}', 'DD/MM/AAAA', texto)
print(texto_modificado)

print("----------------------------------------------------------------------")

texto = "Manzanas, Naranjas; Uvas, Piña"
partes = re.split(r'[,;]', texto)
print(partes)

print("----------------------------------------------------------------------")

patron = re.compile(r'\d{3}-\d{3}-\d{4}') # Ejemplo: Telefono XXX-XXX-XXXX
texto = "Mi número es 833-234-1659"

resultado = patron.search(texto)
if resultado:
    print("Telefono encontrado: ", resultado.group())

print("----------------------------------------------------------------------")

texto = "Telefono: +52-55-1234-5678"
patron = re.compile(r'\+(\d{2})-(\d{2})-\d{4}-\d{4}')
coincidencia = patron.search(texto)

if coincidencia:
    print("Código de país: ", coincidencia.group(1))
    print("Código de país: ", coincidencia.group(2))

print("----------------------------------------------------------------------")

# Validar Email

def validar_email(email):
    patron = r'^[\w.-]+@[\w\.-]+\.\w+$' # Formato básico
    return re.match(patron, email)

print(validar_email("algobard@gmail.com")) # True
print(validar_email("byron@.com")) # False

print("----------------------------------------------------------------------")

"""
    Escribe un script en Python que:

    1. Valide si un número de teléfono cumple con alguno de estos formatos:
        (XXX) XXX-XXXX
        XXX-XXX-XXXX
        XXX XXX XXXX (con espacios).

    2. Extraiga el código de área (primeros 3 dígitos) y el número principal (últimos 7 dígitos).
    Ejemplos de entradas válidas:
        (123) 456-7890
        987-654-3210
        555 123 4567

    3. Ejemplos de entradas inválidas:
        12-345-6789 (código de área incompleto)
        (abc) def-ghij (contiene letras)
        1234567890 (sin formato)
"""
import re

# funciones
def validar_y_extraer_telefono(numero):
    # Definir el patrón con grupo de captura
    patron = r'^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})$'

    """
    ^ -> Inicio de busqueda
    \(? -> Paréntesis despues de apertura opcional(? inidica 0 o 1 repeticiones)
    (\d{3}) -> Grupo 1: 3 digitos
    \)? -> Parénteisis de cierre opcional
    [- ]? -> Seperador opciones (guión o espacio)
    (\d{3}) -> Grupo 2: 3 dígitos
    [- ]? -> Seperador opciones (guión o espacio)
    (\d{4}) -> Grupo 3: 4 dígitos
    $ -> fin de busqueda
    """
    # Validar el formato
    if re.match(patron, numero):
        coincidencia = re.search(patron, numero)
        codigo_area = coincidencia.group(1) # XXX | (XXX) | XXX
        numero_principal = f"{coincidencia.group(2)}-{coincidencia.group(3)}" # XXX-XXXX | XXX XXXX 
        return True, codigo_area, numero_principal # Check True -> XXX-XXX-XXXX | (XXX)-XXX-XXXX | XXX XXX XXXX
    else:
        return False, None, None # Check False -> None | None

# Pruebas
numeros_prueba = [
    "(123) 456-7890",
    "987-654-3210",
    "555 123 4567",
    "12-345-6789",
    "(abc) def-ghij",
    "1234567890"
]

for num in numeros_prueba:
    valido, codigo, principal = validar_y_extraer_telefono(num)
    print(f"Número: {num}")
    print(f"Válido {num}")
    if valido:
        print(f"Código de área: {codigo}")
        print(f"Número principal: {principal}")
    print("-" * 30)


"""
Ejercicio: Extraer Información de Logs de Servidor

Escribe un script en Python que procese líneas de un log de servidor y extraiga:

    Dirección IP del cliente.
    Fecha y hora de la solicitud.
    Método HTTP utilizado (ej: GET, POST, etc.).

Formato del log (ejemplo):
    192.168.1.1 - - [15/Sep/2023:14:23:45 +0200] "GET /index.html HTTP/1.1" 200 2326
    10.0.0.2 - - [15/Sep/2023:14:24:01 +0200] "POST /api/login HTTP/1.1" 401 123

Requerimientos:
    Usa regex para capturar los componentes.
    Ignora líneas que no coincidan con el formato.
"""

import re
def parsear_log(log_line):
    # Patrón para extraer IP, fecha, método HTTP
    patron = r'^(\S+) .* \[(.*?)\] "(\w+) .* HTTP/1\.\d"'
    """
    ^ -> Inicio de busqueda
    (\S+) -> Capturar la IP (Primer grupo), asumiendo que es el primer elemento no-espacio (\S+)
    .* \[(.*?)\] -> Ignorar elemento intermedio y captura la fecha/hora dentro del [ ]
    "(\w+) -> Captura el método HTTP (GET, POST, DELETE, FETCH, ect...)
    .* HTTP/1\.\d -> Ignora el resto de la solicitud hasta la versión HTTP
    $ -> fin de busqueda
    """
    coincidencia = re.search(patron, log_line)

    if coincidencia:
        ip = coincidencia.group(1)
        fecha_hora = coincidencia.group(2)
        metodo_http = coincidencia.group(3)
        return ip, fecha_hora, metodo_http
    else:
        return None
    
# Pruebas
logs = [
    '192.168.1.1 - - [15/Sep/2023:14:23:45 +0200] "GET /index.html HTTP/1.1" 200 2326',
    '10.0.0.2 - - [15/Sep/2023:14:24:01 +0200] "POST /api/login HTTP/1.1" 401 123',
    'INVALID_LINE [corrupta] "BAD_REQUEST"',
    '172.16.0.5 - - [15/Sep/2023:14:25:10 +0200] "DELETE /api/user/123 HTTP/1.1" 204 0'
]

for log in logs:
    resultado = parsear_log(log)
    print(f"Línea: {log}")
    if resultado:
        print(f"IP: {resultado[0]}")
        print(f"Fecha/Hora: {resultado[1]}")
        print(f"Método HTTP: {resultado[2]}")
    else:
        print("Formato de Log Invalido")
    print("-" * 50)