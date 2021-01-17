from datetime import date
from os import system, name

atual = date.today().year

while 1:
    system('cls' if name == 'nl' else 'clear')
    ano = int(input(' Ano de Nascimento: '))
    idade = atual - ano
    print(f'\n O atleta tem {idade} anos.')
    
    if idade <= 9:
        print(' Classificação: MIRIM')
    
    elif idade < 15:
        print(' Classificação: INFANTIL')
        
    elif idade < 20:
        print(' Classificação: JUNIOR')
        
    elif idade < 26:
        print(' Classificação: SêNIOR')
        
    else:
        print(' Classificação: MASTER')
    
    input ('\n Aperte \033[35mEnter\033[m para reiniciar... ')
        
