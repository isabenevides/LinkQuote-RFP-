from django.db import models
from django.contrib.auth.models import User

class Provedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='provedor')
    razao_social = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.razao_social