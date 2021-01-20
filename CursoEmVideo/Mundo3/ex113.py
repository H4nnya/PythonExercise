def leiaInt(msg):
    while True:
        inteiro = str(input(msg))
        try:
            inteiro = int(inteiro)
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            inteiro = int(inteiro)
            break
    return inteiro


def leiaFloat(msg):
    while True:
        real = str(input(msg))
        try:
            real = float(real)
        except (ValueError, TypeError):
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")
        except KeyboardInterrupt:
            print('O usuário interrompeu o programa')
        else:
            real = float(real)
            break
    return real

n1 = leiaInt("Digite um número inteiro: ")
n2 = leiaFloat("Digite um número real: ")
print(f'Você digitou o número inteiro {n1} e o número real {n2}')