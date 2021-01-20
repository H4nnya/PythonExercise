from ex115a.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Criar arquivo', 'Cadastrar pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! digite uma opção válida!\033[m')
    sleep(2)
