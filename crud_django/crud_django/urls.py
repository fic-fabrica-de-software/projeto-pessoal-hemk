
from django.urls import path
from app import views

urlpatterns = [
    # rota, view responsável, nome referência
    # site.com/ path
    path('', views.home, name='home'),
]
