-- SQL es un lenguage estándar para comunicarse con la base de datos relacionales!!!
-- ¿Para qué Sirve? -> Con SQL puedes gestionar prácticamente cualquier sistema que necesite almacenamiento y consultar información: Bancos, e-shop, aerolineas, hospitales, organizaciones gobs. 

-- Las 5 categorías de SQL!!
-- DDL (Data Definitaion Language): Define la estructura de tu base de datos. Son los comandos con los que creas tablas, las modificas o las elminias. Escruir tablas o estructuras relacionadas (tablas vacias)
-- DML (Data Manipulation Language): Manipulas los datos dentros esas estructuras. Con el insetar registro nuevos, actulizar los existentes o eliminar
-- DQL (Data Query Language): CUltas y recupera información. El comando SELECT es más usando en todo SQL; con él haces preguntras a la base de datos
-- DCL (Data Control Language): Control QUIÉN puede hacer QUÉ. Con GRANT das permisos y con REVOKE los quitas.
-- TCL (Transaction Control Language): Gestionas las trancacciones, que son grupos de operaciones que deben ejecutarse juntas o no ejecutarse del todo. Por ejemplo, en una transferencia bancaria: descontar dinero de un cuenta y agregarlo a otra deben ocurrir juntas; sin que una falla, ambas deben revertirse.

-- BUENAS PRACTICAS SQL
-- Legibilidad:  Escribir las palabras resevardad de SQL en mayúsculas (SELECT, FROM, WHERE) y los nombres de tus tablas/columnas en minúsculas SELECT FROM db.hyteck WHERE order_trabajo DELETE *;
-- Nombres descripivos: Llama a tus tablas y columnas con nombres que expliquén. nombre_cliente es infinitamente mejor que nc o campo2
-- Identanción: Divide las consultar largas en varias líneas con sangría. Una consulta bien identada puede leerse casi como texto en español
-- NO USES SELECT * EN PRODUCCIÓN!!!!: Pedir todas las columnas es cómodo para explorar, pero en sistemas reales especifica extatmente que columnas necesitas.!

/* 
    id   nombre edad  cuidad
    1    Luis     28    Madero
    2    Arturo   19    MTY
*/

-- MySQL (muy usado en Web)
-- PostgreSQL (más robusto, ideal para proyectos grandes)
-- SQL Server (MUY CARO la licencia se vende POR procedador del servidor!!!!)
-- SQLite (ligero, para pruebas NOOOO Para produccion - Bueno para aprender y/o estudio)

-- DDL: Comandos principales: CREATE -> Crear | ALTER -> Modificar | DROP -> Eliminar 
-- Ejemplo DDL código

CREATE TABLE clientes (
    --TDA -> Tipo de datos Abtracto
    id INT PRIMARY KEY,
    nombre VARCHAR(100), -- <- 100 Caracteres para nombre
    edad INT
);

-- DML: Comandos pricipales: INSERT -> Insertar | UPDATE -> Actualizar | DELETE -> Eliminar
--  Ejemplo DML código

-- Insertar
INSERT INTO clientes(id, nombre, edad)
VALUES (1, 'Luis', 28);

-- Actualizar
UPDATE clientes
SET edad = 29
WHERE id = 1

-- Eliminar
DELETE FROM clientes
WHERE id = 1;

-- DQL: Comando prcipal: SELECT -> Seleccionar
-- Ejemplo DQL código

SELECT * FROM clientes;

-- DCL: Comando principales: GRANT -> Dar | REVOKE -> Quitar
-- Ejemplo DCL código

GRANT SELECT ON clientes TO usuario1; -- <- Le da permiso a usuario1 para ver los datos de la tabla clientes
REVOKE SELECT ON clientes TO usuario2; -- <- Le quito permiso a usuario 2 para que no vea los datos de la tabla clientes

-- TCL: Comandos princcipales: COMMIT -> Guardar cambios | ROLLBACK -> Deshacer | SAVEPOINT -> Punto intermedio
-- EJemplo TCL código

BEGIN; -- TCL
UPDATE clietes SET edad = 30 WHERE id = 1; -- DML
ROLLBACK; -- TCL

