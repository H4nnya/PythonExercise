n = 'ok'
while n == 'ok':	
 v1 = int(input('Digite o primeiro valor: '))
 v2 = int(input('Digite o segundo valor: '))
 v3 = int(input('Digite o terceiro valor: '))
 lista = [v1,v2,v3]
 
 print('O maior número é {}'.format(max(lista)))
 print('O menor número é {}'.format(min(lista)))
 n = str(input('Digite \033[32mok\033[m para reiniciar o programar ou \033[31mexit\033[m para encerrar\n»'))
 
 if n == 'exit':
        exit()
