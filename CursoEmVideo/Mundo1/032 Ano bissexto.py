from datetime import date
from os import system, name

system('cls' if name == 'nl' else 'clear')
ano = int(input('Digite o ano que queira analisar\n[Ou digite 0 para ver o ano atual]\n>>'))

if ano == 0:
      ano = date.today().year
 
if ano % 2 == 0 and ano % 100 != 0 or ano % 400 == 0:
      print(f'O ano {ano} é BISSEXTO')
 
else:
      print(f'O ano {ano} \033[31mnão\033[m é BISSEXTO')
