from django.db import models

# Create your models here.
class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)

    def convidar(self, perfil):
        ok = len(Convite.objects.filter(solicitante__id=self.id, convidado__id=perfil.id)) == 0
        if(not ok):
            print(f'Perfil de ID {self.id} já convidou perfil de ID {perfil.id}')
            return False
        Convite(solicitante=self, convidado=perfil).save()

class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_recebidos')