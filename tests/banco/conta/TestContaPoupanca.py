import unittest
from banco.conta.ContaPoupanca import ContaPoupanca
from banco.usuario.PessoaFisica import PessoaFisica

class TestContaPoupanca(unittest.TestCase):

    def setUp(self):
        self.usuario1 = PessoaFisica("Carlos Costa", "carloscosta@email.com", 11122233344)
        self.usuario2 = PessoaFisica("Jose Carlos", "josecarlos@email.com", 55566677788)
        self.conta1 = ContaPoupanca(self.usuario1)
        self.conta2 = ContaPoupanca(self.usuario2)

    def test_tipo_conta(self):
        self.assertEqual(self.conta1.tipo_conta(), "Conta Poupança")

    def test_deposito_valido(self):
        self.conta1.depositar(500)
        self.assertEqual(self.conta1.saldo, 500)

    def test_deposito_valor_invalido(self):
        with self.assertRaises(ValueError):
            self.conta1.depositar(0)

    def test_deposito_tipo_invalido(self):
        with self.assertRaises(TypeError):
            self.conta1.depositar("quinhentos")

    def test_saque_valido(self):
        self.conta1.depositar(300)
        self.conta1.sacar(200)
        self.assertEqual(self.conta1.saldo, 100)

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
        self.conta1.transferir(400, self.conta2)
        self.assertEqual(self.conta1.saldo, 600)
        self.assertEqual(self.conta2.saldo, 400)

    def test_transferencia_valor_maior_que_saldo(self):
        with self.assertRaises(ValueError):
            self.conta1.transferir(200, self.conta2)

    def test_transferencia_valor_invalido(self):
        with self.assertRaises(ValueError):
            self.conta1.transferir(-50, self.conta2)

    def test_transferencia_tipo_invalido(self):
        with self.assertRaises(TypeError):
            self.conta1.transferir("duzentos", self.conta2)

    def test_str(self):
        texto = str(self.conta1)
        self.assertIn("Conta Poupança", texto)
        self.assertIn("Carlos Costa", texto)

if __name__ == "__main__":
    unittest.main()
