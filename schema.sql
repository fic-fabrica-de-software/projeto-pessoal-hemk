CREATE DATABASE projeto_curso;

USE projeto_curso;

    CREATE TABLE usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        data_nascimento DATE,
        senha VARCHAR(255) NOT NULL
    ) 