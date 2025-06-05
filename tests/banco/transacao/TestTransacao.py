import unittest
from banco.transacao.Transacao import Transacao

class TestTransacao(unittest.TestCase):

    def test_instanciacao_valida(self):
        transacao = Transacao(200.0, "Depósito")
        self.assertEqual(transacao.valor, 200.0)
        self.assertEqual(transacao.tipo, "Depósito")

    def test_str_retorna_formatado(self):
        transacao = Transacao(150.75, "Saque")
        self.assertEqual(str(transacao), "150.75 | Saque")

    def test_tipo_dado_incorreto(self):
        transacao = Transacao("cem", 123)
        self.assertEqual(transacao.valor, "cem")
        self.assertEqual(transacao.tipo, 123)

if __name__ == "__main__":
    unittest.main()
