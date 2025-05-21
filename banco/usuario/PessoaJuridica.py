from banco.usuario.Usuario import Usuario

class PessoaJuridica(Usuario):
    """ Classe que representa uma pessoa jurídica do sistema. 

    Atributos:
        nome (str): O usuário do sistema.
        email (str): O email do usuário.
        cnpj: (int): O cnpj do usuário
    """
    def __init__(self, nome, email, cnpj):
        super().__init__(nome, email)
        self.cnpj = cnpj

    def tipo_usuario(self):
        """Acessa o tipo de usuário.

        Retorna:
            str: O tipo de usuário.
        """
        return "Pessoa jurídica"    
    
    def documento(self):
        """Acessa o documento do usuário.

        Retorna:
            int: O documento do usuário.
        """
        return self.cnpj
    
    def __str__(self):
        """Acessa uma representação dos atributos de pessoa jurídica.

        Retorna:
            nome (str): O nome do usuário.
            email (str): O email do usuário.
        """
        return f"Usuário: {self.nome} <{self.email}>"