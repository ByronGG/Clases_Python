/*
    DQL: Data Query Language: Sirve para consultar y recuperar datos. Su único comando principal es SELECT, pero es el más poderoso y verstil en todo SQL
*/

--Estructura básica
SELECT columnas FROM tabla;

/*
TABLA EMPLEADOS
    id      nombre      departamento        salario     cuidad
    1       Arturo      IT                  3000        MTY
    2       Luis        CTO                 8000        TAM
    3       Reyna       RRHH                4500        TAM
    4       Carlos      Ventas              2500        CDMX
    5       Sofia       Ventas              2800        GDL
*/

-- Traer todas las columnas
SELECT * FROM empleados;

-- Traer solo algúnas columas
SELECT nombre, salario FROM empleados;

-- WHERE filtrar filas
SELECT nombre, salario FROM empleados WHERE depatamento = 'IT'

--Operadores que puedes usar en WHERE

/*
    Operador        Significado         Ejemplo
    =               igual               salario = 3000
    <> o !=         Distinto            cuidad <> 'TAM'         (simbolos sin FiraCode < >   ! = (Debén ir juntos))
    >, < >=, <=     Comparación         salario >= 3000
    BETWEEN         En un rango         salario BETWEEN 3000 AND 4500
    IN              En una lista        cuidad IN ('MTY', 'TAM', 'CDMX')
    LIKE            Patrón de texto     nombre LIKE 'M%'
    IS NULL         Sin valor           cuidad is NULL
    AND, OR, NOT    Lógicos             salario > 3000 AND cuidad = 'GDL'
*/

-- Empleados de MTY con salario mayor a 2900
SELECT nombre, salario FROM empleados WHERE cuidad = 'MTY' AND salario > 2900;

-- ORDEN BY - Ordenar resultados
SELECT nombre, salario FROM empleados
ORDER BY salario DESC; -- DESC = mayor a menor / ASC = menor a mayor (por defecto)

-- Puedes ordenar varias columnas
ORDER BY departamento ASC, salario DESC;

-- DISTINCT - Eliminar duplicados
SELECT DISTINCT cuidad from empleados; -- Devuleve MTY, TAM, CDXM, GDL

-- LIMIT/TOP Limitar filas devueltas
-- MySQL/PosgreSQL
SELECT nombre, salario FROM empleados
ORDER BY salario DESC LIMIT 3; --Los 3 empleados mejor pagados (DESC los ordena del mayor al menor)

-- Funciones de agregación - Calculan un valor a partir de múltiples filas:
/*
    Función                 Qué hace
    COUNT()                 Cuenta filas
    SUM()                   Suma valores
    AVG()                   Promedio
    MAX()                   Valor máximo
    MIN()                   Valor minimo
*/

SELECT
    COUNT(*) AS total_empleados,
    AVG(salario) AS salario_promedio,
    MAX(salario) AS salario_maximo,
    MIN(salario) AS salario_minimo
FROM empleados;

-- GROUP BY - Agrupar resultados
-- Se usa simpre juntos a funciones de agregación para calcular grupos

SELECT depatamento, COUNT(*) AS total, AVG(salario) AS promedio
FROM empleados
GROUP BY departamento;

/*
    detapatamento           total       promedio
    Ventas                  2           3100
    It                      1           3000
    RRHH                    1           4500
    CTO                     1           8000
*/

-- Alias con AS: Renombrar columnas o tablas para que sean más legibles y crear variables
SELECT nombre AS empleado, salario * 12 AS salario_anual FROM empleados AS e;

/*
    EJEMPLOS DE MATA-JRs => APRENDER DE MEMORIA ESTAS REGLAS!!!!
*/
-- HAVING Filtrar grupos
-- WHERE filtra filas ANTES de agrupar. HAVING filtra grupos DESPúES de agrupar
SELECT depatamento, AVG(salario) AS promedio
FROM empleados
GROUP BY departamento
HAVING AVG(salario) > 3000;

-- El orden de ejecución si es muy importante en SQL (MUY IMPORTANTE!!!!)
-- Aunque escribes en este orden:
SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY -> LIMIT

SELECT * FROM empleados WHERE cuidad = 'TAM' GROUP BY departamento HAVING salario > 3500 ORDER BY ASC LIMIT 3;

-- SQL solo ejecuta en este orden
FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT
-- Esto explica por qué no puedes usar un alias del SELECT dentro del WHERE - El WHERE se ejecuta antes que el SELECT

/*
    FROM        →  ¿De qué tabla?
    WHERE       →  ¿Qué filas?
    GROUP BY    →  ¿Cómo agrupo?
    HAVING      →  ¿Qué grupos me quedan?
    SELECT      →  ¿Qué columnas muestro?
    ORDER BY    →  ¿En qué orden?
    LIMIT       →  ¿Cuántas filas?
*/

/*
    EJEMPLOS DE MATA-JRs => APRENDER DE MEMORIA ESTAS REGLAS!!!!
*/