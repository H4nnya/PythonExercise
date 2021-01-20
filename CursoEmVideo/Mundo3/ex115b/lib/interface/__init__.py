def leiaInt(msg):
    while True:
        inteiro = str(input(msg))
        try:
            int(inteiro)
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        else:
            inteiro = int(inteiro)
            break
    return inteiro


def linha(tam=42):
    return "-" * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho("Menu Principal")
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc
