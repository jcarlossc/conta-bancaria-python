from banco.conta.ContaBancaria import ContaBancaria
from banco.transacao.Saque import Saque
from banco.transacao.Deposito import Deposito
from banco.transacao.Transferencia import Transferencia
from banco.usuario.Usuario import Usuario

class ContaPoupanca(ContaBancaria):
    """Classe que representa uma ContaPoupança do sistema. 

    Atributos:
        None
    """
    def __init__(self, usuario: Usuario) -> None:
        super().__init__(usuario)
        pass

    def depositar(self, valor: float) -> None:
        """Deposita valor na conta poupança.
           -Processa o depósito
           -Adiciona o depósito ao histórico
        
        Retorna:
            None.
        """
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        
        self.saldo += valor
        self.historico.adicionar_transacao(Deposito(valor, "Depósito"))

    def sacar(self, valor: float, registrar=True) -> None:
        """Saca valor da conta poupança .
           -Processa o saque
           -Adiciona o saque ao histórico

        Retorna:
            None.
        """
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        if valor > self.saldo:
            raise ValueError("O valor do saque deve ser menor ou igual ao saldo.")
        
        self.saldo -= valor 
        if registrar:
            self.historico.adicionar_transacao(Saque(valor, "Saque"))
        
    def transferir(self, valor: float, conta_destino: ContaBancaria) -> None:
        """Transfere valor da conta poupança.
           -Processa a transferência
           -Adiciona a tranferência ao histórico

        Retorna:
            None
        """
        if not isinstance(valor, (int, float)):
            raise TypeError("O valor da transferência deve ser numérico.")
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        if valor > self.saldo:
            raise ValueError("O valor da transferência deve ser menor ou igual ao saldo.")
        
        self.sacar(valor, registrar=False)
        conta_destino.depositar(valor)

        self.historico.adicionar_transacao(Transferencia(valor, "Transferência")) 

    def tipo_conta(self) -> str:
        """Acessa o tipo de conta.

        Retorna:
            str: O tipo de conta.
        """
        return "Conta Poupança"       

    def __str__(self) -> str:
        """Acessa uma representação do atributo da ContaPoupança.

        Retorna:
            Usuário (obj): O usuário da conta.
            tipo_conta (str): O tipo da conta bancária
        """
        return f"Usuário: {self.usuario} | <{self.tipo_conta()}>" 