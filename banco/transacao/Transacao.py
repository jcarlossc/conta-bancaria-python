class Transacao:
    """Classe que representa uma Transação. 

    Atributos:
        valor (float): O valor da transaçao.
        tipo (str): O tipo da transação.
    """
    def __init__(self, valor, tipo):
        self.valor = valor 
        self.tipo = tipo
    
    def __str__(self):
        """Acessa uma representação dos atributos da transação.

        Retorna:
            valor (float): O valor da transaçao.
            tipo (str): O tipo da transação.
        """
        return f"{self.valor} || {self.tipo}"