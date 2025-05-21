from banco.usuario.Usuario import Usuario

class PessoaFisica(Usuario):
    """ Classe que representa uma pessoa física do sistema. 

    Atributos:
        nome (str): O usuário do sistema.
        email (str): O email do usuário.
        cpf: (str): O cpf do usuário
    """
    def __init__(self, nome, email, cpf):
        super().__init__(nome, email)
        self.cpf = cpf

    def tipo_usuario(self):
        """Acessa o tipo de usuário.

        Retorna:
            str: O tipo de usuário.
        """
        return "Pessoa Física"    
    
    def documento(self):
        """Acessa o documento do usuário.

        Retorna:
            str: O documento do usuário.
        """
        return self.cpf
    
    def __str__(self):
        """Acessa uma representação dos atributos de pessoa física.

        Retorna:
            nome (str): O nome do usuário.
            email (str): O email do usuário.
        """
        return f"Usuário: {self.nome} <{self.email}>"