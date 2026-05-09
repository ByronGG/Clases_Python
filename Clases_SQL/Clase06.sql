/*
    JOINs combinar tablas para obtener información relacionada entre ellas. Existen varios tipos de JOINs:
    - INNER JOIN: Devuelve solo las filas que tienen coincidencias en ambas tablas.
    - LEFT JOIN: Devuelve todas las filas de la tabla izquierda y las coincidencias de la tabla derecha. Si no hay coincidencia, devuelve NULL para la tabla derecha.
    - RIGHT JOIN: Devuelve todas las filas de la tabla derecha y las coincidencias de la tabla izquierda. Si no hay coincidencia, devuelve NULL para la tabla izquierda.
    - FULL OUTER JOIN: Devuelve todas las filas de ambas tablas, con coincidencias donde existan. Si no hay coincidencia, devuelve NULL para la tabla sin coincidencia.
    - CROSS JOIN: Devuelve el producto cartesiano de ambas tablas, es decir, todas las combinaciones posibles de filas entre las dos tablas.

    ¿Por qué usar JOINs? En base de datos reales, la información nunca vive en una sola tabla. Por ejemplo, podrías tener una tabla de empleados y otra de departamentos. Para obtener el nombre del departamento de cada empleado, necesitarías hacer un JOIN entre ambas tablas.
*/

/*
    Ejemplo de problemas: Si guardas todo en una tabla:
    id      nombre      departamento        jefe_depto     cuidad
    1       Arturo      Ventas                Roberto      TAM
    2       Luis        Ventas                Roberto      TAM
    3       Reyna       IT                    Roberto      TAM
    4       Carlos      IT                    Roberto      TAM
    5       Sofia       RRHH                  Roberto      TAM

    -> "Roberto" y "TAM" se repiten en cada fila, lo que genera redundancia y desperdicio de espacio. Además, si "Roberto" cambia de departamento, tendrías que actualizar varias filas, lo que puede llevar a errores.

    La solución: es seperar en tablas y relacinarlas con JOINs:
    Usaremos tres tablas a partir del ejemplo anterior:

    empleados
    id      nombre      departamento_id   salario
    1       Arturo      1                 3000
    2       Luis        2                 8000
    3       Reyna       1                 5000
    4       Carlos      2                 6000
    5       Sofia       NULL              4000

    depatamentos
    id      nombre      cuidad
    1       Ventas      TAM
    2       IT          MTY
    3       RRHH        CDMX

    proyectos
    id      nombre_proyecto      empleado_id
    1       Web Corporativa           2
    2       APP Móvil                 2
    3       CRM                       4
    4       ERP                       NULL

*/

-- INNER JOIN - Solo los que coinciden en ambas tablas: Es el JOIN más común. Devuleve únicamente las filas donde existen coincidencia en ambas tablas

SELECT empleados.nombre, depatamentos.nombre AS departamento, departamentos.cuidad
FROM empleados
INNER JOIN departamentos ON empleados.departamento_id = departamentos.id;

/*
    Resultado del INNER JOIN
    nombre          departamento            cuidad
    Arturo          Ventas                  TAM
    Luis            Ventas                  TAM
    Reyna           IT                      MTY
    Carlos          IT                      MTY

    Sofia no aparece porque tiene 'departamento_id' = NULL (no conicide con nada). El departamento RRHH tampoco aparece porque ningún empleado le pertenece. REGLA: Si no hay coincidencia en alguno de los dos lados -> la fila se descarta
*/

/*
    LEFT JOIN - Todos de la izquierda, coinciden de las derecha: Devuelve todas las filas de la tabla izquierda (LA DEL FROM), y las coincidencias de la derecha. Si no hay coincidencia, rellene con NULL.
*/

SELECT empleados.nombre, departamentos.nombre AS departamento
FROM empleados 
LEFT JOIN departamentos ON empleados.departamento_id = departamentos.id;

/*
    Resultado
    nombre      departamento
    Arturo      Ventas
    Luis        IT
    Reyna       Ventas
    Carlos      IT
    Sofia       NULL
    Nota: Sofía sí aparece, pero sin departamento (NULL) ¿Cuando usarlo? Cuando quieres todos los registros de una tabla, tengan o no relación con la otra. Muy útil para encontrar registros "huerfanos"
*/

SELECT nombre
FROM empleados
LEFT JOIN departmentos ON empleados.departmento_id = departamento.id
WHERE departamentos.id IS NULL;

/*
    Resultado
    Sofia
*/

/*
    RIGHT JOIN - Todas de la derecha, coincidencias de la izquierda: Es el espejo del LEFT JOIN. Devuelve todas las filas de la tabla derecha, y las coincidencias de la izquierda
*/

SELECT empleados.nombre, departamentos.nombre AS departamento
FROM empleados
RIGHT JOIN departamentos ON empleados.departamento_id = departamentos.id;

/*
    Resultado
    nombre      departamento
    Arturo      Ventas
    Luis        IT
    Reyna       Ventas
    Carlos      IT
    NULL        RRHH
*/