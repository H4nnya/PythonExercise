from math import radians,sin,cos, tan
angulo = int(input('Digite o ângulo: '))

seno = sin(radians(angulo))
print('O seno de {:.2f}° é {:.2f}'.format(angulo,seno))

cosseno = cos(radians(angulo))
print('O cosseno de {:.2f}° é: {:.2f}'.format(angulo, cosseno))

tangente = tan(radians(angulo))
print('A tangente de {:.2f}° é: {:.2f}'.format(angulo, tangente))
