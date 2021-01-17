sexo = str(input(' Digite seu sexo[F/M]: ')).strip().upper()[0]
print(f' {sexo}')
while sexo not in 'FM':
     sexo = str(input(' \033[31mDados inválidos.\033[m Por favor, digite seu sexo: ')).strip().upper()[0]
     
print(f' Sexo \033[32m{sexo}\033[m registrado com sucesso! ')
