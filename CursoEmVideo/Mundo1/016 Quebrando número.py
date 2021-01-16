"""
exercise: 016
objective: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""
from math import trunc

n = float(input('Digite um número Decimal: '))
print(f'O número {n} com a sua poção inteira é: \033[32m{trunc(n)}\033[m.')
