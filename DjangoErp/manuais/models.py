from django.db import models
from django.contrib.auth.models import User


class Manuais(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título")
    detalhes = models.TextField()
    arquivo = models.FileField(upload_to='arquivos/', null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.titulo}"
