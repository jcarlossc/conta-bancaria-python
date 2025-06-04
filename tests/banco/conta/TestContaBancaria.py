import unittest
from banco.conta.ContaBancaria import ContaBancaria
from banco.usuario.PessoaFisica import PessoaFisica
from banco.historico.Historico import Historico

# Subclasse concreta para testes
class ContaBancariaTeste(ContaBancaria):
    def tipo_conta(self) -> str:
        return "ContaTeste"

    def depositar(self, valor: float) -> None:
        self.saldo += valor
        self.historico.adicionar(f"Depósito de {valor}")

    def sacar(self, valor: float) -> None:
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.adicionar(f"Saque de {valor}")
        else:
            raise ValueError("Saldo insuficiente")

    def transferir(self, valor: float, conta_destino) -> None:
        if valor <= self.saldo:
            self.sacar(valor)
            conta_destino.depositar(valor)
            self.historico.adicionar(f"Transferência de {valor} para {conta_destino.usuario.nome}")
        else:
            raise ValueError("Saldo insuficiente para transferência")

class TestContaBancaria(unittest.TestCase):

    def setUp(self):
        self.usuario = PessoaFisica("Jose Carlos", "josecrlos@email.com", 12345678900)
        self.conta = ContaBancariaTeste(self.usuario)

    def test_atributos_iniciais(self):
        self.assertEqual(self.conta.saldo, 0.0)
        self.assertEqual(self.conta.usuario.nome, "Jose Carlos")
        self.assertIsInstance(self.conta.historico, Historico)

    def test_deposito(self):
        self.conta.depositar(100)
        self.assertEqual(self.conta.saldo, 100)

    def test_saque_valido(self):
        self.conta.depositar(200)
        self.conta.sacar(50)
        self.assertEqual(self.conta.saldo, 150)

    def test_saque_invalido(self):
        with self.assertRaises(ValueError):
            self.conta.sacar(100)

    def test_transferencia_valida(self):
        destinatario = ContaBancariaTeste(PessoaFisica("Maria", "maria@teste.com", 98765432100))
        self.conta.depositar(300)
        self.conta.transferir(100, destinatario)
        self.assertEqual(self.conta.saldo, 200)
        self.assertEqual(destinatario.saldo, 100)

    def test_transferencia_invalida(self):
        destinatario = ContaBancariaTeste(PessoaFisica("Maria", "maria@teste.com", 98765432100))
        with self.assertRaises(ValueError):
            self.conta.transferir(100, destinatario)

    def test_str(self):
        self.assertEqual(str(self.conta), f"Titular: {self.usuario}")

if __name__ == "__main__":
    unittest.main()
