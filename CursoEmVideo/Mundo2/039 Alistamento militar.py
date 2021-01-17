import os
from datetime import date

while True:
      os.system('cls' if os.name == 'nl' else 'clear')
      print('\n \033[32mALISTAMENTO MILITAR\033[m\n')
 
 
      sexo = int(input(' Qual é o seu sexo?\n \033[34m(1)\033[mMASCULINO\n \033[34m(2)\033[mFEMUNINO\n\n >> '))
      if sexo == 1:
            ano = int(input(' \033[35mAno de nascimento:\033[33m '))
            hoje = date.today().year
            idade = hoje-ano
            print(f'\n\033[m Quem nasceu em {ano} tem {idade} anos em {hoje}.')

      if idade == 18:
            print(' Você tem que se alistar \033[31mIMEDIATAMENTE!\033[m')
    
      elif idade < 18:
            ano = ano + 18
            anos1 = 18 - idade
            print(f' Seu alistamento será em \033[32m{ano}\033[m.')
            print(f' Ainda faltam {anos1} anos para o alistamento.')
    
      elif idade > 18:
            ano = ano + 18
            print(' Você já deveria ter se alistado há {} anos.'.format(hoje - ano))
            print(f' Seu alistamento foi em {ano}')
    
      else:
            print(' Seu alistamento não é obrigatório!')
      input('\n Aperte \033[36mEnter\033[m para reimiciar... ')
