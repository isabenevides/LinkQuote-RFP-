from django.db import models
from rfps.models import RFP
from provedores.models import Provedor

class Proposta(models.Model):
    rfp = models.ForeignKey(RFP, on_delete=models.CASCADE, related_name='propostas')
    provedor = models.ForeignKey(Provedor, on_delete=models.CASCADE, related_name='propostas')
    valor_mensal = models.DecimalField(max_digits=10, decimal_places=2)
    prazo_instalacao_dias = models.PositiveIntegerField()
    sla_disponibilidade = models.DecimalField(max_digits=5, decimal_places=2, help_text="Ex: 99.5 (%)")
    observacoes = models.TextField(blank=True)
    enviada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['rfp', 'provedor']

    def __str__(self):
        return f"Proposta de {self.provedor} para {self.rfp}"