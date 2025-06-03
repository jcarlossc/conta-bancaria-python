import unittest
from banco.usuario.PessoaJuridica import PessoaJuridica

class TestPessoaJuridica(unittest.TestCase):

    def setUp(self):
        self.pj = PessoaJuridica("Empresa Python", "python@email.com", 12345678000199)

    def test_atributos(self):
        self.assertEqual(self.pj.nome, "Empresa Python")
        self.assertEqual(self.pj.email, "python@email.com")
        self.assertEqual(self.pj.cnpj, 12345678000199)

    def test_tipo_usuario(self):
        self.assertEqual(self.pj.tipo_usuario(), "Pessoa Jurídica")

    def test_documento(self):
        self.assertEqual(self.pj.documento(), 12345678000199)

    def test_str(self):
        esperado = "Usuário: Empresa Python <12345678000199> <python@email.com>"
        self.assertEqual(str(self.pj), esperado)

if __name__ == "__main__":
    unittest.main()
