"""
exercise: 072
objective: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis',
        'dezesete', 'dezoito', 'desenove', 'vinte')
while True:
    num = int(input('digite um número entre 0 a 20: '))
    if 0 <= value <= 20:
        print('Tente novamente. ', end='')
    else:
        break
print(f'Você digitou o número {cont[num]}.')
