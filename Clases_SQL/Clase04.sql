/*
    DML: Data Manipulation Language es el conjunto de comandos SQL que se usan para manipular los datos dentro de la tabla
    Para que sirve:
        - Insertar Datos
        - Modificar Datos
        - Eliminar Datos

        INSERT UPDATE DELETE
*/

--INSERT Sirve para agregar registros a una tabla
-- Inserta un solo valor
INSERT INTO clientes(id, nombre, edad)
VALUES (1, 'Arturo', 20);

-- Inserta múltiples filas
INSERT INTO clientes(id, nombre, edad)
VALUES
(2, 'Luis', 28),
(3, 'Pedo', 21);

-- Insertar sin especificar columnas (NO RECOMENDADO)
INSERT INTO clientes
VALUES (4, 'Maria', 30);

-- UPDATE (Actualizar datos) Sirve para modificar registros existentes
-- Acutaliza 1 solo datos
UPDATE clientes
SET edad = 19
WHERE id = 1;

-- Actualizar múltiples columnas
UPDATE clientes
SET nombre = 'Luis Fernando'
    edad = 29
WHERE id = 2;

-- ERROR CRITICO
UPDATE clientes
SET edad = 50;
-- REGLA DE ORO SIEMPRE USAR WHERE!!!!

-- DELETE: Sirve para borrar registros
-- Eliminar un registro especifico
DELETE FROM clientes
WHERE id = 1;

-- ERROR CRITICO
DELETE FROM clientes;

-- DML y transacciones
BEGIN;

UPDATE clientes SET saldo = saldo - 100
WHERE id = 1;
UPDATE clientes SET saldo = saldo + 100
WHERE id = 2;

COMMIT;

-- DML y DDL respeta la reglas este ultimo (DDL)
-- EJEMPLO DE PARTE DEL DDL

edad INT CHECK (edad >= 18)

-- Cambio de valores por DML
-- Te piden hacer un insert a la BD que ya tiene hasta ahora 550 registros y agregar al usuario 'Aruturo' a la tabla clientes
-- La tabla clientes tiene 3 columnas id, nombre y edad
INSERT INTO clientes VALUES(551, 'Arturo', 15); -- Este INSERT va a fallar

CREATE TABLE clientes(
    id INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT CHECK (edad >= 18)
);

/*
    Escebnario: Sistema de Ventas 
    - Clientes
    - Productos
    - Órdenes

    Objetivo trbajar con DML
*/

CREATE TABLE clientes(
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    cuidad VARCHAR(100)
);

CREATE TABLE productos(
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2)
);

CREATE TABLE ordenes(
    id INT PRIMARY KEY,
    cliente_id INT,
    producto_id INT,
    cantidad INT,
    fecha DATE,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id),
    FOREIGN KEY(producto_id) REFERENCES productos(id),
);

-- EJERCICIO DE ARTURO
/* 
Luis - Cuidad de Mexico
Ana - Monterrey
Pedro -  Guadalajara
Lucia Cuidad Mexico

Laptop 15000.00
Mouse 300.00
Teclado 800.00

Orden 1 - Luis compro una laptop lo compro ayer
Orden 2 - Ana compro dos mouse lo compro hace 3 dias
Orden 3 - Luis compro un teclado
Orden 4 - Lucia compro un teclado 
*/

INSERT INTO clientes(id, nombre, cuidad) VALUES
(1, "Luis", "CDMX"),
(2, "Ana", "MTY"),
(3, "Pedro", "GDL"),
(4, "Lucia", "CDMX");

INSERT INTO productos(id, nombre, precio) VALUES
(1, "Laptop", 15000.00),
(2, "Mouse", 300.00),
(3, "Teclado", 800.00);


INSERT INTO ordenes(id, cliente_id, producto_id, cantidad, fecha) VALUES
(1, 1, 1, 1, '17-04-2026'),
(2, 2, 2, 2, '15-04-2026'),
(3, 1, 3, 1, '18-04-2026'),
(4, 4, 3, 1, '18-04-2026');
