from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nome}"


class SitTributaria(models.Model):
    nome = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.nome}"


class CFOP(models.Model):
    nome = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.nome}"


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=500)
    data_criacao = models.DateTimeField(default=timezone.now)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    foto = models.FileField(upload_to='arquivos/', null=True)
    ativo = models.BooleanField(default=True)
    custo = models.FloatField(null=True)
    venda = models.FloatField(null=True)
    ncm = models.CharField(max_length=8)
    sit_tributaria = models.ForeignKey(SitTributaria, on_delete=models.PROTECT, verbose_name='Situação Tributária')
    CFOP = models.ForeignKey(CFOP, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome}"
