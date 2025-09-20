<?php
 
    $servidor = "localhost";
    $usuario = "root";
    $senha = "";
    $dbname = "projeto_curso";

    $conexao = new mysqli($servidor, $usuario, $senha, $dbname);

    // Verificar conexão
    if ($conexao->connect_error) {
        die("Falha na conexão: " . $conn->connect_error);    
    }

    $conexao->set_charset("utf8");
?>