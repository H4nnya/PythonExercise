fat = int(input(' Digite um número para ver seu fatorial: '))
c1 = 1
cont = fat

while cont > 0:
    c1 *= fat
    print(f' {cont}', end='')
    fat -= 1
    cont -= 1
    
    if cont > 0:
         print(' x ', end='')
    else:
         print(' = ', end='')
print(f'\033[32m{c1} \033[m')
