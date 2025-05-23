class Extrato:
    """Classe que representa o extrato das contas. 

    Atributos:
        None.
    """
    def __init__(self):
        pass
        
    def acessar_extrato(self, conta):
        """Imprime extrato.

        Retorna:
            None.
        """
        print("---------------------------------------- EXTRATO ----------------------------------------")
        print(f"TIPO DE CONTA: {conta.tipo_conta()}")
        print(f"TITULAR: {conta.usuario.nome}")
        if conta.usuario.tipo_usuario() == "Pessoa Física":
            print(f"CPF: {conta.usuario.documento()}")
        else:    
            print(f"CNPJ: {conta.usuario.documento()}")
        print(f"SALDO: R$ {round(conta.saldo, 2)}")
        print("LISTA DE TRANSAÇÕES")
        for transacao in conta.historico.transacoes:
            print(transacao)
        print("------------------------------------------ FIM ------------------------------------------")