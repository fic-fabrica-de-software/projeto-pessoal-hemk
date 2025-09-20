import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.alert("O script vai começar. Não mexa no mouse ou teclado.")
time.sleep(3)

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

# Abrir o sistema
pyautogui.write("http://localhost/f%C3%A1brica_de_software/projeto-pessoal-projeto_curso/php/login.php")
pyautogui.press("enter")
time.sleep(2)

# Fazer login (demonstração)

# Preencher email
pyautogui.press("tab")
pyautogui.write("admin@gmail.com")

# Preencher senha
pyautogui.press("tab")
pyautogui.write("senha123")

# Clicar em entrar
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)   
# Importar a base de dados (tabela)
import pandas

tabela = pandas.read_csv(r"C:\xampp\htdocs\fábrica_de_software\projeto-pessoal-projeto_curso\python\src\usuarios.csv")

print(tabela)

# Cadastrar usuários em loop
for linha in tabela.index[:5]: # Limitar a 5 cadastros para teste
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")

    nome = tabela.loc[linha, "Nome"]
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

pyautogui.alert("Usuarios cadastrados com sucesso.")