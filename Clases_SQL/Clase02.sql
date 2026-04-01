-- Tipos de Datos definen qué tipo de información puede guardar una columna

edad INT -- Aquí solo se pueden guardar números enteros INT

/* 
    Para qué sirven?
    1. Mantener orden y consistencia entre datos (Datos limpios = sistema estable)
    2. Validar datos automáticamente (Evitar errores ej. no meter texto en edad)
    3. Otimizar rendimiento (SQL usa menos memoria si eliges bien el tipo de dato)
*/

-- INT (Eneteros)
edad INT --1, 25, 100, etc. // 3.1416 "texto"

-- DECIMAL / NUMERIC (Precisión excta) DECIMAL es muy usado en dinero
precio DECIMAL (10, 2) -- 10 digitos, 2 decimales = 9999999999.99

-- FLOAT / DOUBLE (Decimales aproximados)
temperatura FLOAT -- Sensores, datos, ecuaciones

-- VARCHAR (Texto variable)
nombre VARCHAR(100) -- "Luis" "Hy teck" // 100 (X número) la logitud de la cadena máxima

-- CHAR (Texto fijo)
codigo CHAR(10) -- Siempre ocupa 10 caracteres // códigos fijos, RFC, CURP, FOLIO

-- TEXT (Texto largo)
descripcion TEXT -- Texto grandes // comentarios, descripciones de prodctos, ect

-- DATE
fecha DATE -- 2026-04-01

-- DATETIME / TIMESTAMP
created_at TIMESTAMP -- Fecha + hora // 2026-04-01 11:40:24

-- BOOLEAN
activo BOOLEAN -- TRUE / FALSE

-- TIPO DE DATOS ESPECIALES NOTA: DEPENDE DEL MOTOR!!! JSON(PostgreSQL/MySQL)
datos JSON

{
    "nombre": Luis,
    "edad": 28
}

-- ENUM
estado ENUM ('pendiente', 'proceso', 'completado')

-- VALIDACIONES EN SQL
-- NULL
nombre VARCHAR(100) NOT NULL -- No permite valores vacios
fecha DATE NULL -- Permite No guardar la fecha

-- PRIMARY KEY
id INT PRIMARY KEY -- No se repite y no permite NULL
OT INT PRIMARY KEY -- 5367 (NO NULL)

-- UNIQUE
email VARCHAR(100) UNIQUE -- NO permite duplicados

-- CHECK
edad INT CHECK (edad >= 18) -- Solo permite valores válidos

-- FOREIGN KEY
cliente_id INT,
FOREIGN KEY (cliente_id) REFERENCES -- Relacionar tablas
cliente(id)

-- DEFAULT
activo BOOLEAN DEFAULT TRUE -- Valor automatico lo pone VERDADERO

-- EJEMPLO DE TABLA "Realista"

CREATE TABLE usarios (
    id INT PRIMARY KEY, -- ID, UNICA, NO NULL, NO NEGATIVO
    nombre VARCHAR(100) NOT NULL, -- TEXTO VARIABLE HASTA 100 CARACTERES NO NULL
    email VARCHAR(100) UNIQUE, -- TEXTO VARIABLE HASTA 100 CARACTERES Y NO SE PUEDE REPETIR
    edad INT CHECK (edad >= 18), -- NUMERICO, VALIDA QUE SEA MAYOR O IGUAL A 18
    usuario_activo BOOLEAN DEFAULT TRUE, -- PONEN AUTOMATICAMENTE TRUE
    fecha_registro TIMESTAMP -- REGISTRA FECHA Y HORA
);

-- SQL NO VALIDARA EN COPILACIÓN Y PERDERAS VALIDACIÓN DE DATOS
edad VARCHAR(10) -- <- edad = "xd"

/*
    ¿Qué es WHERE?
    Where sirve para filtrar datos "Dame SOLO los registros que cumplan esta condición"
*/

SELECT * FROM clientes
WHERE cuidad = "MTY";

-- Operaciones básicas WHERE

WHERE edad = 25 -- Trae la consulta donde la edad sea igual a 25
WHERE edad != 25 -- Trae la consulta donde la edad sea diferente a 25
WHERE edad > 18 -- Trae la consulta donde la edad sea mayor a 18
WHERE edad < 18 -- Trae la consulta donde la edad sea menor a 18

-- AND Todas las condiciones deben cumplirse
SELECT * FROM clientes
WHERE cuidad = "MTY" AND edad >= 18;

-- OR Se cumple al menos una condición
SELECT * FROM clientes
WHERE cuidad = "MTY" OR cuidad = "CDMX"

-- LIKE Búsquedas por patrón - Sirve para buscar texto parcial
-- % = cualquier cosa

WHERE nombre LIKE 'Lu%' -- Luis, Lucia, Lucho
WHERE nombre LIKE '%ez' -- Perez, Gomez
WHERE nombre LIKE 'a%o' -- Arturo
WHERE nombre LIKE '%ui%' -- Luis, Ruiz

-- BETWEEN Rango para valores entre dos límites
SELECT * FROM clientes
WHERE edad BETWEEN 20 AND 30 -- BETWEEN INCLUYE LOS VALORES PUESTOS (INCLUYE EL 20 Y EL 30)

WHERE fecha BETWEEN '2026-01-01' AND '2026-12-31'

-- IN Lista de valores Es como muchos OR en una sola linea
WHERE ciudad = 'CDMX' OR ciudad = 'MTY' OR ciudad = 'GDL'

WHERE ciudad IN ('CDMX', 'MTY', 'GDL')

-- EJEMPLO COMPLETO
SELECT * FROM clientes -- SELECCIONA TODA LA TABLA DE CLIENTES
WHERE edad BETWEEN 20 AND 40 -- REVISA LAS EDAD ENTRE 20 Y 40
AND ciudad IN ('CDMX', 'TAM') -- EN LA LISTA DE CUIDADES DE CDMX O TAMPICO
AND nombre LIKE 'A%'; -- NOMBRES EMPIECE CON A HASTA CUALQUIER PATRÓN DE LETRAS

-- FIX THIS
WHERE ciudad = 'TAM' OR ciudad = 'MTY' AND edad > 30 -- Forma JR larga y confusa
WHERE ciudad IN('TAM', 'MTY') AND edad > 30 -- Forma Sr
