from django.db import models
from .balancete import Balancete ##importando o modelo balancete

class Receita(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.FloatField(default=0)
    balancete = models.ForeignKey(Balancete, on_delete=models.CASCADE, related_name='receitas')