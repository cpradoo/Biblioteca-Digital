CREATE DATABASE if NOT EXISTS biblioteca_digital;
USE biblioteca_digital;

CREATE TABLE if NOT EXISTS usuarios (
    id INT AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    tipo_suscripcion CHAR(10) NOT NULL DEFAULT 'gratuita',
    correo VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT pk_usuarios PRIMARY KEY (id)
);

CREATE TABLE if NOT EXISTS recursos_digitales (
    id INT AUTO_INCREMENT,
    titulo VARCHAR(255) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    premium TINYINT NOT NULL DEFAULT 0,

    CONSTRAINT pk_recursos PRIMARY KEY (id)
);

CREATE TABLE if NOT EXISTS historial_descargas (
    id INT AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    id_recurso INT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT pk_historial PRIMARY KEY (id),
    CONSTRAINT fk_historial_usuario FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    CONSTRAINT fk_historial_recurso FOREIGN KEY (id_recurso) REFERENCES recursos_digitales(id)
);