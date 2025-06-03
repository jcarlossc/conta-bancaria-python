from banco.conta.ContaBancaria import ContaBancaria
from banco.usuario.Usuario import Usuario
from banco.transacao.Saque import Saque
from banco.transacao.Deposito import Deposito
from banco.transacao.Transferencia import Transferencia

class ContaCorrente(ContaBancaria):
    """Classe que representa uma ContaCorrente do sistema. 
       
    Atributos:
        usuário (obj): O objeto usuário.
    """
    def __init__(self, usuario: Usuario) -> None:
        super().__init__(usuario)
        pass

    def depositar(self, valor: float) -> None:
        """- Deposita valor na conta.
           - Processa o depósito.
           - Adiciona o depósito ao histórico.
        
        Retorna:
            None:
        """
        if not isinstance(valor, (int, float)):
            raise TypeError("O valor do depósito deve ser numérico.")
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        
        self.saldo += valor
        self.historico.adicionar_transacao(Deposito(valor, "Depósito"))

    def sacar(self, valor: float, registrar=True) -> None:
        """- Saca valor da conta.
           - Processa o saque.
           - Adiciona o saque ao histórico.

        Retorna:
            None
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

    def transferir(self, valor: float, conta_destino: ContaBancaria) -> None:
        """- Transfere valor da conta.
           - Processa a transferência
           - Adiciona a tranferência ao histórico

        Retorna:
            None:
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
           tipo_conta (str): O tipo de conta.
        """
        return "Conta Corrente"       

    def __str__(self) -> str:
        """Acessa uma representação do atributo da ContaCorrente.

        Retorna:
            Usuário (obj): O usuário da conta.
            tipo_conta (str): O tipo da conta bancária
        """
        return f"Tipo de conta: {self.tipo_conta()} | {self.usuario}" 