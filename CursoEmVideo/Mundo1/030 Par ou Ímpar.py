num = int(input(' Me digame um número qualquer: '))
valor = num%2

if valor == 0:
      print(f' \033[32mO número {num} é PAR.\033[m')
else:
      print(f' \033[32mO número {num} é ÍMPAR.\033[m')
