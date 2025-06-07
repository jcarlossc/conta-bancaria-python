# PROJETO PYTHON VENV - CONTA BANCÁRIA

Estudo sobre orientação a objetos e os respectivos testes unitário em linguagem de programação Python e ambiente virtual VENV.

VENV: Um ambiente virtual em Python isola dependências do projeto, evitando conflitos com pacotes globais do sistema. Ele permite que cada projeto tenha suas próprias bibliotecas e versões específicas.

## Ferramentas utilizadas
* Linguagem de programação Python 3.9.13.
* Ambiente virtual VENV.
* Git/GitHub
* Visual studio code.
* Windows 10.

## Modo de utilizar
* Clonar repositório.
* Entrar no diretório do projeto ```cd conta-bancaria-python```. 
* Executar ```python -m venv venv``` para instalar o ambiente virtual.
* Executar, caso esteja no Windows, ```venv\Scripts\activate``` para iniciar o ambiente. Caso Linux ou MacOS, ```source venv/bin/activate```.
* Executar ```pip install -r requirements.txt``` para instalar as dependências, caso o projeto as tenha. Obs: Este projeto não contém módulos extenos.
* ```python app.py``` - Executa o algoritmo.
* Para sair do ambiente virtual ```deactivate```.

O projeto também conta com classes de testes unitários com módulo 'unittest'. Seguem abaixo os comandos para serem executados na raiz do projeto.
* ```python -m unittest tests/banco/usuario/TestUsuario.py```
* ```python -m unittest tests/banco/usuario/TestPessoaFisica.py```
* ```python -m unittest tests/banco/usuario/TestPessoaJuridica.py```
* ```python -m unittest tests/banco/conta/TestContaBancaria.py```
* ```python -m unittest tests/banco/conta/TestContaCorrente.py```
* ```python -m unittest tests/banco/conta/TestContaPoupanca.py```
* ```python -m unittest tests/banco/transacao/TestTransacao.py```
* ```python -m unittest tests/banco/transacao/TestDeposito.py```
* ```python -m unittest tests/banco/transacao/TestSaque.py```
* ```python -m unittest tests/banco/transacao/TestTransferencia.py```
* ```python -m unittest tests/banco/historico/TestHistorico.py```
* ```python -m unittest tests/banco/extrato/TestExtrato.py```

## Contribuição:
Se quiser contribuir para este projeto, fique à vontade para enviar um pull request ou relatar problemas na seção de issues.

## Licença:
Este projeto é licenciado sob a Licença MIT.

## COMANDOS IMPORTANTES
* ```python -m venv venv``` - Cria um ambiente virtual chamado venv. Observação: o primeiro venv é o comando, o segundo, o nome do diretório.
* No Windows, ```venv\Scripts\activate``` e no Linux, ```source venv/bin/activate``` - Inicializa o ambiente.
* ```deactivate``` - Encerra o ambiente.
* ```pip freeze > requirements.txt``` - Gera o arquivo para instalação de dependências. Esse mesmo comando atualiza o arquivo quando uma dependência for instalada.
* ```pip list``` - Lista as dependências do projeto.
* ```pip show``` - Inserindo o nome da dependência após o comando, lista informações da dependência.
* ```pip install -r requirements.txt``` - Instala dependências que estão no arquivo 'requirements.txt'.
* ```pip install``` - Inserindo o nome da dependência após o comando, instala dependências.
* ```pip uninstall``` - Inserindo o nome da dependência após o comando, desinstala dependências.
