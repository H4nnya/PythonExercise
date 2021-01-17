soma = valor = 0
while True:
    n = int(input(' Digite um número [ou 999 para parar]: '))
    if n == 999:
        break
    valor += 1
    soma += n
print(f' Você digitou {valor} valores e a soma entre eles foi {soma}.')
