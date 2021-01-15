"""
exercise: 011
objective:  Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""
b = float(input('Àrea da parede: '))
h = float(input('Altura da parede: '))
a = b * h
print(F'A área da parede é de {a}m².\nPara pintar a parede, você precisará de \033[32m{a/2}\033[ml de tinta.')
