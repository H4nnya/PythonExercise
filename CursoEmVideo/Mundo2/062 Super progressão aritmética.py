from os import system
system('clear')

pt = int(input('Primeiro termo: '))
raz = int(input('Razão: '))

termo = pt
cont1 = 1
cont2 = 10
go = False
cont_term  = 10

while cont2 > 0:
    
    while cont1 <= cont2:
        go = True
        print(f'\033[32m{termo}\033[m', end='')
        termo += raz
        cont1 += 1
        
        if cont1 <= cont2:
            print(' => ', end='')
            
        else:
            print('  PAUSA', end='')
    
    while  go == True:
        cont1 = 1
        cont2 = int(input('\n\n Quantos termos você quer mostrar a mais? '))
        cont_term += cont2
        go = False
        
print(f'\nA progressão foi finalizada com {cont_term} Termos.')    
