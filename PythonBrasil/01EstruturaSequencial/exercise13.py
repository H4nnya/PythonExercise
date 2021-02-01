""""
Exercício: 13
Objetivo: Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
"""

h = float(input('Digite sua altura: '))
sx = str(input('Qual é o seu sexo?[M/F] ')).upper()[:1]
peso = 0
if sx in 'M':
    peso = (72.7 * h) - 58
elif sx == 'F':
    peso = (62.1 * h) - 44.7

print(f"O seu peso ideal seria {peso:.2f}")
