from django.contrib import admin
from financeiro.models.usuario import Usuario
from financeiro.models.balancete import Balancete
from financeiro.models.receita import Receita
from financeiro.models.despesa import Despesa

admin.site.register(Usuario)
admin.site.register(Balancete)
admin.site.register(Receita)
admin.site.register(Despesa)
