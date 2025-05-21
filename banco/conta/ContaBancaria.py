from abc import ABC, abstractmethod
#from banco.historico.Historico import Historico

class ContaBancaria(ABC):
    """ Classe que representa uma conta bancária do sistema. 

    Atributos:
        usuário (obj): O objeto usuário.
    """
    def __init__(self, usuario):
        self.usuario = usuario
        self.saldo = 0.0
        #self.historico = Historico()

    @abstractmethod
    def tipo_conta(self):
        """Acessa o tipo de conta.
           Método abstrato. 

        Retorna:
            str: O tipo de conta.
        """
        pass   

    @abstractmethod
    def depositar(self, valor):
        """Deposita valor na conta.
           Método abstrato .

        Retorna:
            bool: Falso ou verdadeiro.
        """
        pass

    @abstractmethod
    def sacar(self, valor):
        """Saca valor da conta.
           Método abstrato .

        Retorna:
            bool: Falso ou verdadeiro.
        """
        pass   
    @abstractmethod    
    def transferir(self, valor, conta):    
        """Transfere valor da conta.
           Método abstrato.

        Parâmetros:
            valor (float): O valor da transferência.  
            conta (obj): O objeto que receberá o depósito. 

        Retorna:
            bool: Falso ou verdadeiro.
        """
        pass  

    def __str__(self):
        """Acessa uma representação do atributo da conta.

        Retorna:
            usuário (Usuário): O usuário da conta.
            saldo (float): O saldo da conta.
        """
        return f"Titular: {self.usuario}"  