"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
sexo = str(input('Digte o seu sexo[F/M]: '))[0]
print('Seu sexo é ', end='')
if sexo in 'Ff':
    print('feminino.')
elif sexo in 'Nn':
    print('Masculino.')
else:
    print('Inválido.')
