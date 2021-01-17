from os import system

while True:
    system('clear')
    print('  {:=^20}'.format(' MERCADO '))

    preco = float(input(' Preço das compras: R$'))
    print('''\n \033[32m   Formas de pagamentos\033[m
 [1]A vista dinheiro/cheque:
 [2]A vista no Cartão:
 [3]Em ate 2x no cartão:
 [4]3x ou mais no cartão: ''')
    opcao = int(input('\n Qual é a opção? '))

    if opcao == 1:  
         preco2 = preco - (preco*10/100)
    
  
    elif opcao == 2:
         preco2 = preco - (preco*5/100)
    
    
    elif opcao == 3:
         preco2 = preco
         print(' Sua compra será parcelada em 2x de R${:.2f}'.format(preco2 / 2))

    elif opcao == 4:
         preco2 = preco + (preco*20/100)    
         parcela = int(input(' Quantas parcelas? '))
         print(' Sua compra será parcelada em {}x de R${:.2f}'.format(parcela, (preco2/parcela)))
    
    print(' A sua comprar de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco2))
    input('\n Aperte \033[35mEnter\033[m para continuar...')
