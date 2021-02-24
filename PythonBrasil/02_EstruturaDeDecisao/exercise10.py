"""
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
turno = str(input('Digite o turno que você estuda[M/V/N]: '))[0]
if turno in 'Mm':
    print('BOA DIA!')
elif turno in 'Vv':
    print('BOA TARDE!')
elif turno in 'Nn':
    print('BOA NOITE!')
else:
    print('Valor inválido!')
