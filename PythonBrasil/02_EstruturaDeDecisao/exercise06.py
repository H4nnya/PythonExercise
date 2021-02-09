"""
Faça um Programa que leia três números e mostre o maior deles.
"""

maior = 0
for n in range(1, 4):
    number = int(input(f'Digite o {n}° número: '))
    if number > maior:
        maior = number
print(f'O maior número é o {maior}.')
