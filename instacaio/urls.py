from django.contrib import admin
from django.urls import path

from instacaio import views

urlpatterns = [
    path('postar/', views.criar_post, name='postar'),
    path('registrar/', views.signup, name='registrar'),
    path('', views.inicio, name='inicio'),
]
