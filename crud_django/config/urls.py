from zipfile import Path
from django.urls import path, include
from app import views

urlpatterns = [
    path('', include('app.urls')),
]
