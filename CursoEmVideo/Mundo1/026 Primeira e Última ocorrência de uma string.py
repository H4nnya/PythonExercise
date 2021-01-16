name = str(input('Digite uma frase: ')).upper()

print(' A letra A aparece {} vezes na frase. '.format(name.count('A')))
print(' A primeira letra A aparece na posição: \033[32m{}\033[m '.format(name.find('A')+1))
print(' A última letra A aparece na posição {}'.format(name.rfind('A')+1))
