import datetime
from typing import List, Dict, Any
from banco.transacao.Transacao import Transacao 

class Historico:
    """Classe que representa o histórico das transações. 

    Atributos:
        None.
    """
    def __init__(self) -> None:
        self.transacoes: List[Dict[str, Any]] = []
        self.data_hora = datetime.datetime.now()

    def adicionar_transacao(self, transacao: Transacao) -> None:   
        """Adiciona às transações ao histórico.

        Retorna:
            None.
        """
        transacao_dict: Dict[str, Any] = {
            "Valor R$": transacao.valor,
            "Transação" : transacao.tipo,
            "Data" : self.data_hora.strftime("%d/%m/%Y"),
            "Hora" : self.data_hora.strftime("%H:%M:%S")
        }
        self.transacoes.append(transacao_dict) 

    def acessa_transacoes(self) -> List[Dict[str, Any]]:
        """Acessa às transações.

        Retorna:
            transações (array): As transações do sistema.
        """
        return self.transacoes  

    def __str__(self) -> str:
        """Acessa uma representação das transações.

        Retorna:
            transações (array): As transações.
        """
        return f"{self.transacoes}"   