import unittest
from banco.transacao.Saque import Saque

class TestSaque(unittest.TestCase):

    def test_instanciacao_valida(self):
        saque = Saque(500.0, "Saque")
        self.assertEqual(saque.valor, 500.0)
        self.assertEqual(saque.tipo, "Saque")

    def test_str_formatado(self):
        saque = Saque(300.0, "Saque")
        self.assertEqual(str(saque), "300.0 - Saque")

if __name__ == "__main__":
    unittest.main()