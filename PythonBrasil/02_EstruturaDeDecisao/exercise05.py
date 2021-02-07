"""
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
 ° A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
 ° A mensagem "Reprovado", se a média for menor do que sete;
 ° A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2
print(f'Com {media} de média o aluno foi ', end='')
if media == 10:
    print("Aprovado com distinção.")
elif media >= 6:
    print("Aprovado.")
else:
    print('Replovado.')
