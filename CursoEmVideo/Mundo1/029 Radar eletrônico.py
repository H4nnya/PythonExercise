n = float(input('Qual é a velocidade atual do carro? km/h'))

valor = n*7-80*7

if n <= 80:
      print('\033[32m Tenha um bom dia! Dirija com segurança.\033[m')
elif n >= 81:
      print('\033[33m Você está indo muito rápido.\n\033[31mSua multa é de R${:.2f}\033[m'.format(valor))
