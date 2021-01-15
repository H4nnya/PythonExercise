"""
exercise: 008
objective: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""
m = float(input('Digite a distância em metros: '))
print(f'A medida {m}m corresponde a\n\033[32m{m/1000}km\n{m/100}hm\n{m/10}dam')
print(f'{m*10}dm\n{m*100}cm\n{m*100}mm\033[m')
