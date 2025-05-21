from abc import ABC, abstractmethod

class Usuario(ABC):
    """ Classe que representa um usuário do sistema. 

    Atributos:
        nome (str): O usuário do sistema.
        email (str): O email do usuário.
    """
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @abstractmethod
    def tipo_usuario(self):
        """Retorna o tipo de usuário: 'Pessoa Física' ou 'Pessoa Jurídica'."""
        pass    

    @abstractmethod
    def documento(self):
        """Retorna o CPF ou CNPJ"""
        pass