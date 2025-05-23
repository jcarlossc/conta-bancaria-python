from banco.transacao.Transacao import Transacao

class Transferencia(Transacao):
    """Classe que representa a transaçao Transferência. 

    Atributos:
        valor (float): O valor da transaçao.
        tipo (str): O tipo da transação.
    """
    def __init__(self, valor, tipo):
        super().__init__(valor, tipo)

    def __str__(self):
        """Acessa uma representação do atributo Transferência.

        Retorna:
            valor (float): O valor da transaçao.
            tipo (str): O tipo da transação.
        """
        return f"{self.valor} - {self.tipo}"  