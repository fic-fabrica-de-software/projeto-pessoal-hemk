from django.shortcuts import render
from .models import Usuario

# Create your views here.
def home(request):
    return render(request, 'usuarios/home.html') 

def usuarios(request):
    # Salvar dados do usuários para banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save

    # Exibir usuários cadastrados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar os dados
    return render(request, 'usuarios/usuarios.html', usuarios)