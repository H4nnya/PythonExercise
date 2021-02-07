"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = str(input('Digite uma letra: ')).upper()[0]
print(f"A letra {letra} é ", end='')
if letra in 'AEIOU':
    print('VOGAL.')
else:
    print('CONSOANTE.')
