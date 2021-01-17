from os import system
system('clear')

print('=-'*20)
print('     MERCADO SENNA')
tot = cont = menor = maior = 0
name = ''
while True:
    print('=-'*20)
    prod = str(input(' Nome do produto: '))
    preco = float(input(' Preço: R$'))
    tot += preco
    opc = ' '
    while opc not in 'NnSs':
         opc = str(input(' Quer continuar?[S/N] ')).upper()[0]
    cont += 1
    if preco > 1000:
         maior += 1 
    
    if cont == 1 or preco < menor:
          menor = preco
          nome = prod
        
    if opc in 'Nn':
          break
        
print('\n', '=-'*20)       
print(f' O total da compra foi R${tot:.2f}')
print(f' Temos {maior} produto custando mais de R$1000.00')
print(f' O produto mais barato foi {nome} que custou R${menor}')
print('=-'*20)
