"""
exercise: 010
objective: Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira e mostre quantos dólares ela pode comprar.
"""
real = float(input('Quanto dinheiro você têm? R$'))
print(f'Com \033[32mR${real:.2f}\033[m você consegue \033[32mUS${(real/5.30):.2f}\033[m.')
