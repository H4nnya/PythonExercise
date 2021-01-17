from os import system
system('clear')

go = False

while True:
     v1 = int(input(' Digite o primeiro valor: '))
     v2 = int(input(' Digite o segundo valor: '))   
     go = True 
  
     while go ==  True:
          n = int(input('''\n [1]Somar 
 [2]Multiplicar  
 [3]Maior 
 [4]Novos números
 [5]Sair do programa
 \n >> '''))

          if n == 1:
               valor = v1 + v2
               print(f' {v1} + {v2} = {valor}')
               input()

          elif n == 2:
               valor = v1*v2
               print(f' {v1} x {v2} = {valor}')
               input()
    
          elif n == 3:
               if v1 > v2:
                    print(f' o valor {v1} é maoir que {v2}.')
         
               elif v1 < v2:
                    print(f' O valor {v2} é maior que {v1}.')

               else:
                    print(f' Os dois valores são iguais.')
               input()

          elif n == 4:
               system('clear')
               go = False

          elif n == 5:
               system('clear')
               print(' Volte sempre!:)')
               exit()    
          system('clear')
