from banco.conta.ContaBancaria import ContaBancaria

class Extrato:
    """Classe que representa o extrato das contas. 

    Atributos:
        None.
    """
    def __init__(self) -> None:
        pass
        
    def acessar_extrato(self, conta: ContaBancaria) -> None:
        """Imprime extrato.

        Retorna:
            None.
        """
        print("---------------------------------------- EXTRATO ----------------------------------------")
        print(f"TITULAR: {conta.usuario.nome}")
        print(f"EMAIL: {conta.usuario.email}")
        print(f"TIPO DE CONTA: {conta.tipo_conta()}")
        if conta.usuario.tipo_usuario() == "Pessoa Física":
            print(f"TIPO DE USUÁRIO: {conta.usuario.tipo_usuario()}")
            print(f"CPF: {conta.usuario.documento()}")
        else:    
            print(f"TIPO DE USUÁRIO: {conta.usuario.tipo_usuario()}")
            print(f"CNPJ: {conta.usuario.documento()}")
        print(f"SALDO: R$ {round(conta.saldo, 2)}")
        print("LISTA DE TRANSAÇÕES")
        for transacao in conta.historico.transacoes:
            print(transacao)
        print("------------------------------------------ FIM ------------------------------------------")