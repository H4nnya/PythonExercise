"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e
o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante :aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
"""
print('     REAJUSTE SALARIAL')
pos = 0
sal = str(input('Digite o seu salário bruto: R$')).replace(',', '.')
sal = float(sal)
if sal <= 280:
    pos = 20
    al = (sal * pos) / 100
elif sal <= 700:
    pos = 15
    al = (sal * pos) / 100
elif sal <= 1500:
    pos = 10
    al = (sal * pos) / 100
elif sal > 1500:
    pos = 5
    al = (sal * pos) / 100

print(f"O seu salário antes da aplicação: R${str(sal).replace('.',',')}")
print(f"O aumento do seu salário foi de {pos}%")
valor = f'{al:.2f}'
print(f"O valor do aumento foi R${str(valor).replace('.',',')}")
total = f'{sal + al:.2f}'
print(f"O seu novo salário é de R${total.replace('.',',')}")
