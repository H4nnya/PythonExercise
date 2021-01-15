"""
exercise: 012
objective: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
n = float(input('Qual é o preço do produto? R$'))
des = n - (n * 5 / 100)
print(f'O produto que custava R${n:.2f} na promoção com desconto de 5% vai custar \033[32mR${des:.2f}\033[m.')
