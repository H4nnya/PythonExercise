from os import system

while True:
      system('clear')
      num1 = int(input(' Primeiro número: '))
      num2 = int(input(' Segundo número: '))
 
      if num1 > num2:
            print('\n O PRIMEIRO número é maior.')
            input(' \033[32mEnter... \033[m')
      elif num1 < num2:
            print('\n O SEGUNDO número é maior.')
            input(' \033[32mEnter... \033[m')
      else:
            print('\n Os dois valores são IGUAIS.')
            input(' \033[32mEnter... \033[m')
