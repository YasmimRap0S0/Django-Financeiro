from django.db import models
import datetime
from django.utils import timezone


class Balancete(models.Model):
    nome = models.CharField(max_length=30)
    data = models.DateField('Data de registro')

    def __str__(self):
        return self.nome


    def publicada_recentemente(self):
        agora = timezone.now().date()
        return self.data >= agora - datetime.timedelta(days=1)