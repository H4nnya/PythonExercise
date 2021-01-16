name = str(input('Digite seu nome inteiro: ')).strip()

n = name.find(' ')+1
print(f'Foi um prazer em te conhecer, \033[32m{name[:n]}\033[m.')
nome = name.split()
print('Seu ultimo nome é: \033[32m{}\033[m.'.format(nome[len(nome)-1]))
