"""
Faça um Programa que peça dois números e imprima o maior deles.
"""

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número: '))
maior = 0
if n1 >= n2:
    maior = n1
else:
    maior = n2
print(f'O maior número é o {maior}')
