import unittest
from banco.conta.ContaCorrente import ContaCorrente
from banco.usuario.PessoaFisica import PessoaFisica
from banco.transacao.Deposito import Deposito
from banco.transacao.Saque import Saque
from banco.transacao.Transferencia import Transferencia


class TestContaCorrente(unittest.TestCase):

    def setUp(self):
        self.usuario1 = PessoaFisica("Jose Carlos", "josecarlos@email.com", 12345678900)
        self.usuario2 = PessoaFisica("Maria Teresa", "mariateresa@email.com", 98765432100)
        self.conta1 = ContaCorrente(self.usuario1)
        self.conta2 = ContaCorrente(self.usuario2)

    def test_tipo_conta(self):
        self.assertEqual(self.conta1.tipo_conta(), "Conta Corrente")

    def test_deposito_valido(self):
        self.conta1.depositar(1000)
        self.assertEqual(self.conta1.saldo, 1000)

    def test_deposito_invalido_tipo(self):
        with self.assertRaises(TypeError):
            self.conta1.depositar("mil")

    def test_deposito_invalido_valor(self):
        with self.assertRaises(ValueError):
            self.conta1.depositar(-100)

    def test_saque_valido(self):
        self.conta1.depositar(500)
        self.conta1.sacar(200)
        self.assertEqual(self.conta1.saldo, 300)

    def test_saque_valor_maior_que_saldo(self):
        self.conta1.depositar(100)
        with self.assertRaises(ValueError):
            self.conta1.sacar(150)

    def test_saque_valor_invalido(self):
        with self.assertRaises(ValueError):
            self.conta1.sacar(0)

    def test_saque_tipo_invalido(self):
        with self.assertRaises(TypeError):
            self.conta1.sacar("cem")

    def test_transferencia_valida(self):
        self.conta1.depositar(1000)
        self.conta1.transferir(300, self.conta2)
        self.assertEqual(self.conta1.saldo, 700)
        self.assertEqual(self.conta2.saldo, 300)

    def test_transferencia_valor_maior_que_saldo(self):
        with self.assertRaises(ValueError):
            self.conta1.transferir(100, self.conta2)

    def test_transferencia_valor_invalido(self):
        with self.assertRaises(ValueError):
            self.conta1.transferir(-50, self.conta2)

    def test_transferencia_tipo_invalido(self):
        with self.assertRaises(TypeError):
            self.conta1.transferir("cem", self.conta2)

    def test_str(self):
        texto = str(self.conta1)
        self.assertIn("Tipo de conta: Conta Corrente", texto)
        self.assertIn("Jose Carlos", texto)

if __name__ == "__main__":
    unittest.main()