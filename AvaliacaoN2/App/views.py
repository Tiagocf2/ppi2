from django.shortcuts import render
from .models import Senha

# Create your views here.
def show_status_senha(request):
    senhas = Senha.objects.filter(id_status_senha__nome__contains='Na fila')
    return render(request, 'statusSenha.html', {'senhas': senhas})