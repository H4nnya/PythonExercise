"""
Exercício: 071
Objetivo: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""


def space(val):
    print('=' * val)


notes = {50: 0, 20: 0, 10: 0, 1: 0}
space(30)
print(f'{"BANCO S.A.Y":^30}')
space(30)
money = int(input('Qual valor você quer sacar? R$'))
while True:
    if money <= 0:
        break
    for number in notes:
        while True:
            if money - number >= 0:
                money -= number
                notes[number] += 1
            else:
                break
for number in notes:
    if notes[number] >= 1:
        print(f'Total de {notes[number]} cédulas de R${number}')
space(30)
print('Volte sempre ao banco S.A.Y!')

