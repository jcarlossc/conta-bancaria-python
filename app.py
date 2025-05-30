from banco.extrato.Extrato import Extrato
from banco.usuario.PessoaFisica import PessoaFisica
from banco.usuario.PessoaJuridica import PessoaJuridica
from banco.conta.ContaCorrente import ContaCorrente
from banco.conta.ContaPoupanca import ContaPoupanca


pj1 = PessoaJuridica('carlos', 'carlos@gmail.com', 789)

pf1 = PessoaFisica('jose', 'jose@gmail.com', 123)

cc1 = ContaCorrente(pf1)
cc2 = ContaPoupanca(pj1)

cc1.depositar(500)
cc1.sacar(200)
cc1.transferir(100, cc2)

cc2.depositar(5000)
cc2.sacar(100)
cc2.transferir(1000, cc1)



ex = Extrato()
ex.acessar_extrato(cc1)



ex.acessar_extrato(cc2)