<?php
require "config/conexao.php";
session_start();

$erro = "";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    if (isset($_POST["login"])) { //verifica se o botão foi clicado
        $email = trim($_POST["email"] ?? ""); //evita espaços vazios
        $senha = trim($_POST["senha"] ?? "");

        // Verifica se o nome de usuário e senha estão corretos
        $stmt = $conexao->prepare("SELECT * FROM administradores WHERE email = ? AND senha = ? ");
        $stmt->bind_param("ss", $email, $senha);
        $stmt->execute();
        $resultado = $stmt->get_result();

        // Verifica se encontrou um usuário com as credenciais fornecidas
        if ($resultado->num_rows === 1) {
            $dados = $resultado->fetch_assoc();

            $_SESSION['nome'] = $dados['nome'];
            $_SESSION['id'] = $dados['id'];

            header("location: index.php");
            exit;
        } else {
            $_SESSION['erro'] = "Email ou senha inválidos.";
            header("location: login.php");
        }
    }
}
?>
<!doctype html>
<html lang="pt-BR">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Login - Sistema de Usuários</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <style>
        body {
            background-color: #f8f9fa;
            min-height: 100vh;
            display: flex;
            align-items: center;
        }

        .login-card {
            background-color: white;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .login-header {
            background-color: #343a40;
            color: white;
            padding: 2rem;
            text-align: center;
            border-radius: 8px 8px 0 0;
        }

        .login-body {
            padding: 2rem;
        }

        .form-control {
            border: 1px solid #ced4da;
            border-radius: 4px;
        }

        .form-control:focus {
            border-color: #6c757d;
            box-shadow: 0 0 0 0.2rem rgba(108, 117, 125, 0.25);
        }

        .btn-login {
            background-color: #343a40;
            border-color: #343a40;
            color: white;
        }

        .btn-login:hover {
            background-color: #23272b;
            border-color: #1d2124;
        }

        .text-muted {
            color: #6c757d !important;
        }

        .link-dark {
            color: #343a40;
            text-decoration: none;
        }

        .link-dark:hover {
            color: #23272b;
            text-decoration: underline;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-6 col-lg-4">
                <div class="card login-card">
                    <div class="login-header">
                        <i class="bi bi-person-circle fs-1 mb-3"></i>
                        <h3 class="mb-0">Login</h3>
                        <p class="mb-0">Acesse sua conta</p>
                    </div>

                    <div class="login-body">
                        <form action="" method="POST">
                            <div class="mb-3">
                                <label for="email" class="form-label">Email</label>
                                <div class="input-group">
                                    <span class="input-group-text bg-light">
                                        <i class="bi bi-envelope text-muted"></i>
                                    </span>
                                    <input type="email" name="email" class="form-control" id="email" placeholder="Digite seu email" required>
                                </div>
                            </div>

                            <div class="mb-3">
                                <label for="senha" class="form-label">Senha</label>
                                <div class="input-group">
                                    <span class="input-group-text bg-light">
                                        <i class="bi bi-lock text-muted"></i>
                                    </span>
                                    <input type="password" name="senha" class="form-control" id="senha" placeholder="Digite sua senha" required>
                                </div>
                            </div>

                            <div class="mb-3 form-check">
                                <input type="checkbox" name="lembrar" value="1" class="form-check-input" id="lembrar">
                                <label class="form-check-label" for="lembrar">
                                    Lembrar de mim
                                </label>
                            </div>

                            <div class="d-grid mb-3">
                                <button type="submit" class="btn btn-login" name="login">
                                    <i class="bi bi-box-arrow-in-right me-2"></i>
                                    Entrar
                                </button>
                            </div>
                            <?php
                            if (isset($_SESSION["erro"])) {
                                $erro = $_SESSION["erro"];
                                echo "<div class='alert alert-danger'> <span> $erro </span> </div>";
                            }
                            ?>
                        </form>

                    </div>
                </div>

                <div class="text-center mt-3">
                    <p class="text-muted mb-0">
                        <i class="bi bi-shield-check me-1"></i>
                        Projeto - Fábrica de Software
                    </p>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>

</html>