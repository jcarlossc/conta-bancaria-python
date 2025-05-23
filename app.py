
from banco.usuario.PessoaFisica import PessoaFisica
from banco.usuario.PessoaJuridica import PessoaJuridica
from banco.conta.ContaCorrente import ContaCorrente
from banco.conta.ContaPoupanca import ContaPoupanca
from banco.extrato.Extrato import Extrato

ex = Extrato()

pj2 = PessoaJuridica('carlos', 'carlos@email.com', 33333333333)
cp2 = ContaPoupanca(pj2)

pf1 = PessoaFisica('jose', 'jose@email.com', 22222222222)
cc1 = ContaCorrente(pf1)

cc1.depositar(500)
cc1.sacar(100)
cc1.transferir(100, cp2)
ex.acessar_extrato(cc1)

cp2.depositar(5000)
cp2.sacar(1000)
cp2.transferir(1000, cc1)
ex.acessar_extrato(cp2)