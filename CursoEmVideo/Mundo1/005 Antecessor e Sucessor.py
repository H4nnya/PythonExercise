"""
exercise: 005
objective: faça um programa que leia um número inteiro e mostre na tela seu sucessor e antecessor.
"""
n = int(input('digite um número: '))
print(f'mAnalisando o valor \033[33m{n}\033[m...')
print(f'Seu antecessor é \033[32m{n-1}\033[m e seu sucesso é \033[32m{n+1}\033[m.')
