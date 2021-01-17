from datetime import datetime
from os import system

now = datetime.now()
year = now.year

maior = 0
menor = 0

while True:
    system('clear')
    for c in range(1, 8):
         nas = int(input(f'\033[m Em que ano o {c}° nasceu? \033[32m'))
         if 18 <= ( year - nas):
              maior +=1
         else:
              menor +=1

    input(f'\033[m {maior} pessoas são maior de idade.\n {menor} são menor de idade.')
