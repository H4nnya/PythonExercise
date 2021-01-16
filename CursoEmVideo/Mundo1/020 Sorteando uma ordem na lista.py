from random import shuffle

a1 = str(input('Nome do 1° Aluno: '))
a2 = str(input('Nome do 2° Aluno: '))
a3 = str(input('Nome do 3° Aluno: '))
a4 = str(input('Nome do 4° Aluno: '))

lista = [a1,a2,a3,a4]
shuffle(lista)
print('a ordem de quem vai entregar o trabalho primeiro:\n{}'.format(lista))
