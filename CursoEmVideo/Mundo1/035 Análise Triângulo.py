n = 's'
while n == 's':
     print('=-'*20)
     print('     \033[33m  Analiser de triângulo\033[m')
     print('=-'*20)
 
     s1 = float(input(' Primeiro segmento: '))
     s2 = float(input(' Segundo segmento: '))
     s3 = float(input(' Terceiro segmento: '))

     if s1 < s2+s3 and s2 < s3+s1 and s3 < s1+s2:
            print('\n É possível formar um triângulo.')
     else:
            print('\n Não é possível formar um triângulo.')
    
     n = str(input('\n Desejar reiniciar? [s/n]\n >>'))
     if n == 'n':
            exit()
