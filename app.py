from banco.usuario.PessoaFisica import PessoaFisica
from banco.usuario.PessoaJuridica import PessoaJuridica
from banco.conta.ContaCorrente import ContaCorrente
from banco.conta.ContaPoupanca import ContaPoupanca

pf2 = PessoaJuridica('carlos', 'carlos@email.com', 987654)
cc2 = ContaPoupanca(pf2)

pf1 = PessoaFisica('jose', 'jose@email.com', 123456)
cc1 = ContaCorrente(pf1)

cc1.depositar(500)
cc1.sacar(100)
cc1.transferir(100, cc2)
print(cc1.historico.acessa_transacoes())