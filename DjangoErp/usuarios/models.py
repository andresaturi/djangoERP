from django.db import models
from django.contrib.auth.models import User


class Cidade(models.Model):
    nome = models.CharField(max_length=50)


class Empresa(models.Model):
    razao_social = models.CharField(max_length=100, null=True)
    nome_fantasia = models.CharField(max_length=100, null=True)
    endereco = models.CharField(max_length=100, null=True)
    numero = models.CharField(max_length=5, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, null=True)
    cep = models.CharField(max_length=10, null=True)
    user_master = models.OneToOneField(User, on_delete=models.PROTECT)


