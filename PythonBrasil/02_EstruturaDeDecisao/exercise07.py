"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

maior = menor = 0
for n in range(1, 4):
    number = int(input(f'Digite o {n}° número: '))
    if number > maior:
        maior = number
    if n == 1:
        menor = number
    elif number < menor:
        menor = number
print(f'O maior número é o {maior} e o menor é o {menor}')
