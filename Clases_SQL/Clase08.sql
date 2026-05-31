/*
    Subconsultas (Subqueries) y Visas (Views)
    Son dos heramientas potentes que permiten escribir consultas más limpias, reutilizables y expresivas.
    ¿Qué es una subconsulta? => Es una consulta dentro de otra consulta. Se escribe entre parentesis y sus resultado lo usa la consulta principal

    SELECT nombre
    FROM empleados
    WHERE salario > (SELECT AVG(salario) FROM empleados);
        └──────────────── consulta externa ────────────────┘
                            └──── subconsulta ────┘

    La idea clave: SQL ejecuta primero la subconsulta, obtiene un resultado, y luego la consulta externa lo utiliza
*/

-- Ejemplo de tablas
/*
    Tabla empleados
    id      nombre      depatamento_id    salario
    1       Ana         1                 3000
    2       Luis        2                 4500
    3       Marta       1                 3200
    4       Carlos      2                 5000
    5       Sofía       3                 2800

    Tabla departamentos
    id      nombre      cuidad
    1       Ventas      México
    2       It          Tampico
    3       RRHH        Monterrey                   
*/

-- Tipo 1: Subconsulta escalar (devuleve un solo valor)
-- Es la más simple. La subconsulta devuelve un único valor (una fila, una columna), que se compara directamente.

-- Empleados que ganan más que el promedio 
SELECT nombre, salario
FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados);

/*
    PASO a PASO
    1. La subconsulta calcula AVG(salario) = (3000 + 4500 + 3200 + 5000 + 2800) / 5 = 3700
    2. La consulta externa se conviete en WHERE: salario > 3700

    Resultado
    nombre      salario
    Luis        4500
    Carlos      5000

    Esto no se puede hacer en una sola consultado simple, porque 'WHERE salario > AVG(salario)' daría error: no puedes usar una función de agregación directamente en el WHERE.
*/

-- Tipo 2: Subconsulta de columna (devuelve una lista de valores)
-- Devuelve varios valores en una columna. Se usa con operadores como IN, NOT IN, ANY, ALL

-- Empleados que trabajan en departamenteso de México y Tampico
SELECT nombre
FROM empleados
WHERE departamento_id IN (SELECT id FROM departamentos   WHERE cuidad IN('México', 'Tampico'));

/*
    PASO A PASO
    1. La subconsulta devuelos los ids de departamentos de México o Tampico (1, 2)
    2. La consulta externa: Where departamentos_id IN (1,2)
    Resultados: Ana, Luis, Marta, Carlos

    MATA JRs en pruebas tecnicas!!!!!
    Cuidado con NOT IN y NULL
    NOT IN se comporta de forma extraña si la subconsulta devuelve algún NULL. Si la lista contiene un NULL, NOT IN puede devolver 'cero filas inesoperadamente'. Por seguridad, filtra los NULL o usa NOT EXIST
*/

-- Tipo 3: Subconsulta de fila/tabla (devuelve varias filas y columnas)
-- Devuelve un conjuto que se usa como si fuera una tabla. Típicamente en la cláusula FROM

-- Promedio de salario por detapartamento, pero solo los que superan 3500
SELECT sub.departamentos_id, sub.promedio
FROM (
    SELECT departamento_id, AVG(salario) AS promedio
    FROM empleados
    GROUP BY deparatamento_id
) AS sub
WHERE sub.promedio > 3500;

-- A esto se le llama una subconsulta derivada 'pro' o tabla derivada. Es obligatorio darle una alias (AS sub), porque SQL necesita un nombre para tratarla como tabla.

-- Como escribir o formas de escribir una subconsulta
-- En el WHERE (lo más comun)
SELECT nombre FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados);

-- En el FROM (tabla derivada)
SELECT * FROM (SELECT nombre, salario FROM empleados WHERE salario > 3000) AS altos;

-- SELECT (subconsulta escalar como columna)
SELECT
    nombre,
    salario,
    (SELECT AVG(salario) FROM empleados) AS promedio_general,
    salario - (SELECT AVG(salario) FROM empleados) AS diferencia
FROM empleados;
-- Cada fila muestra el salario del empleado y cuánto se desvía del promedio general.

-- En el HAVING
SELECT departamento_id, AVG(salario) AS promedio
FROM empleados
GROUP BY depatamentos_id
HAVING AVG(salario) > (SELECT AVG(salario) FROM empleados);

/*
    EXISTS y NOT EXISTS
    EXISTS comprueba si una subconsulta devuelve al menos una fila. NO LE IMPORTA EL CONTENIDO, solo si hay resultados o no. Devuelve True o False
*/

-- Departamentos que TIENEN al menos un empleado
SELECT d.nombre
FROM departamentos d
WHERE EXISTS(
    SELECT 1 FROM empleados e WHERE e.departamento_id = d.id
);

-- Se suele escribir SELECT 1 dentro del EXISTS porque el contenido no importa, solo si hay filas

-- Departamento SIN empleados
SELECT d.nombre
FROM deparamentos d
WHERE NOT EXISTS (
    SELECT 1 FROM empleados e WHERE e.depatamento_id = d.id
);

/*
    EXISTS vs IN
    Ambos puedes resolver promeas parecidos, pero:
        * EXISTS suele ser más eficiente con tablas grandes y maneja mejor el NULL
        * IN es más legible para listas pequeñas y fijas
*/

-- VISTAS
/*
    ¿Qué es una vista?
    Una vista es una consulta guardada con nombre que se comparta como si fuera una tabla. No almacenada datos propios (en la mayoría de los casos): es una "tabla virtual" que ejecuta su consulta cada vez que la consultas.

    Piensa como accesos directos a una consulta compleja
    ¿Para que sirve?
        - Simplificar consultas complejas: encapsula un JOIN complicado y lo reutilizas con un nombre simple
        - Seguridad: puedes dar acceso a una vista que muestre solo ciertas columnas, ocultado datos sensibles
        - Reutilizacion: si usas la misma consulta en muchos lugares, la defines una vez
        - Abstracción: si la estructura de las tablas cambia, actualizas la vista y el resto del código sigue funcionando
*/

-- Crear una vista (view)
CREATE VIEW empleados_con_departamentos AS
SELECT
    e.nombre AS empleado,
    e.salario,
    d.nombre AS departamento,
    d.cuidad
FROM empleados e
INNER JOIN departamentos d ON e.departamento_id = d.id;

-- Puedes consultarla como si fuera una tabla normal
SELECT * FROM empleados_con_departamentos;
-- Incluso aplicarle filtros, ordenes, etc.
SELECT empleado, salario
FROM empleados_con_departamentos
WHERE cuidad = "Monterrey"
ORDER BY salario DESC;

/*
    Resultado de la vista empleados_con_departamentos
    empleado    salario     departamento    cuidad
    Ana         3000        Ventas          México
    Luis        4500        It              Tampico
    Marta       3200        Ventas          México
    Carlos      5000        It              Tampico
    Sofía       2800        RRHH            Monterrey

*/

/*
Tú escribes:                    SQL realmente ejecuta:
┌──────────────────────┐       ┌────────────────────────────────┐
│ SELECT * FROM        │       │ SELECT * FROM (                │
│ empleados_con_       │  -->  │   SELECT e.nombre, e.salario,  │
│ departamento         │       │   d.nombre, d.ciudad           │
│ WHERE ciudad =       │       │   FROM empleados e             │
│ 'Monterrey'          │       │   JOIN departamentos d ON ...  │
└──────────────────────┘       │ ) WHERE ciudad = 'Monterrey'   │
                               └────────────────────────────────┘
*/

-- Modificar y eliminar vistas
-- Modificar una vista existen (algunos motores usan CREATE or REPLACE)
CREATE OR REPLACE VIEW empleados_con_departamentos AS
SELECT e.nombre, e.salario, d.nombre AS departamento
FROM empleados e
INNER JOIN departamentos d ON e.departamento_id = d.id;

-- Eliminar una vista
DROP VIEW empleados_con_departamentos;
-- Eliminar una vista no afecta a als tablas base. Solo borra la consulta guardada

-- Seguridad: Ocultar datos sensibles
-- Imagina que un becario llamado Arturo necesita ver la lista de empleados, pero no debe ver los salario. Tu como SR debes crear una vista sin esa columna

CREATE VIEW directrio_empleados AS
SELECT e.nombre, d.nombre AS departamento, d.cuidad
FROM empleados e
INNER JOIN departamentos d ON e.departamento_id = d.id;

-- Luego le das permiso al becario Arturo solo sobre directrio_empleados, no sobre la tabla empleados. Así nunca verá los salario y borrara por accidente la BD

/*
    PREGUNTA MATA JRS!!!!!
    Vistas actualizables vs solo lectura
    Algunas visas perminten hacer INSERT, UPDATE o DELETE que afecta a las tables base. Pero hay condiciones estrictas:
    Una vista suele ser actualizable si:
        - Está basada en una sola tabla
        - No usa GROUP BY, DISTINCT, funciones de agregación ni JOIN
        - No tiene subconsultas en el SELECT
*/