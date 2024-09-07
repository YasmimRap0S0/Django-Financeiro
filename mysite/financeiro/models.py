from django.db import models
from django.contrib.auth.models import User

##Django permite que você defina relações que são um pra um (OneToOneField),
##um pra muitos (ForeignKey) e muitos pra muitos (ManyToManyField).

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=50)

class Balancete(models.Model):
    nome = models.CharField(max_length=30)
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Receita(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.FloatField(default=0)
    balancete = models.ForeignKey(Balancete, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Despesa(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.FloatField(default=0)
    foto_boleto = models.ImageField(upload_to='boletos/', null=True, blank=True)
    balancete = models.ForeignKey(Balancete, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
