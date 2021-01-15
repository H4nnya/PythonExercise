"""
exercise:009
objective: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
"""

n = int(input('digite um número: '))
print('\033[32m=\033[m'*15)
print(f'{n} × {2:2} = {n*2} \n{n} × {3:2} = {n*3}\n{n} × {4:2} = {n*4}')
print(f'{n} × {5:2} = {n*5} \n{n} × {6:2} = {n*6}\n{n} × {7:2} = {n*7}')
print(f'{n} × {8:2} = {n*8} \n{n} × {9:2} = {n*9}\n{n} × 10 = {n*10}')
print('\033[32m=\033[m'*15)
