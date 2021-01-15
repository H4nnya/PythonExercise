"""
exercise: 007
objective: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'A média entre {n1:.1f} e {n2:.1f} é: {media:.1f}')
