from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=12, null=True)
    endereco = models.CharField(max_length=150, verbose_name='Endereço', null=True)
    numero = models.CharField(max_length=5, null=True)
    cpf = models.CharField(max_length=15, verbose_name='CPF/CNPJ (Obrigatório para emissão de Nota Fiscal)', null=True)
    ativo = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome}"
