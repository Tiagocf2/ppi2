from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_status_senha, name='status_senha'),
]