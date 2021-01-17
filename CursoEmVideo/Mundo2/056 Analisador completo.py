media = 0
maiorh = 0
nomev = ''
totf = 0
for p in range(1,5):
    print(f' ---- {p}ªPessoa ---')
    nome = str(input(' Nome: '))
    idade = int(input(' Idade: '))
    sexo = str(input(' Sexo[F/M]: ')).strip()
    if p == 1 and sexo in 'Mm':
         maiorh = idade
         nomev = nome
    if sexo in 'Mm' and idade > maiorh:
         maiorh = idade
         nomev = nome
    if sexo in 'Ff' and idade < 20:
         totf += 1
    media += idade / 4
print(' A media de idade é: {:.2f}'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorh, nomev))
print(f' Ao todo são {totf} mulheres com menos de 20 anos.')
