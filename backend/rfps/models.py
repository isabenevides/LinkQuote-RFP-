from django.db import models
from django.contrib.auth.models import User

class RFP(models.Model):
    TIPO_LINK_CHOICES = [
        ('banda_larga', 'Banda larga empresarial'),
        ('dedicado', 'Link dedicado'),
        ('ponto_a_ponto', 'Transporte ponto a ponto'),
    ]

    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rfps')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    tipo_link = models.CharField(max_length=20, choices=TIPO_LINK_CHOICES)
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=255, blank=True)
    velocidade_download_mbps = models.PositiveIntegerField()
    velocidade_upload_mbps = models.PositiveIntegerField()
    prazo_cotacao = models.DateTimeField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.get_tipo_link_display()})"