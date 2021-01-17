from random import randint
point = 0

while True:
    cpu = randint(1, 20)
    n = int(input(' Digite um valor(0 a 20): '))
    ip = str(input(' par ou ímpar?[p/i] ')) 
    tot = (n + cpu)%2
    print('='*20)
    print(f' CPU jogou: {cpu}\n Player jogou: {n}')
    print('='*20)
    
    if tot == 0 and ip in 'Pp':
         print(' \033[32mvocê ganhou!\033[m')
         point += 1
        
    elif tot != 0 and ip in 'Ii':
         print(' \033[32mVocê ganhou!\033[m')
         point += 1                 
        
    else:
         print(f' \033[31mGamer over!\033[m\n Você ganhou {point} vezes.')
         break
    
