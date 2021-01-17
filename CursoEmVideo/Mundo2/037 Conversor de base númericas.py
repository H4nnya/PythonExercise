import os
os.system('cls' if os.name == 'nl' else 'clear')

while 1:
 os.system('cls' if os.name == 'nl' else 'clear')
 num = int(input(' Digite um número inteiro: ')) 
 es = int(input(''' Escolha uma das bases para conversão:
 	(1)Converter para Binário
 	(2)Converter para octal
 	(3) Converter para hexadecimal\n  >> '''))
 	
 
 if es == 1:
     print(' \033[33m{}\033[m Convertido para Binário é igual a:\n \033[32m {}\033[m'.format(num , bin(num)[2:]))
     input('\n Aperte \033[32menter\033[m para iniciar novamente... ')
     
 elif es == 2:
     print(' \033[33m{}\033[m Convertido para octal é igual a\n \033[32m{}\033[m '.format(num, oct(num)[2:])) 
     input('\n Aperte \033[32menter\033[m para iniciar novamente... ')

 elif es == 3:
     print(' \033[33m{}\033[m Convertido para Hexadecimal é igual a\n \033[32m{}\033[m '.format(num , hex(num)[2:]))
     input('\n Aperte \033[32menter\033[m para iniciar novamente... ')
 
 else:
     input('\n Digite um valor válido\n Aperte \033[32mEnter\033[m para inicar novamente... ')
