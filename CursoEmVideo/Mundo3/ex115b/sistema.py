from ex115b.lib.interface import *
from ex115b.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Criar arquivo', 'Cadastrar pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de lista o conteúdo de um arquivo
        leiaArquivo(arq)
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! digite uma opção válida!\033[m')
    sleep(2)
