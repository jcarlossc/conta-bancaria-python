import unittest
from banco.usuario.Usuario import Usuario

# Subclasse concreta para testes
class UsuarioTeste(Usuario):
    def tipo_usuario(self) -> str:
        return "Teste"

    def documento(self) -> int:
        return 12345678900

class TestUsuario(unittest.TestCase):

    def setUp(self):
        self.usuario = UsuarioTeste("João Teste", "joao@teste.com")

    def test_atributos(self):
        self.assertEqual(self.usuario.nome, "João Teste")
        self.assertEqual(self.usuario.email, "joao@teste.com")

    def test_metodo_tipo_usuario(self):
        self.assertEqual(self.usuario.tipo_usuario(), "Teste")

    def test_metodo_documento(self):
        self.assertEqual(self.usuario.documento(), 12345678900)

    def test_str(self):
        self.assertEqual(str(self.usuario), "Usuário: João Teste <joao@teste.com>")

if __name__ == "__main__":
    unittest.main()
