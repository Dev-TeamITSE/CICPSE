CREATE DATABASE cicpseRegistro;
USE cicpseRegistro;
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombreCompleto VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    area VARCHAR(255) NOT NULL   
);
