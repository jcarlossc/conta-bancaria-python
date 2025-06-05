import unittest
from banco.transacao.Deposito import Deposito

class TestDeposito(unittest.TestCase):

    def test_instanciacao_valida(self):
        deposito = Deposito(500.0, "Depósito")
        self.assertEqual(deposito.valor, 500.0)
        self.assertEqual(deposito.tipo, "Depósito")

    def test_str_formatado(self):
        deposito = Deposito(300.5, "Depósito")
        self.assertEqual(str(deposito), "300.5 - Depósito")

if __name__ == "__main__":
    unittest.main()
