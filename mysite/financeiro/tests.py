from django.test import TestCase
from .models.balancete import Balancete
from .models.receita import Receita
from .models.despesa import Despesa
import datetime

class BalanceteTestCase(TestCase):
	def setUp(self):
		self.balancete = Balancete.objects.create(nome="Teste", data=datetime.date.today())

	def test_balancete_str(self):
		self.assertEqual(str(self.balancete), "Teste")

	def test_publicada_recentemente(self):
		self.assertTrue(self.balancete.publicada_recentemente())

	def test_receita_e_despesa(self):
		receita = Receita.objects.create(nome="Receita 1", valor=100, balancete=self.balancete)
		despesa = Despesa.objects.create(nome="Despesa 1", valor=40, balancete=self.balancete)
		self.assertEqual(self.balancete.receitas.count(), 1)
		self.assertEqual(self.balancete.despesas.count(), 1)
		total_receitas = sum(r.valor for r in self.balancete.receitas.all())
		total_despesas = sum(d.valor for d in self.balancete.despesas.all())
		saldo = total_receitas - total_despesas
		self.assertEqual(saldo, 60)
