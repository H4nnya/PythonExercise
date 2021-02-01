""""
Exercício: 15
Objetivo: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
xx8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a)salário bruto.
b)quanto pagou ao INSS.
b)quanto pagou ao sindicato.
c)o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
"""
salario_bruto = float(input('Digite o seu Salário: '))
ir = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sindicato = (salario_bruto * 5) / 100
desconto = ir + inss + sindicato
print(f'O seu salario de R${salario_bruto:.2f} com os descontos fica R${salario_bruto - desconto:.2f}')
