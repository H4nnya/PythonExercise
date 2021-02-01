""""
Exercício: 11
Objetivo: Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.
"""

n1 = int(input("Digite um número inteiro: "))
n2 = int(input('Digite outro número inteiro: '))
n3 = float(input('Digite um número real: '))
print(f"O dobro de {n1} é {n1*2} e a metade de {n2} é {n2/2}")
print(f'O tripo de {n1} mais {n3} é igual a {(n1*3)+n3}')
print(f'O resultado de {n3} elevado ao cubo é {n3**3}')
