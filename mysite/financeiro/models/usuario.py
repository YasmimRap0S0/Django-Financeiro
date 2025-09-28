from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=50)