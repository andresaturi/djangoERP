from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tecnico(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nome}"


class Status(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nome}"


class Chamados(models.Model):
    assunto = models.CharField(max_length=150)
    contato = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    detalhes = models.TextField()
    data_criado = models.DateTimeField(default=timezone.now)
    data_fechado = models.DateTimeField(default=timezone.now)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='arquivos/', null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    atividade = models.TextField(null=True)
    resolucao = models.TextField(null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.assunto}"
