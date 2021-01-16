from random import choice

print('=-'*20,'\nVou pensar em um número de 0 a 5.Tente adivinhar...')
print('=-'*20)

num = int(input('Em que número eu pensei? '))
lista = [0,1,2,3,4,5]
cpu = choice(lista)

if cpu == num:
     print('O número escolhido foi: {}\n\033[32mParabens, você ganhou!\033[m'.format(cpu))
else:
     print('O número escolhido foi: {}\n\033[31mVocê errou!\033[m'.format(cpu))
