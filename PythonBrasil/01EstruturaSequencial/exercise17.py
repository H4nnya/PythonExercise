""""
Exercício: 17
Objetivo: Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
 que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""


def banner():
    print('''====================================
\033[33m        ___ _ _ ___ ___
       |_ -| - | . | . |
       |___|_-_|___|  _|
                   |_|\033[m
====================================
 ''')


def input_error():
    print('\033[31mErro de digitação! O valor digitado não exite, tente novamente.\033[m')


def option():
    print('''Suas opções de compras:
    [1] Apenas R$80,00 cada latas de 18 litros
    [2] Apenas R$25,00 cada galões de 3,6 litors 
    [3] Misturar latas e lagões (Mais econômico)''')


start = True
while start:
    banner()
    meters = float(input('Digite a área da sua parede em metros quadrados(m²): '))
    m = meters
    liter1 = liter2 = price = 0
    while True:
        option()
        res = int(input('>> '))
        if res == 1:
            while True:
                if m - 108 >= 0:
                    m -= 108
                    liter1 += 1
                elif m > 0:
                    m -= m
                    liter1 += 1
                else:
                    price = f'{(80 * liter1):.2f}'.replace('.', ',')
                    liters = liter1
                    break
        elif res == 2:
            while True:
                if m - 21 >= 0:
                    m -= 21
                    liter2 += 1
                elif m > 0:
                    m -= m
                    liter2 += 1
                else:
                    price = f'{(25 * liter2):.2f}'.replace('.', ',')
                    liters = liter2
                    break
        elif res == 3:
            while True:
                if m - 108 >= 0:
                    m -= 108
                    liter1 += 1
                elif m - 21 > 0:
                    m -= 21
                    liter2 += 1
                elif m > 0:
                    m -= m
                else:
                    price = f'{((80 * liter1) + (25 * liter2)):.2f}'.replace('.', ',')
                    break
        else:
            input_error()
        if m == 0:
            break
    print(f'\033[34mCom uma parede de {meters}m² você precisará comprar,', end='')
    if res == 3:
        print(f'{liter1}l de latas e {liter2}l de galões de tinta.')
    else:
        print(f'{liters}l de tinta. ', end='')

    print(f'\n\033[32mPreço total: R${price}')
    start = False
