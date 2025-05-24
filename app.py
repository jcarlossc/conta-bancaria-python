
from banco.usuario.PessoaFisica import PessoaFisica
from banco.usuario.PessoaJuridica import PessoaJuridica
from banco.conta.ContaCorrente import ContaCorrente
from banco.conta.ContaPoupanca import ContaPoupanca
from banco.extrato.Extrato import Extrato

ex = Extrato()

pj2 = PessoaJuridica('jose carlos', 'carlos@email.com', 12345678998)
cp2 = ContaPoupanca(pj2)

pf1 = PessoaFisica('maria jose', 'jose@email.com', 98765432198765)
cc1 = ContaCorrente(pf1)

cc1.depositar(500)
cc1.sacar(100)
cc1.transferir(100, cp2)
ex.acessar_extrato(cc1)

cp2.depositar(5000)
cp2.sacar(1000)
cp2.transferir(1000, cc1)
ex.acessar_extrato(cp2)