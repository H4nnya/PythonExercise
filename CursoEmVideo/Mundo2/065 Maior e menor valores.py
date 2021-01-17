go = 's'
media = cont = n = maior = menor = 0

while go in 'Ssim':
    n = int(input(' Digite um número: '))
    go = str(input(' Quer continuar?[s/n] ')).lower()
    cont += 1
    media += n
    if cont == 1:
         maior = menor = n
    else:
         if n > maior:
              maior = n 
         if n < menor:
              menor = n
     
print(' Você digitou {:.0f} números e a media foi {:.2f}.'.format(cont, media / cont))
print(f' O maior número foi {maior} e o menor número foi {menor}.')
