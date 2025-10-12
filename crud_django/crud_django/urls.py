from django.urls import path
from app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cadastrar_usuario/", views.cadastrar_usuario, name="cadastrar_usuario"),
    path("usuarios/", views.listagem_usuarios, name="listagem_usuarios"),
]
