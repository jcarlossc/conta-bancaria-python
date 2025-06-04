import unittest
from banco.historico.Historico import Historico
from banco.transacao.Transacao import Transacao

class MockTransacao(Transacao):
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo

class TestHistorico(unittest.TestCase):

    def setUp(self):
        self.historico = Historico()
        self.transacao1 = MockTransacao(100.0, "Depósito")
        self.transacao2 = MockTransacao(50.0, "Saque")

    def test_adicionar_transacao(self):
        self.historico.adicionar_transacao(self.transacao1)
        transacoes = self.historico.acessa_transacoes()
        self.assertEqual(len(transacoes), 1)
        self.assertEqual(transacoes[0]["Valor R$"], 100.0)
        self.assertEqual(transacoes[0]["Transação"], "Depósito")
        self.assertIn("Data", transacoes[0])
        self.assertIn("Hora", transacoes[0])

    def test_multiplas_transacoes(self):
        self.historico.adicionar_transacao(self.transacao1)
        self.historico.adicionar_transacao(self.transacao2)
        transacoes = self.historico.acessa_transacoes()
        self.assertEqual(len(transacoes), 2)
        self.assertEqual(transacoes[1]["Valor R$"], 50.0)
        self.assertEqual(transacoes[1]["Transação"], "Saque")

    def test_acessa_transacoes_vazio(self):
        self.assertEqual(self.historico.acessa_transacoes(), [])

    def test_str_retorna_lista(self):
        self.historico.adicionar_transacao(self.transacao1)
        resultado = str(self.historico)
        self.assertIn("Depósito", resultado)
        self.assertIn("100.0", resultado)

if __name__ == "__main__":
    unittest.main()
