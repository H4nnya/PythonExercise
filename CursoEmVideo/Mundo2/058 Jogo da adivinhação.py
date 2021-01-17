from random import randint
from os import system

system('clear')

cpu = randint(0, 10)
tentativas = 0
acerto = False

print(' Eu pensei em um número entre 1 e 10, tente adivinhar.')

while not acerto:
    
    player = int(input(' >> '))
    
    if player == cpu:
         print(f' Você acertou!!!')
         tentativas += 1
         acerto = True
       
    elif player > cpu:
          print(' Menos...tente novamente.')
          tentativas += 1
        
    elif player < cpu:
          print(' Mais...tente novamente.')
          tentativas += 1
   
    else:
          print(' Error...tente novamente.')
    
print(f' Na {tentativas}° tentativa. Parabéns!')
