from django.db import models

# Create your models here.
class Tipo(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45, null=False)

class StatusSenha(models.Model):
    id_status = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45, null=False)

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45, null=False)

class Senha(models.Model):
    id_senha = models.AutoField(primary_key=True)
    senha = models.IntegerField(null=False)
    hora_data = models.DateTimeField(null=False)
    id_categoria = models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE)
    id_status_senha = models.ForeignKey(StatusSenha, null=True, on_delete=models.CASCADE)
    id_tipo = models.ForeignKey(Tipo, null=True, on_delete=models.CASCADE)
