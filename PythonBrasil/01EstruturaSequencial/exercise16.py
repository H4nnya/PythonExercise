""""
Exercício: 16
Objetivo: Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
metros = float(input('Digite o tamanho em metros quadrados da parede: '))
m = metros
litros = 0
while True:
    if m - 54 >= 0:
        m -= 54
        litros += 1
    elif m > 0:
        m -= m
        litros += 1
    if m <= 0:
        break

preco = str(80.00 * litros).replace('.', ',')
print(f'Com a parede de {metros}m² você precisa comprar {litros} litro(s) de tinta, tudo isso custará R${preco}')
