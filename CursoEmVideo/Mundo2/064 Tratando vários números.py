cont = 0
n = 0
soma = 0
while n != 999:
    n = int(input(' Digite um número ou 999 pra para: '))
    if n != 999:
        cont += 1
        soma += n

print(f'\n Você digitou {cont} números e a soma entre eles foi {soma}.')
