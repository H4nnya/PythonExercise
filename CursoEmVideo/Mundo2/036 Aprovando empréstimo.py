casa = float(input(' valor da casa: R$'))
salario = float(input(' Salário mensal ? '))
anos = int(input('Quabtos anos? '))

mensal = casa /  (anos*12)
porcentagem = salario*30 / 100

print('Para pagar uma casa de R${:.2f} em {:.0f} anos, o preço mensal é de R${:.2f}'.format(casa, anos, mensal))
print(f'O mínimo do seu salário é de: R${porcentagem}')

if mensal <= porcentagem:
       print('\033[32m Empréstimo aceito! \033[m')
else:
       print('\033[31m Empréstimo negado! \033[m')
