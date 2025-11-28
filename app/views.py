from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario

def index(request):
    return render(request, 'user/index.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def cadastrar_usuario(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.senha = request.POST.get('senha')
        novo_usuario.save()
        return redirect('listagem_usuarios')
    return redirect('login') # Redireciona para a página de login se for GET

def logar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        try:
            usuario = Usuario.objects.get(nome=nome, senha=senha)
            return redirect('listagem_usuarios')
        except Usuario.DoesNotExist:
            return redirect('login') # Redireciona para a página de login se falhar
    return redirect('login') # Redireciona para a página de login se for GET

def deletar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return redirect('listagem_usuarios')

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.senha = request.POST.get('senha')
        usuario.save()
        return redirect('listagem_usuarios')
    contexto = {
        'usuario': usuario
    }
    return render(request, 'usuarios/editar_usuario.html', contexto)

def listagem_usuarios(request):
    usuarios_cadastrados = Usuario.objects.all()
    contexto = {
        'usuarios': usuarios_cadastrados
    }
    return render(request, 'usuarios/usuarios.html', contexto)