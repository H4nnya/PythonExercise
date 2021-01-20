from ex115c.lib.interface import *
from ex115c.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        leiaArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho("NOVO CADASTRO")
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma nova opção no menu...
        print('\033[31mErro! digite uma opção válida!\033[m')
    sleep(2)
