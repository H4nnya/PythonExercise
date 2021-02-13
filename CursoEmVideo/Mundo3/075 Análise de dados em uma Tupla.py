"""
exercise: 075
objective: Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

numbers = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
           int(input('Digite mais número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os números: {numbers}')
print(f'O valor 9 apareceu {numbers.count(9)} vezes.')
if 3 in numbers:
    print(f'O valor 3 apareceu na {numbers.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram', end='')
for n in numbers:
    if n % 2 == 0:
        print(f' {n}', end='')
