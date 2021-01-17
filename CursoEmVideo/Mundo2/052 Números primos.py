from os import system

while True:
    system('clear')
    n = int(input(' Digite um número inteiro: '))
    total = 0
    for c in range(1, n + 1 ): 
        if n % c == 0:
             print(f'\033[32m {c} ', end='')
             total += 1

        else:
             print(f'\033[31m {c}', end='')
   
    print(f'\n\033[mO número {n} foi divisivel {total} vezes.')

    if total == 2:
        print('E por isso ele é PRIMO.')

    else:
        print('E por isso ele não é PRIMO.')

    input()
