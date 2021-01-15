"""
exercise: 014
objective: Escreva um programa que converta uma temperatura digitando em
graus Celsius e converta para graus Fahrenheit.
"""
c = float(input('Informe a temperatura em C°: '))
f = 9 * c / 5 + 32
print(f'A temperatura {c}° é: \033[34m{f}\033[mF°')
