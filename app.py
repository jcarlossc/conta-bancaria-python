from banco.usuario.PessoaFisica import PessoaFisica
from banco.usuario.PessoaJuridica import PessoaJuridica
from banco.conta.ContaCorrente import ContaCorrente

pj1 = PessoaJuridica('carlos', 'carlos@gmail.com', 789)
print(pj1, pj1.cnpj, pj1.nome, pj1.email, pj1.tipo_usuario(), pj1.documento())

pf1 = PessoaFisica('jose', 'jose@gmail.com', 123)
print(pf1, pf1.cpf, pf1.nome, pf1.email, pf1.tipo_usuario(), pf1.documento())

cc1 = ContaCorrente(pf1)
cc2 = ContaCorrente(pj1)

cc1.depositar(500.65)
cc1.sacar(200)
cc1.transferir(100, cc2)
print(cc1.saldo)