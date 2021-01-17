from os import system
system('clear')

while True:
    n = int(input(' Digite um número para ver a sua tabuada: '))
    if n > -1:
         for c in range(1, 11):
              print(f' {n} x {c:2} = {c*n}')
    else:
         break
        
system('clear')
print(' PROGRAMA ENCERRADO! Volte sempre.')   
