from banco.extrato.Extrato import Extrato
from banco.usuario.PessoaFisica import PessoaFisica
from banco.usuario.PessoaJuridica import PessoaJuridica
from banco.conta.ContaCorrente import ContaCorrente
from banco.conta.ContaPoupanca import ContaPoupanca

pf1 = PessoaFisica('Carlos da Costa', 'carloscosta@gmail.com', 12345678978)
pj1 = PessoaJuridica('Jose Carlos', 'josecarlos@gmail.com', 98765432132165)

cc1 = ContaCorrente(pf1)
cc2 = ContaPoupanca(pj1)


cc2.depositar(5000)
cc2.sacar(1000)
cc2.transferir(1000, cc1)

cc1.depositar(500)
cc1.sacar(200)
cc1.transferir(100, cc2)



ex = Extrato()
ex.acessar_extrato(cc1)
ex.acessar_extrato(cc2)

