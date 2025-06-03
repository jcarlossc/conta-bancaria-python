import unittest
from banco.usuario.PessoaFisica import PessoaFisica

class TestPessoaFisica(unittest.TestCase):

    def setUp(self):
        self.pf = PessoaFisica("Maria Teresa", "mariateresa@email.com", 12345678900)

    def test_atributos(self):
        self.assertEqual(self.pf.nome, "Maria Teresa")
        self.assertEqual(self.pf.email, "mariateresa@email.com")
        self.assertEqual(self.pf.cpf, 12345678900)

    def test_tipo_usuario(self):
        self.assertEqual(self.pf.tipo_usuario(), "Pessoa Física")

    def test_documento(self):
        self.assertEqual(self.pf.documento(), 12345678900)

    def test_str(self):
        esperado = "Usuário: Maria Teresa <12345678900> <mariateresa@email.com>"
        self.assertEqual(str(self.pf), esperado)

if __name__ == "__main__":
    unittest.main()
