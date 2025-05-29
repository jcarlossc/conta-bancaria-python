from abc import ABC, abstractmethod
from banco.usuario.Usuario import Usuario

class ContaBancaria(ABC):
    """ Classe que representa uma conta bancária do sistema. 

    Atributos:
        usuário (obj) O usuário do sistema.
    """
    def __init__(self, usuario: Usuario) -> None:
        self.saldo = 0.0
        self.usuario = usuario
        #self.historico = Historico()

    @abstractmethod
    def tipo_conta(self) -> str:
        """Acessa o tipo de conta.
           Método abstrato. 

        Retorna:
            tipo_conta (str): O tipo de conta.
        """
        pass   

    @abstractmethod
    def depositar(self, valor) -> float:
        """Deposita valor na conta.
           Método abstrato .

        Retorna:
            None:
        """
        pass

    @abstractmethod
    def sacar(self, valor) -> float:
        """Saca valor da conta.
           Método abstrato .

        Retorna:
            None:
        """
        pass  

    @abstractmethod    
    def transferir(self, valor, conta_destino) -> float | object:    
        """Transfere valor da conta.
           Método abstrato.

        Parâmetros:
            valor (float): O valor da transferência.  
            conta_destino (obj): O objeto que receberá o depósito. 

        Retorna:
            None:
        """
        pass  

    def __str__(self) -> str:
        """Acessa uma representação do atributo da conta.

        Retorna:
            usuário (obj): O usuário da conta.
        """
        return f"Titular: {self.usuario}"  