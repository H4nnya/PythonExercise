from os import system

while True:
    system('clear')
    n = int(input(' Digite um número: '))
    
    for c in range(0, 11):
         print(' {:2} × {:2} = {:2}'.format(n, c, n*c))
    input(' ')
