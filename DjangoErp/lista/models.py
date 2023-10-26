from django.db import models
from django.contrib.auth.models import User


class Lista(models.Model):
    produto = models.CharField(max_length=150)
    recebido = models.BooleanField(default=False)
    pessoa = models.CharField(max_length=100, null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)


    def __str__(self):
        return f"{self.produto}"
