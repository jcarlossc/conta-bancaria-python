from abc import ABC, abstractmethod

class Usuario(ABC):
    """ Classe que representa um usuário do sistema. 

    Atributos:
        nome (str): O usuário do sistema.
        email (str): O email do usuário.
    """
    def __init__(self, nome: str, email: str) -> None:
        self.nome = nome
        self.email = email

    @abstractmethod
    def tipo_usuario(self) -> str:
        """Retorna o tipo de usuário: 'Pessoa Física' ou 'Pessoa Jurídica'."""
        pass    

    @abstractmethod
    def documento(self) -> int:
        """Retorna o CPF ou CNPJ"""
        pass

    def __str__(self) -> str:
        """Acessa uma representação dos atributos do Usuário.

        Retorna:
            nome (str): O nome do usuário.
            email (str): O email do usuário.
        """
        return f"Usuário: {self.nome} <{self.email}>"