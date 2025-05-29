from banco.transacao.Transacao import Transacao

class Deposito(Transacao):
    """Classe que representa a transaçao Depósito. 

    Atributos:
        valor (float): O valor da transaçao.
        tipo (str): O tipo da transação.
    """
    def __init__(self, valor: float, tipo: str) -> None:
        super().__init__(valor, tipo)
        pass

    def __str__(self) -> str:
        """Acessa uma representação do atributo Depósito.

        Retorna:
            valor (float): O valor da transaçao.
            tipo (str): O tipo da transação.
        """
        return f"{self.valor} - {self.tipo}"     