dis = float(input('Qual é a distância da viagem? '))

if dis <= 200:
       print(f' Você esta preste a fazer uma viagem de {dis}Km.')
       print(' E o preço da sua passagem será R${:.2f}'.format(dis * 0.50))
       
elif dis >= 201:
       print(f' Você está preste a fazer uma viagem de {dis}km.')
       print(' E o preço da sua passagem será R${:.2f}'.format(dis * 0.45))
