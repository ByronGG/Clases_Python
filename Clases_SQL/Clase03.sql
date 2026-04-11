/* 
    Data Definition Language: Sirve para crear, midificar y eliminar escructuras dentro de una base de datos. No se enfoca en los datos en sí, sino en el DISEÑO de la base de datos
    
    DDL sirve para trabajr con objetos como:
        - baso de datos
        - tablas
        - columnas
        - índices
        - vistas
        - esquemas
        - restricciones

    Comandos principales de DDL
        - CREATE
        - ALTER
        - DROP
        - TRUNCATE
        - RENAME (esto en algunos motores)
*/

-- CREATE: sirve para crear objetos nuevos
-- CREATE DATABASE -> CREATE TABLE -> CREATE INDEX -> CREATE VIEW

CREATE DATABASE db_empresa; -- Esto crea una base de datos llamda db_empresa
CREATE DATABASE empresa_test; -- Algúnos motores crear un segundo entorno para pruebas
USE empresa --MySQL necesita contexto para saber que db usar

-- CREATE Tablas :  Ejemplo básico
 
-- Tabla básica (mala practica)
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nombre VARCHAR(100), -- dejar vacio
    correo VARCHAR(100), -- repetir correos
    edad INT -- entrar gente menor de edad y/o gente con edad de 1,000,000 años
);

-- Tabla básoca (con buenas practicas)
CREATE TABLE clientes(
    id INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE,
    edad INT CHECK(edad >= 18),
    activo BOOLEAN DEFAULT TRUE
);

-- FOREING KEY: Esto se usa para relacionar tablas
CREATE TABLE pedidos(
    id INT PRIMARY KEY,
    cliente_id INT,
    total DECIMAL(10, 2),
    FOREIGN KEY(cliente_id) REFERENCES clientes(id)
);

-- Anatomía completa de una tabla (real)
CREATE TABLE empleados(
    id INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    correo VARCHAR(150) UNIQUE NOT NULL,
    salario DECIMAL(10, 2) CHECK (salario > 0),
    fecha_ingreso DATE NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    departamento_id INT,
    FOREIGN KEY(departamento_id) REFERENCES departamentos(id)
);


-- ALTER: sirve para modificar una estructra existente
/*
    Con ALTER puedes:
        - agregar columnas
        - comabiar tipos de datos
        - renombrar columnas
        - agregar resticciones
        - eliminiar restricciones
        - eliminar columnas

    Es uno de los comandos más usados cuando la base ya está en marcha
*/

-- Agregar una COLUMNA de la tabla
ALTER TABLE clientes
ADD telefono VARCHAR(20);

-- Modificar el tipo de dato
ALTER TABLE clientes
ALTER COLUMN nombre TYPE VARCHAR(150);

-- MySQL usa MODIFY
ALTER TABLE clientes
MODIFY nombre VARCHAR(150);

-- Renombrar una columna
ALTER TABLE clientes
RENAME COLUMN correo to email;

-- Agregar resticción
ALTER TABLE clientes
ADD CONSTRAINT uq_correo UNIQUE (correo);

-- Agregar un foreign key
ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_clientes
FOREIGN KEY(clientes_id) REFERENCES clientes(id);

-- Eliminar columnas
ALTER TABLE clientes
DROP COLUMN telefono; -- DROP != DELETE enable => disaeble

/*
    DROP: sirve para eliminar objetos completos
    Es un comnado potente y peligroso!!!!!!!!!
    Puede borrar:
        * base datos
        * tablas
        * vistas
        * índices
*/

DROP TABLE clientes; -- Esto elimina: la tabla, su estructura, rompe relaciones, todos sus datos

DROP DATABASE hyteck; -- Esto elimina: TODA LA BASE DATOS y da inicio a tu nueva vida como cliente