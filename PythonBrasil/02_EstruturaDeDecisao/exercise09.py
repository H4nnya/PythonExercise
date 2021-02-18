"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
numbers = []
for n in range(1, 4):
    numbers.append(int(input(f'Digite o {n}º número: ')))
numbers.sort(reverse=True)
print('Os números digitados em ordem decrescente ficam:', end='')
for n in range(0, 3):
    print(f' {numbers[n]}', end='')
