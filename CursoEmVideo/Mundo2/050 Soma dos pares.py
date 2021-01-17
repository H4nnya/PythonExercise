# from os import system

while True:
    system('clear')
    soma = 0
    cont = 0
    
    for c in range(1,7):
        n = int(input(f' Digite o {c}° Valor: '))
        if n%2 == 0:
             soma += n
             cont += 1
        
    print(f' Você informou {cont} números PARES\n e a soma é: {soma}.')
    input(' ')
