from banco.usuario.Usuario import Usuario

class PessoaJuridica(Usuario):
    """ Classe que representa uma pessoa jurídica do sistema
    e estende a classe abstrata Usuário. 

    Atributos:
        nome (str): O nome do usuário.
        email (str): O email do usuário.
        cnpj (int): O email do usuário.
    """
    def __init__(self, nome: str, email: str, cnpj: int) -> None:
        super().__init__(nome, email)
        self.cnpj = cnpj

    def tipo_usuario(self) -> str:
        """Acessa o tipo de usuário.

        Retorna:
            str: O tipo de usuário.
        """
        return "Pessoa Jurídica"    
    
    def documento(self) -> int:
        """Acessa o documento do usuário.

        Retorna:
            cnpj (int): O documento do usuário.
        """
        return self.cnpj
    
    def __str__(self) -> str:
        """Acessa uma representação dos atributos de pessoa jurídica.

        Retorna:
            nome (str): O nome do usuário.
            email (str): O email do usuário.
            cnpj (int): O cnpj do usuário.
        """
        return f"Usuário: {self.nome} <{self.cnpj}> <{self.email}>"