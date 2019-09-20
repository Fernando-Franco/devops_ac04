from unittest import TestCase
from br.franco.soma_dia import Soma_dia

class Test_Agenda(TestCase):

	def setUp(self):
		self.test_soma_dia = Soma_dia()

	def test_somarDias(self):
		self.assertEqual(self.test_soma_dia.somarDias(1), 2, "Sujou")
