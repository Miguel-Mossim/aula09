from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    path('postar/', views.criar_post, name='postar'),
    path('', views.inicio, name='inicio'),
    path('contas/', include("contas.urls")),
]
