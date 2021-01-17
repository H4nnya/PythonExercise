from os import system
from time import sleep
from random import randint

while True:
  system('clear')
  print(''' Suas opções:
   [1]Pedra
   [2]papel
   [3]Tesoura''')
  
  int0 = {1 : 'PEDRA', 2 : 'PAPEL', 3 : 'TESOURA'}
  cpu = randint(1, 3)
  jg = int(input(' Qual é a sua jogada? '))
   
  sleep(0.5)
  print(' \033[35mJO')
  sleep(1)
  print(' \033[34mKEN')
  sleep(1)
  print(' \033[32mPO!!!\033[m')
      
  print('-='*20)
  print(' Computador jogou \033[36m{}\33[m'.format(int0[cpu]))
  print(f' Jogandor jogou \033[36m{int0[jg]}\033[m')
  print('-='*20)

  if cpu == 1:
      if jg == 1:
          print(' \033[33mEMPATE\033[m')
          
      elif jg == 2:
          print(' \033[32mJOGADOR GANHOU!!!\033[m')
          
      elif jg == 3:
          print(' \033[31mJOGADOR PERDEU\033[m')
          
      else:
          print(' Jogada inválida.')
          
      
  elif cpu == 2:
      if jg == 1:
          print(' \033[31mJOGADOR PERDEU\033[m')
          
      elif jg == 2:
          print(' \033[33mEMPATE\033[m')
          
      elif jg == 3:
          print(' \033[32mJOGADOR GANHOU!!!\033[m')
          
      else:
          print(' Jogada inválida.')
       
  elif cpu == 3:
      if jg == 1:
          print(' \033[32mJOGADOR GANHOU!!!\033[m')
          
      elif jg == 2:
          print(' \033[31mJOGADOR PERDEU\033[m')
          
      elif jg == 3:
          print(' \033[33mEMPATE\033[m')
          
          
      else:
          print(' Jogada inválida.')
          
  input('\n Aperte \033[35mEnter\033[m para reiniciar...')
