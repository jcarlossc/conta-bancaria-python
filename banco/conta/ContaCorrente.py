from banco.conta.ContaBancaria import ContaBancaria
from banco.transacao.Saque import Saque
from banco.transacao.Deposito import Deposito
from banco.transacao.Transferencia import Transferencia

class ContaCorrente(ContaBancaria):
    """Classe que representa uma ContaCorrente do sistema. 

    Atributos:
        obj (Usuário): O objeto Usuário.
    """
    def __init__(self, usuario):
        super().__init__(usuario)

    def depositar(self, valor):
        """Deposita valor na conta.
           Processa o depósito
           Adiciona o depósito ao histórico
        
        Retorna:
            bool: Falso ou verdadeiro.
        """
        if not isinstance(valor, (int, float)):
            raise TypeError("O valor do depósito deve ser numérico.")
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        
        self.saldo += valor
        self.historico.adicionar_transacao(Deposito(valor, "Depósito"))

    def sacar(self, valor, registrar=True):
        """Saca valor da conta.
           Processa o saque
           Adiciona o saque ao histórico

        Retorna:
            bool: Falso ou verdadeiro.
        """
        if not isinstance(valor, (int, float)):
            raise TypeError("O valor do saque deve ser numérico.")
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        if valor > self.saldo:
            raise ValueError("O valor do saque deve ser menor ou igual ao saldo.")
        
        self.saldo -= valor 
        if registrar:
            self.historico.adicionar_transacao(Saque(valor, "Saque"))  
        

        
    def transferir(self, valor, destino):
        """Transfere valor da conta.
           Processa a transferência
           Adiciona a tranferência ao histórico

        Retorna:
            bool: Falso ou verdadeiro.
        """
        if not isinstance(valor, (int, float)):
            raise TypeError("O valor da transferência deve ser numérico.")
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        if valor > self.saldo:
            raise ValueError("O valor da transferência deve ser menor ou igual ao saldo.")
        
        if self.sacar(valor, registrar=False):
            destino.depositar(valor)

        self.historico.adicionar_transacao(Transferencia(valor, "Transferência")) 

    def tipo_conta(self):
        """Acessa o tipo de conta.

        Retorna:
            str: O tipo de conta.
        """
        return "Conta Corrente"       

    def __str__(self):
        """Acessa uma representação do atributo da ContaCorrente.

        Retorna:
            Usuário (obj): O usuário da conta.
            tipo_conta (str): O tipo da costa bancária
        """
        return f"Tipo de conta: {self.tipo_conta()} | {self.usuario}" 