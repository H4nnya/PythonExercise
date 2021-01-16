name = str(input('Digite seu nome completo: ')).strip()
n = ('{}'.format('SILVA'in name.upper()))

if n == 'True':
    print('Seu bome tem silva? \033[32mTrue\033[m')
else:
    print('Seu nome tem Silva: \033[31mFalse\033[m')
