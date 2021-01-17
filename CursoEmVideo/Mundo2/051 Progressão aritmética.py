from os import system

while True:
     system('clear')
     print ("=-"*20)
     print('  10 Termos de uma PA')
     print('=-'*20)
     
     pt = int(input(' Primeiro termo: '))
     rz = int(input(' Razão: '))
     cont = pt + (10 - 1) * rz
     for c in range(pt, cont + rz , rz):
           print(c, end=' > ')
         
     input(' ')
