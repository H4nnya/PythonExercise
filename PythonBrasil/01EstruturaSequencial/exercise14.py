""""
Exercício: 14
Objetivo: faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável
excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
limite = 50klg
multa = R$4 por quilo
"""

peso = float(input('Digite o peso em quilos do peixe: '))
print(f'Hoje a sua pesca foi de {peso}kg.')
if peso > 50:
    excesso = peso - 50
    multa = str(excesso * 4).replace('.', ',')
    print(f"Você ultrapassou {excesso}kg do limite de 50kg. você pagara R${multa} de multa. ")
else:
    print('Volte sempre!')
