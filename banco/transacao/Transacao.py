class Transacao:
    """Classe que representa uma Transação do sistema. 

    Atributos:
        valor (float): O valor da transaçao.
        tipo (str): O tipo da transação.
    """
    def __init__(self, valor: float, tipo: str) -> None:
        self.valor = valor 
        self.tipo = tipo
    
    def __str__(self) -> str:
        """Acessa uma representação dos atributos da transação.

        Retorna:
            valor (float): O valor da transaçao.
            tipo (str): O tipo da transação.
        """
        return f"{self.valor} | {self.tipo}"