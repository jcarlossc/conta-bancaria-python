from abc import ABC, abstractmethod

class Usuario(ABC):
    """ Classe que representa um usuário do sistema. 

    Atributos:
        nome (str): O usuário do sistema.
        email (str): O email do usuário.
    """
    def __init__(self):
        pass

    def adicionar_nome(self, nome):
        """Adiciona o nome do usuário."""
        self.nome = nome

    def adicionar_email(self, email):
        """Adiciona o email co usuário."""
        self.email = email

    @abstractmethod
    def tipo_usuario(self):
        """Retorna o tipo de usuário: 'Pessoa Física' ou 'Pessoa Jurídica'."""
        pass    

    @abstractmethod
    def documento(self):
        """Retorna o CPF ou CNPJ"""
        pass