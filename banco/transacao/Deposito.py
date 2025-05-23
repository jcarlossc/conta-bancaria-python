from banco.transacao.Transacao import Transacao

class Deposito(Transacao):
    """Classe que representa a transaçao Depósito. 

    Atributos:
        valor (float): O valor da transaçao.
        tipo (str): O tipo da transação.
    """
    def __init__(self, valor, tipo):
        super().__init__(valor, tipo)

    def __str__(self):
        """Acessa uma representação do atributo Depósito.

        Retorna:
            valor (float): O valor da transaçao.
        """
        return f"{self.valor}"     