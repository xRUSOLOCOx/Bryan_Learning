CREATE TABLE usuario(

id_usuario INT AUTO_INCREMENT NOT NULL,
nombre_usuario VARCHAR(50) NOT NULL,
correo_usuario VARCHAR(255),
contraseña VARCHAR(255) NOT NULL DEFAULT 0000,
rol VARCHAR(20) DEFAULT "User", 

PRIMARY KEY(id_usuario),
UNIQUE(correo_usuario)
);

CREATE TABLE cliente(

id_cliente INT NOT NULL AUTO_INCREMENT,
nombre_cliente VARCHAR(100) NOT NULL,
telefono_cliente VARCHAR(20),
email_cliente VARCHAR(255),

PRIMARY KEY(id_cliente),
UNIQUE(telefono_cliente)
);

CREATE TABLE empleado(

id_empleado INT NOT NULL AUTO_INCREMENT,
nombre_empleado VARCHAR(100) NOT NULL,
telefono_empleado VARCHAR(20) NOT NULL,
direccion_empleado VARCHAR(150) NOT NULL,
email_empleado VARCHAR(255),
salario INT NOT NULL DEFAULT 0,
cargo VARCHAR(30) DEFAULT "Empleado",

PRIMARY KEY(id_empleado),
UNIQUE(telefono_empleado),
UNIQUE(email_empleado)
);

CREATE TABLE proveedor(

id_proveedor INT NOT NULL AUTO_INCREMENT,
nombre_proveedor VARCHAR(100) NOT NULL,
telefono_proveedor VARCHAR(20) NOT NULL,
direccion_proveedor VARCHAR(150),
email_proveedor VARCHAR(255),
tipo_proveedor ENUM("Natural","Juridico"),

PRIMARY KEY(id_proveedor),
UNIQUE(telefono_proveedor),
UNIQUE(email_proveedor)
);


CREATE TABLE producto (

    id_producto INT NOT NULL AUTO_INCREMENT,
    nombre_producto VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    descripcion TEXT,
    marca VARCHAR(50),
    tipo_producto VARCHAR(50),
    precio INT NOT NULL DEFAULT 0,
    id_proveedor INT NOT NULL,
    
    PRIMARY KEY(id_producto),
	FOREIGN KEY(id_proveedor) REFERENCES proveedor(id_proveedor)
    
);


CREATE TABLE factura(

    id_factura INT NOT NULL AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    fecha_factura DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    tipo_factura ENUM("Fisica","Electronica") NOT NULL,
    estado_factura ENUM('Pendiente', 'Pagada', 'Cancelada') NOT NULL,
    subtotal INT NOT NULL DEFAULT 0,
    monto_total INT NOT NULL DEFAULT 0,
    monto_pagado INT NOT NULL DEFAULT 0,
    cambio INT AS (monto_pagado - monto_total) STORED,
    metodo_pago VARCHAR(20),
    
    PRIMARY KEY(id_factura),
    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente)
);


CREATE TABLE pagos(

    id_pago INT NOT NULL AUTO_INCREMENT,
    id_factura INT NOT NULL,
    metodo_pago VARCHAR(20),
    monto_total INT NOT NULL,
    detalles_pago TEXT,
    
    FOREIGN KEY(id_factura) REFERENCES factura(id_factura),
    PRIMARY KEY(id_pago)
);


CREATE TABLE venta (

    id_venta INT NOT NULL AUTO_INCREMENT,
    id_factura INT NOT NULL,
    id_producto INT NOT NULL,
    id_empleado INT NOT NULL,
    cantidad INT NOT NULL DEFAULT 0,
    subtotal INT NOT NULL DEFAULT 0,
    
    FOREIGN KEY(id_factura) REFERENCES factura(id_factura),
    FOREIGN KEY(id_producto) REFERENCES producto(id_producto),
    FOREIGN KEY(id_empleado) REFERENCES empleado(id_empleado),
    PRIMARY KEY(id_venta)
);