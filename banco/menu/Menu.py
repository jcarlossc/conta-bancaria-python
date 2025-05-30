import os
import re
from banco.conta.ContaCorrente import ContaCorrente
from banco.conta.ContaPoupanca import ContaPoupanca
from banco.usuario.PessoaFisica import PessoaFisica
from banco.usuario.PessoaJuridica import PessoaJuridica

class Menu:
    """Classe que representa o menu do sistema
    e centraliza as operações. 

    Atributos:
        None.
    """
    def __init__(self) -> None: 
        pass

    @classmethod    
    def acessar_menu(self):
        """Método para acessar o menu, também centraliza 
        todas as operações do sistema.

        Retorna:
            None.
        """
        # Método para limpar tela.
        def limpar_tela():
            os.system('cls' if os.name == 'nt' else 'clear')

        # Função do menu principal.    
        def menu_principal():
            print("\n----------------------------------🚀 BANCO PYTHON 🚀---------------------------------\n")
            print("1 - CADASTRAR USUÁRIO")
            print("2 - CRIAR CONTA")
            print("3 - DEPOSITAR")
            print("4 - SACAR")
            print("5 - TRANSFERIR")
            print("6 - EXTRATO")
            print("7 - SAIR")
            print("\n----------------------------------------- FIM -----------------------------------------\n")

        # Função do menu de cadastro de usuários.
        def menu_cadastro():
            print("\n-------------------------------🚀 CADASTRO DE USUÁRIO 🚀------------------------------\n")
            print("1 - PESSOA FÍSICA")
            print("2 - PESSOA JURÍDICA")
            print("3 - SAIR")
            print("\n----------------------------------------- FIM -----------------------------------------\n")   

        # Função do menu da criação de conta.
        def menu_conta():
            print("\n--------------------------------🚀 CROAÇÃO DE CONTA 🚀--------------------------------\n")
            print("1 - CONTA CORRENTE")
            print("2 - CONTA POUPANÇA")
            print("3 - SAIR")
            print("\n----------------------------------------- FIM -----------------------------------------\n")    

        limpar_tela()

        # While principal.
        while True:
            menu_principal()
            operacao = input(f'🔍 ESCOLHA UMA OPERAÇÂO: ')

            # Condicional cadasto de usuário.
            if operacao == "1":
                limpar_tela()

                # While cadastro do usuário.
                while True:
                    # Função que valida email.
                    def validar_email(email):
                        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                        return re.match(padrao, email) is not None
                    
                    menu_cadastro()
                    cadastro_usuario = input(f'🔍 ESCOLHA UMA OPERAÇÃO: ')

                    # Condicional cadastro de pessoa física.
                    if cadastro_usuario == "1":

                        # Entradas para nome, email e cpf de pessoa física.
                        nome_pessoa_fisica = input(f'🔍 DIGITE SEU NOME: ')
                        email_pessoa_fisica = input(f'🔍 DIGITE SEU EMAIL: ')
                        cpf_pessoa_fisica = input(f'🔍 DIGITE SEU CPF: ')

                        # Condicional que valida nome, email e cpf de pessoa física.
                        if nome_pessoa_fisica.replace(" ", "").isalpha() and validar_email(email_pessoa_fisica) and cpf_pessoa_fisica.isdigit():
                            cpf_pessoa_fisica_int = int(cpf_pessoa_fisica)

                            # Instância de PessoaFísica.
                            pessoa_fisica = PessoaFisica(nome_pessoa_fisica, email_pessoa_fisica, cpf_pessoa_fisica_int)

                            limpar_tela()
                            print(f"✅ {pessoa_fisica.nome.title()} | Pessoa Física cadastrada com sucesso!")

                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida! Tente novamente") 
                            print(f'✅ NOME: somente caracteres alfabéticos.') 
                            print(f'✅ EMAIL: formato: nome@email.com.') 
                            print(f'✅ CPF: somente caracteres numéricos.') 

                    # Condicional cadastro de pessoa jurídica.
                    elif cadastro_usuario == "2":
                        
                        # Entradas para nome, email e cpf de pessoa jurídica.
                        nome_pessoa_juridica = input(f'🔍 DIGITE SEU NOME: ')
                        email_pessoa_juridica = input(f'🔍 DIGITE SEU EMAIL: ')
                        cnpj_pessoa_juridica = input(f'🔍 DIGITE SEU CNPJ: ')

                        # Condicional que valida nome, email e cpf de pessoa jurídica.
                        if nome_pessoa_juridica.replace(" ", "").isalpha() and validar_email(email_pessoa_juridica) and cnpj_pessoa_juridica.isdigit():
                            cnpj_pessoa_juridica_int = int(cnpj_pessoa_juridica)

                            # Instância de PessoaFísica.
                            pessoa_juridica = PessoaJuridica(nome_pessoa_juridica, email_pessoa_juridica, cnpj_pessoa_juridica_int)

                            limpar_tela()
                            print(f"✅ {pessoa_juridica.nome.title()} | Pessoa jurídica cadastrada com sucesso!")

                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida! Tente novamente") 
                            print(f'✅ NOME: somente caracteres alfabéticos.') 
                            print(f'✅ EMAIL: formato: nome@email.com.') 
                            print(f'✅ CPF: somente caracteres numéricos.') 
                            
                    # Condicional para sair do cadastro de usuários.
                    elif cadastro_usuario == "3":
                        break

                    else:
                        limpar_tela()
                        print(f"❌ Opção inválida!")       

                limpar_tela()        

            elif operacao == "2":
                pass
            elif operacao == "3":
                pass
            elif operacao == "4":
                pass
            elif operacao == "5":
                pass
            elif operacao == "6":
                pass
            elif operacao == "7":
                limpar_tela()
                print("SAIR, ATÉ A PRÓXIMA!")
                exit()
            
            else:
                limpar_tela()
                print("❌ Opção inválida!")