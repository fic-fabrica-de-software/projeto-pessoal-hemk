from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', views.logar_usuario, name='logar_usuario'),
    path('usuarios/', views.listagem_usuarios, name='listagem_usuarios'),
    path('deletar/<int:usuario_id>/', views.deletar_usuario, name='deletar_usuario'),
    path('editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('atribuir_tarefa/<int:usuario_id>/', views.atribuir_tarefa, name='atribuir_tarefa'),
]
