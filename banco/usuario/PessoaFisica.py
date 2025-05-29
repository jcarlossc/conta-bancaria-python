from banco.usuario.Usuario import Usuario

class PessoaFisica(Usuario):
    """ Classe que representa uma pessoa física do sistema
    e estende a classe abstrata Usuário. 

    Atributos:
        nome (str): O nome do usuário.
        email (str): O email do usuário.
        cpf (int): O email do usuário.
    """
    def __init__(self, nome: str, email: str, cpf: int) -> None:
        super().__init__(nome, email)
        self.cpf = cpf

    def tipo_usuario(self) -> str:
        """Acessa o tipo de usuário.

        Retorna:
            str: O tipo de usuário.
        """
        return "Pessoa Física"    
    
    def documento(self) -> int:
        """Acessa o documento do usuário.

        Retorna:
            cpf (int): O documento do usuário.
        """
        return self.cpf
    
    def __str__(self) -> str:
        """Acessa uma representação dos atributos de pessoa física.

        Retorna:
            nome (str): O nome do usuário.
            email (str): O email do usuário.
            cpf (int): O cpf do usuário.
        """
        return f"Usuário: {self.nome} <{self.cpf}> <{self.email}>"