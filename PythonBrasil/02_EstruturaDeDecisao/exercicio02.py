"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

number = int(input('Digite um número: '))
print(f'O número {number} é ', end='')
if number > 0:
    print('POSITIVO.')
elif number < 0:
    print('NEGATIVO.')
else:
    print('NEUTRO.')
