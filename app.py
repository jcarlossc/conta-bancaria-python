from banco.extrato.Extrato import Extrato
from banco.usuario.PessoaFisica import PessoaFisica
from banco.usuario.PessoaJuridica import PessoaJuridica
from banco.conta.ContaCorrente import ContaCorrente
from banco.conta.ContaPoupanca import ContaPoupanca

pf1 = PessoaFisica('Carlos da Costa', 'carloscosta@gmail.com', 12345678978)
pj1 = PessoaJuridica('Jose Carlos', 'josecarlos@gmail.com', 98765432132165)

cc1 = ContaCorrente(pf1)
cc2 = ContaPoupanca(pj1)

try:
    cc2.depositar(5000)
except Exception as e:
    print(f"[ERRO] Depósito inválido em cc2: {e}")

try:
    cc2.sacar(5500)
except Exception as e:
    print(f"[ERRO] Saque em cc2: {e}")

try:
    cc2.transferir(1000, cc1)
except Exception as e:
    print(f"[ERRO] Transferência de cc2 para cc1: {e}")

try:
    cc1.depositar(500)
except Exception as e:
    print(f"[ERRO] Depósito em cc1: {e}")

try:
    cc1.sacar(200)
except Exception as e:
    print(f"[ERRO] Saque em cc1: {e}")

try:
    cc1.transferir(100, cc2)
except Exception as e:
    print(f"[ERRO] Transferência de cc1 para cc2: {e}")

try:
    ex = Extrato()
    ex.acessar_extrato(cc1)
    ex.acessar_extrato(cc2)
except Exception as e:
    print(f"[ERRO] Acesso ao extrato: {e}")

