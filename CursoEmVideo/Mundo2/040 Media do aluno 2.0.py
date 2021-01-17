import os 
os.system('cls' if os.name == 'nl' else 'clear')

while True:
     os.system('cls' if os.name == 'nl' else 'clear')
     nota1 = float(input(' Primeira nota do aluno: '))
     nota2 = float(input(' Segunfa nota do aluno: '))
     media = (nota1/2) + (nota2/2)
     print('\n A Média do aluno é {:.2f}'.format(media))
 	
     if media < 5:
          print(' o aluno foi \033[31mREPROVADO\033[m.')

     elif media >= 5 and media <= 6.99:
          print(' O aluno está de \033[33mRECUPERAÇÃO\033[m.')

     elif media >= 7:
          print(' O aluno foi \033[33mAPROVADO\033[m.')
    
     input('\n Aperte ENTER para continuar.... ')
