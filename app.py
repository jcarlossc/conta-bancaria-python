from banco.usuario.PessoaFisica import PessoaFisica
from banco.usuario.PessoaJuridica import PessoaJuridica

pj1 = PessoaJuridica('carlos', 'carlos@gmail.com', 789)
print(pj1, pj1.cnpj, pj1.nome, pj1.email, pj1.tipo_usuario(), pj1.documento())

pf1 = PessoaFisica('jose', 'jose@gmail.com', 123)
print(pf1, pf1.cpf, pf1.nome, pf1.email, pf1.tipo_usuario(), pf1.documento())