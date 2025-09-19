import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.alert("O script vai começar. Não mexa no mouse ou teclado.")
time.sleep(3)

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)

# Abrir o sistema
pyautogui.write("localhost:8080/aulas_hemk/projeto-pessoal-projeto_curso/php/login.html")
pyautogui.press("enter")
time.sleep(2)

# Fazer login (demonstração)

# Preencher email
pyautogui.press("tab")
pyautogui.write("admin@gmail.com")

# Preencher senha
pyautogui.press("tab")
pyautogui.write("senhaforte")

# Clicar em entrar
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

# Importar a base de dados (tabela)
import pandas as pd

tabela = pd.read_csv("../data/usuarios.csv")

print(tabela)

# Cadastrar usuários em loop
for linha in tabela.index:
    pyautogui.click(x=100, y=200)  # Coordenadas do botão "Adicionar Usuário"
    time.sleep(1)

    pyautogui.click(x=300, y=300)  # Coordenadas do campo "Nome"

    nome = tabela.loc[linha, "nome"]
    pyautogui.write(nome)
    pyautogui.press("tab")

    email = tabela.loc[linha, "email"]
    pyautogui.write(email)
    pyautogui.press("tab")

    dataNascimento = tabela.loc[linha, "data_nascimento"]
    pyautogui.write(dataNascimento)
    pyautogui.press("tab")
    pyautogui.press("tab")

    senha = tabela.loc[linha, "senha"]
    pyautogui.write(senha)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.alert(f"Usuário {nome} cadastrado com sucesso!")


pyautogui.alert("Script finalizado.")