from random import randint
from time import sleep

print('\33[33m=='*20)
print('\033[34m Vou pensar em um número de 0 a 5.\n tente adivinhar...\n','\033[33m==\033[m'*20)

numeric = int(input(' Digite um número: '))
num = randint(0,5)

print(' Processando...\n')
sleep(1.2)

if numeric == num:
     print('\033[32m Parabéns, você acertou!\033[m')
 
else:
     print(f'\033[31m Você perdeu, eu pensei em {num}.\n tente novamente...\033[m')
