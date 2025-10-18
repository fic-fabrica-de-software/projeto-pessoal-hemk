from django.urls import path, include
from app import views

urlpatterns = [
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', views.logar_usuario, name='logar_usuario'),
    path('usuarios/', views.listagem_usuarios, name='listagem_usuarios'),
    path('deletar/<int:usuario_id>/', views.deletar_usuario, name='deletar_usuario'),
    path('', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    # Path('', include('app.urls')),
]
