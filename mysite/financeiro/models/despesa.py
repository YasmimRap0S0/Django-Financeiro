from django.db import models
from .balancete import Balancete ##importando o modelo balancete
from .usuario import Usuario

class Despesa(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.FloatField(default=0)
    foto_boleto = models.ImageField(upload_to='boletos/', null=True, blank=True)
    balancete = models.ForeignKey(Balancete, on_delete=models.CASCADE, related_name='despesas')
    