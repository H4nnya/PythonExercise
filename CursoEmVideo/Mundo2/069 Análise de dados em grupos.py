maior = 0
man = 0 
girl = 0

while True:
    idade = int(input('Idade:\033[32m '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('\033[m Sexo[M/F]:\033[32m ')).upper()
    if idade > 18:
        maior += 1    
        
    if sexo in 'Mm':
        man += 1
        
    if idade < 20 and sexo in 'Ff':
        girl += 1
    
    opc = str(input('\033[m Quer continuar?[s/n] '))
    if opc in 'Nn':
        break

print(f'\n Total de pessoas com mais de 18 anos: \033[32m{maior}\033[m')
print(f' Ao todo temos \033[32m{man}\033[m homens cadastrado.')
print(f' E Temos \033[32m{girl}\033[m Mulheres com menos de 20 anos.')
