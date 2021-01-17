from os import system

go = True
while go == True:
    system('clear')
    
    print('='*20)
    pterm = int(input('Primeiro termo: '))
    raz = int(input('Razão: '))
    print('='*20)

    term = pterm
    cont = 1

    while cont <= 10:
        print(f'{term}', end='')
        term += raz
        cont += 1
        
        if cont < 11:
            print(' => ', end='')            
            
    input('\n\n	Aperte \033[35mEnter\033[m para continuar...')       
