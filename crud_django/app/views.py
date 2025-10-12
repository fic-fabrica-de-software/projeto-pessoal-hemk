from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    return render(request, 'usuarios/login.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.senha = request.POST.get('senha')
        novo_usuario.save()
        return redirect('listagem_usuarios')
    return redirect('home') # Redireciona para a página de login se for GET

def listagem_usuarios(request):
    usuarios_cadastrados = Usuario.objects.all()
    contexto = {
        'usuarios': usuarios_cadastrados
    }
    return render(request, 'usuarios/usuarios.html', contexto)