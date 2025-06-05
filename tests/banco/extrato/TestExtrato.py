import unittest
from io import StringIO
import sys

from banco.usuario.PessoaFisica import PessoaFisica
from banco.conta.ContaCorrente import ContaCorrente
from banco.extrato.Extrato import Extrato

class TestExtrato(unittest.TestCase):

    def setUp(self):
        self.usuario = PessoaFisica("Jose Carlos", "josecarlos@email.com", 12345678901)
        self.conta = ContaCorrente(self.usuario)
        self.conta.depositar(1000)
        self.conta.sacar(200)
        self.extrato = Extrato()

    def test_acessar_extrato_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.extrato.acessar_extrato(self.conta)
        sys.stdout = sys.__stdout__ 

        output = captured_output.getvalue()
        
        self.assertIn("TITULAR: Jose Carlos", output)
        self.assertIn("EMAIL: josecarlos@email.com", output)
        self.assertIn("TIPO DE CONTA: Conta Corrente", output)
        self.assertIn("TIPO DE USUÁRIO: Pessoa Física", output)
        self.assertIn("CPF: 12345678901", output)
        self.assertIn("SALDO: R$ 800.0", output)
        self.assertIn("Depósito", output)
        self.assertIn("Saque", output)
        self.assertIn("LISTA DE TRANSAÇÕES", output)
        self.assertIn("FIM", output)

if __name__ == "__main__":
    unittest.main()
