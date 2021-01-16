from math import hypot

co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
hi = hypot(co,  ca)

# hipotenusa = (co ** 2 + ca ** b2) ** (1/2)
print('A hipotenusa vai medir: {:.2f}'.format(hi))
