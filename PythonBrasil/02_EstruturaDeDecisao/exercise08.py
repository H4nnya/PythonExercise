"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""
name = str()
manor = float()
print('     O MENOR PREÇO AQUI')
for n in range(1, 4):
    product = str(input(f'Digite o nome do {n}° produto: '))
    price = float(input('Digite o preço do produto: R$'))
    if n == 1:
        name = product
        menor = price
    elif price < menor:
        name = product
        menor = price
    print('='*30)
print(f"O produto {name} que custa R${str(menor).replace('.',',')} é o mais barato da lista.")
