/*
    SELF JOIN - Una tabla unida consigo misma, es una tecnica INNER JOIN o LEFT JOIN sobre la misma tabla, tratándola como si fuera dos tablas diferentes

    ¿Cuando se usa? -> Cuando una tabla tiene una relación consigo misma. Los casos típicos son:
        - Jerarquias
        - Relaciones entre pares
        - Estructuras de árboles
        - Comprara fials de la misma tabla
    
    Jerarquia de Empleados
    Imagina una tabla 'empleados' donde cada empleado puede tener un jefe que tambiene sta en la misma tabla

    id      nombre      jefe_id
    1       Roberto     NULL
    2       Ana         1
    3       Luis        1
    4       Marta       2
    5       Carlos      2
    6       Sofía       3
*/

/*
    El SELF JOIN duplica internamente la tabla
    Tabla "e" (empleados)    Tabla "j" (jefes)
┌────┬─────────┬───────┐  ┌────┬─────────┬───────┐
│ id │ nombre  │jefe_id│  │ id │ nombre  │jefe_id│
├────┼─────────┼───────┤  ├────┼─────────┼───────┤
│ 1  │ Roberto │ NULL  │  │ 1  │ Roberto │ NULL  │
│ 2  │ Ana     │  1    │←→│ 2  │ Ana     │  1    │
│ 3  │ Luis    │  1    │  │ 3  │ Luis    │  1    │
└────┴─────────┴───────┘  └────┴─────────┴───────┘
        ↑                          ↑
   "el empleado"              "el jefe"
*/

SELECT
    e.nombre AS empleado,
    j.nombre AS jefe
FROM empleados e
INNER JOIN empleados j ON e.jefe_id = j.id;

/*
    empleado          jefe
    Ana               Roberto
    Luis              Roberto
    Marta             Ana
    Carlos            Ana
    Sofía             Luis
*/
-- INNER JOIN descarta los NULL

SELECT
    e.nombre AS empleado,
    j.nombre AS jefe
FROM emepleados e
LEFT JOIN empleados j ON e.jefe_id = j.id;
-- LEFT JOIN rellena con null a la izquierda

/*
    empleado          jefe
    Roberto           NULL
    Ana               Roberto
    Luis              Roberto
    Marta             Ana
    Carlos            Ana
    Sofía             Luis
*/

/*
    FULL OUTER JOIN - Todo de ambas tablas
    ¿Qué es? Combina lo mejor de LEFT JOIN y RIGHT JOIN: devuelve todas las filas de ambas tablas, emparejando donde hay coincidencia, y rellenando con NULL donde no la hay.

    ¿Cuando se usa? Cuando necestias panorama completo de dos tablas, sin perder información de ninguno de los dos latos, Casos tipicos
        - Auditorias
        - Conciliaciones
        - Migraciones
        - Reportes completos

    Tabla empleados
    id      nombre      departamento_id
    1       Ana         1
    2       Luis        2
    3       Sofía       NULL

    Tabla departamentos
    id      nombre
    1       Ventas
    2       IT
    3       RRHH
*/

SELECT
    e.nobre AS empleado,
    d.nombre AS departamento
FROM empleados e
FULL OUTER JOIN departamentos d ON e.departamento_id = d.id;

/*
    empleado        departamento
    Ana             Ventas
    Luis            IT
    Sofía           NULL
    NULL            RRHH
*/

-- Caso de un real: encontrar huérfanos en ambos lados
SELECT
    e.nobre AS empleado_sin_depto,
    d.nombre AS depto_sin_empleados
FROM empleados e
FULL OUTER JOIN departamentos d ON e.departamento_id = d.id
WHERE e.id IS NULL OR d.id is NULL;

/*
    empleado_sin_depto      depto_sin_empleados
    Sofía                   NULL
    NULL                    RRHH
*/

/*
    CROSS JOIN - Producto cartesiano
    ¿Qué es? -> Devuelve todas las combinaciones posibles entre las filas de dos tablas. No usa condición ON. Si la tyabla A tiene n filas y tabla B tiene m filas, resultado tendrá n x m filas

    ¿Cuando se usa? -> Con diferencia de otros JOINs, CROSS JOIN no busca relaciones existentes, sino que genera combianaciones. Caso típicos:
        - Generar combianaciones
        - Crear matrices de datos
        - Simulaciones
        - Rellenar huecos en series temporales

    Ejemplo práctico: catálogo de combianacioones

    Tabla tallas:
    talla
    S
    M
    L

    Tabla colores:
    color
    Rojo
    Azul
    Verde
    Negro
*/

SELECT t.talla, c.color
FROM talla t
CROSS JOIN colores c;

/*
    Resultado 3x4=12 filas

    talla          color
    S              Rojo
    S              Azul
    S              Verde
    S              Negro
    .              .
    .              .
    .              .

    Cada talla se combina con cada color -> todas las combinaciones posibles de un catálago
*/

-- Otro ejemple: generar la matriz de turno
/*
    Tabla empleados:
    nombre
    Ana
    Luis
    Arturo

    Tabla dias:
    Lunes
    Martes
    Miercoles
    Jueves
    Viernes
    Sabado
*/

SELECT e.nombre, d.dia
FROM empleados e
CROSS JOIN dias d;

-- 3x6=18 combinaciones posibles para las tablas de emeplados x turnos

SELECT * FROM tallas CROSS JOIN colores;

SELECT * FROM tallas, colores;