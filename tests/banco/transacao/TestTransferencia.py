import unittest
from banco.transacao.Transferencia import Transferencia

class TestTransferencia(unittest.TestCase):

    def test_instanciacao_valida(self):
        transferencia = Transferencia(250.75, "Transferência")
        self.assertEqual(transferencia.valor, 250.75)
        self.assertEqual(transferencia.tipo, "Transferência")

    def test_str_formatado(self):
        transferencia = Transferencia(1000.0, "Transferência")
        self.assertEqual(str(transferencia), "1000.0 | Transferência")

if __name__ == "__main__":
    unittest.main()
