"""
exercise: 013
objective: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
sal = float(input('Qual é o salario do funcionário? R$'))
aum = sal + (sal * 15 / 100)
print(f'Um fucionário que ganhava R${sal}, com 15% de aumento, passa a receber \033[32mR${aum:.2f}\033[m.')
