from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfis/<int:perfil_id>', views.exibir, name='exibir'),
    path('perfis/<int:perfil_id>/convidar', views.convidar, name='convidar'),
    
]

