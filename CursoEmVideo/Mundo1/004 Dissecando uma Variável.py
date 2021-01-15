"""
exercise: 004
objective: Faça um programa que leia algo pelo teclado e mostre na tela o
seu tipo primitivo e todas as informações possíveis sobre ele.

"""


def tipo(text='string', value='True or False'):
    print(text, end='')
    if value:
        print(f'\033[34m{value}\033[m')
    else:
        print(f'\033[31m{value}\033[m')


n = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(n)}')
tipo('Só tem espaço? ', n.isspace())
tipo('É número? ', n.isnumeric())
tipo('É alfabético? ', n.isalpha())
tipo('É alfanumérico? ', n.isalnum())
tipo('Está em maiúsculo? ', n.isupper())
tipo('Está em minúsculo? ', n.islower())
tipo('Está capitalizado? ', n.istitle())
