"""
exercise: 006
objective: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
while True:
    n = int(input(f'Digite um número[ou 0 para sair: '))
    if n == 0:
        break
    print(f'O dobro de {n} vale: {n*2}.')
    print(f'O triplo de {n} vale: {n*3}.')
    print(f'A raiz quadrada de {n} vale: {n**(1/2):.2f}.')
