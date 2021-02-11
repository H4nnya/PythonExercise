"""
exercise: 074
objective: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados
e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

number = (randint(1, 10), randint(1, 10), randint(1, 10),
          randint(1, 10), randint(1, 10))
print("Os valores sorteados foram:", end='')
for n in range(0, 5):
    print(f" {number[n]}", end='')

print(f'\nO maior valor sorteado foi {max(number)}')
print(f'O menor valor sorteado foi {min(number)}')

