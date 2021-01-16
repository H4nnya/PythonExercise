go = 'y'

while go == "y":
      n = float(input('Qual é o salario de funcionário?: R$'))
      if n < 1251:
           nw = (n/100)*15
           print('O funcionário que ganhavar R${:.2f} vai comecar a gannhar R${:.2f} .'.format(n,(nw+n)))
           
      elif n >= 1250:
            nw1 = (n/100)*10
            print('O funcionário que ganhava ganhavar R${:.2f} vai começar a ganhar R${:.2f} .'.format(n,(nw1+n)))
            
      n = str(input('\nDeseja recumeçar?[y/n]\n>> '))
 
      if n == 'n':
             exit()
