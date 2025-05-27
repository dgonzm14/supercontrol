-- Cambiar a la base de datos 'master' para poder eliminar 'SuperControl'
USE master;
GO

-- Cerrar conexiones a la base de datos 'SuperControl' (Esto fuerza la desconexi�n)
ALTER DATABASE SuperControl SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
GO

-- Eliminar la base de datos 'SuperControl'
DROP DATABASE IF EXISTS SuperControl;
GO

-- Crear la base de datos 'SuperControl' nuevamente
CREATE DATABASE SuperControl;
GO

-- Usar la base de datos reci�n creada
USE SuperControl;
GO

-- Crear las tablas necesarias

CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY IDENTITY(1,1),
    nombre_cliente VARCHAR(100),
    apellido_cliente VARCHAR(100),
    direccion_cliente VARCHAR(200),
    telefono_cliente VARCHAR(15),
    email_cliente VARCHAR(100)
);

CREATE TABLE empleados (
    id_empleado INT PRIMARY KEY IDENTITY(1,1),
    nombre_empleado VARCHAR(100),
    apellido_empleado VARCHAR(100),
    rol_empleado VARCHAR(50),
    salario_empleado DECIMAL(10, 2)
);

CREATE TABLE categorias (
    id_categoria INT PRIMARY KEY IDENTITY(1,1),
    nombre_categoria VARCHAR(100)
);

CREATE TABLE productos (
    id_producto INT PRIMARY KEY IDENTITY(1,1),
    nombre_producto VARCHAR(100),
    descripcion_producto TEXT,
    id_categoria INT NULL,
    precio DECIMAL(10, 2) DEFAULT 1.00,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

CREATE TABLE stock (
    id_stock INT PRIMARY KEY IDENTITY(1,1),
    id_producto INT,
    cantidad INT,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

CREATE TABLE precios (
    id_precio INT PRIMARY KEY IDENTITY(1,1),
    id_producto INT,
    precio DECIMAL(10, 2),
    fecha DATE,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

CREATE TABLE ventas (
    id_venta INT PRIMARY KEY IDENTITY(1,1),
    id_cliente INT,
    fecha_venta DATE,
    total DECIMAL(10, 2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE detalle_ventas (
    id_detalle INT PRIMARY KEY IDENTITY(1,1),
    id_venta INT,
    id_producto INT,
    cantidad INT,
    precio DECIMAL(10, 2),
    FOREIGN KEY (id_venta) REFERENCES ventas(id_venta),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- Crear la tabla de usuarios para login (añadiendo email y contraseña)
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY IDENTITY(1,1),
    nombre_usuario VARCHAR(100),
    apellido_usuario VARCHAR(100),
    usuario VARCHAR(100) UNIQUE,
    contrasena VARCHAR(100),
    email_usuario VARCHAR(100),
    telefono_usuario VARCHAR(15),
    rol VARCHAR(50)
);



