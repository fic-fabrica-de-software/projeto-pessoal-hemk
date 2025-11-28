from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', views.logar_usuario, name='logar_usuario'),
    path('usuarios/', views.listagem_usuarios, name='listagem_usuarios'),
    path('deletar/<int:usuario_id>/', views.deletar_usuario, name='deletar_usuario'),
    path('editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
]
