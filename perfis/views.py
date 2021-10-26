from django.shortcuts import render
from perfis.models import Perfil
#from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    return render(request, 'perfil.html', {'perfil': perfil})